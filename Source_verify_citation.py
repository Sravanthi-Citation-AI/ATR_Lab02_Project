# -*- coding: utf-8 -*-
"""Reusable Crossref bibliographic verification functions.

Research: The Influence of Citation Formatting on Human Trust in Fabricated Resources
"""

import requests
from difflib import SequenceMatcher

CROSSREF_API = "https://api.crossref.org/works"


def similarity(a, b):
    """Compare two strings using case-insensitive sequence matching."""
    return SequenceMatcher(
        None, a.casefold().strip(), b.casefold().strip()
    ).ratio()


def verify_paper(title, authors="", year="", venue="", doi=""):
    """Compare user-provided paper details with Crossref metadata."""

    if not title.strip():
        return {
            "decision": "INVALID INPUT",
            "reason": "Paper title is required.",
        }

    try:
        # Search by DOI when provided; otherwise search by title.
        if doi.strip():
            clean_doi = doi.strip()
            clean_doi = clean_doi.removeprefix(
                "https://doi.org/"
            ).removeprefix("http://doi.org/")

            url = f"{CROSSREF_API}/{clean_doi}"
            response = requests.get(url, timeout=15)
            response.raise_for_status()
            records = [response.json()["message"]]

        else:
            response = requests.get(
                CROSSREF_API,
                params={"query.title": title, "rows": 5},
                timeout=15,
            )
            response.raise_for_status()
            records = response.json()["message"]["items"]

    except requests.RequestException:
        return {
            "decision": "UNVERIFIED",
            "reason": "Crossref could not be reached or no DOI record was accessible. Retry later.",
        }

    if not records:
        return {
            "decision": "UNVERIFIED",
            "reason": "No matching Crossref records found. This alone does not prove fabrication.",
        }

    best_record = None
    best_score = -1

    for record in records:
        titles = record.get("title", [])
        if not titles:
            continue

        title_score = similarity(title, titles[0])

        if title_score > best_score:
            best_score = title_score
            best_record = record

    if best_record is None:
        return {
            "decision": "UNVERIFIED",
            "reason": "Crossref returned no usable title records.",
        }

    record = best_record
    matched_title = record.get("title", [""])[0]
    record_doi = record.get("DOI", "")
    record_year = (
        record.get("published", {})
        .get("date-parts", [[None]])[0][0]
    )
    record_venue = record.get("container-title", [""])
    record_venue = record_venue[0] if record_venue else ""

    record_authors = [
        " ".join(filter(None, [
            author.get("given", ""),
            author.get("family", "")
        ]))
        for author in record.get("author", [])
    ]

    # Evaluate each available field.
    checks = {
        "Title matches": best_score >= 0.90,
        "Year matches": (
            str(year).strip() == str(record_year)
            if year.strip() and record_year else None
        ),
        "Venue matches": (
            similarity(venue, record_venue) >= 0.80
            if venue.strip() and record_venue else None
        ),
        "Author matches": (
            any(
                similarity(user_author, record_author) >= 0.80
                for user_author in authors.split(";")
                for record_author in record_authors
            )
            if authors.strip() and record_authors else None
        ),
        "DOI matches": (
            doi.strip().lower().removeprefix("https://doi.org/").removeprefix("http://doi.org/")
            == record_doi.lower()
            if doi.strip() else None
        ),
    }

    # A supplied DOI must resolve to a matching title.
    if doi.strip() and best_score < 0.90:
        decision = "INCONSISTENT - MANUAL REVIEW"
        reason = "The supplied DOI record's title does not sufficiently match the submitted title."
    elif best_score < 0.90:
        decision = "UNVERIFIED"
        reason = "No sufficiently similar title was found in the retrieved records."
    elif any(value is False for value in checks.values()):
        decision = "INCONSISTENT - MANUAL REVIEW"
        reason = "One or more supplied fields disagree with the Crossref record."
    else:
        decision = "POSSIBLE GENUINE MATCH"
        reason = "A matching Crossref record was found. Verify the metadata and source before confirming authenticity."

    return {
        "decision": decision,
        "reason": reason,
        "submitted_title": title,
        "matched_title": matched_title,
        "submitted_authors": authors,
        "record_authors": "; ".join(record_authors),
        "submitted_year": year,
        "record_year": record_year,
        "submitted_venue": venue,
        "record_venue": record_venue,
        "submitted_doi": doi,
        "record_doi": record_doi,
        "title_similarity": round(best_score, 3),
        "criteria": checks,
    }
