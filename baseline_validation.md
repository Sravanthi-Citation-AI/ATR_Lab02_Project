# Baseline Validation & Reproduction Checks

## 1. Environment & Dependency Check
- **Python Version:** Python 3.10+
- **Dependencies:** `requests>=2.31.0` (listed in `requirements.txt`).
- **Entrypoint:** `python scripts/run_verification.py` imports `verify_paper` from `src/verify_citation.py`.

## 2. Deterministic Logic & Edge-Case Verification
| Test Case | Input Condition | Expected Decision | Status |
| :--- | :--- | :--- | :--- |
| Empty Title | `title=""` | `INVALID INPUT` (`Paper title is required.`) | Verified |
| DOI Prefix Normalization | `doi="https://doi.org/10.1038/s41598-023-41032-5"` | Strips `https://doi.org/` cleanly before querying Crossref | Verified |
| Network / API Failure | `requests.RequestException` | `UNVERIFIED` (graceful error handling without crash) | Verified |
| Title Mismatch on Supplied DOI | `doi` resolves to record with `title_similarity < 0.90` | `INCONSISTENT - MANUAL REVIEW` | Verified |

## 3. Known Deviations & Limitations
- Crossref metadata coverage varies across conference proceedings, preprints, and non-DOI books; an `UNVERIFIED` result indicates absence from retrieved Crossref records rather than definitive proof of fabrication.
- Live Crossref API queries require outbound internet connectivity.

## 4. Extended Validation Checks (Thresholds, Multi-Author & Field Mismatches)
| Test Case | Input Condition / Rule | Expected Behavior & Decision | Status |
| :--- | :--- | :--- | :--- |
| Title Similarity Boundary | `best_score >= 0.90` vs. `best_score < 0.90` | Records with title ratio `< 0.90` without a matching DOI return `UNVERIFIED` (`No sufficiently similar title was found in the retrieved records.`). | Verified |
| Year Mismatch | Supplied `year` differs from `record_year` when both are non-empty | Marks `Year matches` as `False` (`MISMATCH`) and sets decision to `INCONSISTENT - MANUAL REVIEW`. | Verified |
| Venue Similarity Threshold | Supplied `venue` similarity `< 0.80` against `record_venue` | Marks `Venue matches` as `False` (`MISMATCH`) and flags `INCONSISTENT - MANUAL REVIEW`. | Verified |
| Semicolon-Delimited Authors | Multiple authors split on `;` with `similarity >= 0.80` against any `record_authors` entry | Marks `Author matches` as `True` (`PASS`) if at least one author pair meets the `0.80` threshold; `None` (`NOT CHECKED`) if omitted or record lacks authors. | Verified |
| HTTP vs. HTTPS DOI Stripping | `http://doi.org/...` and `https://doi.org/...` inputs | Normalizes both schemes prior to querying `https://api.crossref.org/works/{clean_doi}` and comparing against `record_doi.lower()`. | Verified |
| Non-Existent / Hallucinated Citation Simulation | Plausible formatted citation with non-existent DOI or zero matching Crossref items | Returns `UNVERIFIED` with explicit note that absence from Crossref alone does not prove fabrication and requires manual check. | Verified |
