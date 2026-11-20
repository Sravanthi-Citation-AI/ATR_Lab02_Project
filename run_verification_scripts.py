# -*- coding: utf-8 -*-
"""CLI entrypoint for interactive academic reference verification."""

import os
import sys

# Ensure project root is on sys.path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.verify_citation import verify_paper


def format_report(result):
    """Format a verification dictionary into a readable CLI report."""
    lines = [
        "-" * 55,
        "VERIFICATION REPORT",
        "-" * 55,
    ]
    for key, value in result.items():
        if key == "criteria":
            lines.append("
CRITERIA CHECKS:")
            for criterion, passed in value.items():
                status = (
                    "NOT CHECKED" if passed is None
                    else "PASS" if passed
                    else "MISMATCH"
                )
                lines.append(f"  {criterion}: {status}")
        else:
            lines.append(f"{key.replace('_', ' ').title()}: {value}")

    lines.append("
Note: This is a preliminary verification, not proof of authenticity.")
    return "
".join(lines)


def main():
    print("=" * 55)
    print("ACADEMIC REFERENCE VERIFICATION SYSTEM")
    print("=" * 55)

    title = input("Enter paper title: ")
    authors = input("Enter authors (separate multiple authors with ;): ")
    year = input("Enter publication year: ")
    venue = input("Enter journal/conference name: ")
    doi = input("Enter DOI (or press Enter if unavailable): ")

    result = verify_paper(title, authors, year, venue, doi)
    print("
" + format_report(result))


if __name__ == "__main__":
    main()
