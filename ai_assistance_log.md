# AI Assistance & Provenance Log

This log documents AI-assisted development and human verification steps in accordance with responsible AI research-integrity rules.

| # | Task / Stage | Tool Used | AI Proposal / Output | Human Verification & Decision | Outcome |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | LaTeX Manuscript Structuring (`Overleaf_Final_Paper.pdf`) | Overleaf / LaTeX Assistant | Structured sections, conceptual diagrams, and tables organizing literature on citation formatting and trust. | Verified all citations against source papers (Walters & Wilder, 2023; Ding et al., 2025; Besançon et al., 2024; Topaz et al., 2026) and added explicit scope notes distinguishing theoretical hypotheses from empirical data. | Accepted with manual revisions (`paper/Overleaf_Final_Paper.pdf`). |
| 2 | Crossref Verification Script (`ATR Python code.py` -> `src/verify_citation.py`) | Google Colab / AI Coding Assistant | Generated initial Crossref API lookup script using `requests` and `difflib.SequenceMatcher`. | Reviewed similarity thresholds (`0.90` title, `0.80` author/venue), added DOI prefix normalization (`https://doi.org/`), and enforced conservative decision labels (`POSSIBLE GENUINE MATCH` instead of claiming absolute proof). | Modularized into `src/verify_citation.py` and `scripts/run_verification.py`. |
| 3 | GitHub Repository Packaging | AI Assistant | Organized repository directory tree matching lab specification (`configs/`, `data/`, `notebooks/`, `src/`, `scripts/`, `results/`, `paper/`, and provenance `.md` files). | Verified that both original PDFs in `paper/` were copied byte-for-byte without modification and that all imports and paths resolve cleanly. | Packaged as `AITR_Lab02_Project.zip`. |
