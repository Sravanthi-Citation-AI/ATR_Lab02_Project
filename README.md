# The Influence of Citation Formatting on Human Trust in Fabricated Resources

## Research Question & Overview
**Research Question:** How does citation formatting influence perceived trustworthiness and verification behavior when a cited scholarly resource is fabricated or non-existent?

This repository accompanies the research paper *"The Influence of Citation Formatting on Human Trust in Fabricated Resources"* and provides a reproducible Crossref REST API metadata verification baseline (`src/verify_citation.py`) to check whether cited works exist and whether their metadata fields match authoritative bibliographic records.

## Repository Structure
```text
AITR_Lab02_Project/
├── README.md                  # Research question and reproducibility guide
├── requirements.txt           # Verified Python dependencies
├── configs/                   # Frozen experimental settings
│   └── verification_config.yaml
├── data/                      # Dataset access & input specification (no restricted raw data)
│   └── README.md
├── notebooks/                 # Exploration and verified runnable notebook
│   └── Citation_Formatting_Trust_Research.ipynb
├── src/                       # Reusable verification functions
│   └── verify_citation.py
├── scripts/                   # CLI entrypoint and batch evaluation scripts
│   └── run_verification.py
├── results/                   # Genuine metric/log files and structured verification outputs
│   ├── sample_verification_report.txt
│   └── sample_verification_results.csv
├── paper/                     # Final research papers (unmodified)
│   ├── ATR MNS_11_final.pdf
│   └── Overleaf_Final_Paper.pdf
├── research_decisions.md      # Literature-to-experiment decisions
├── baseline_validation.md     # Reproduction checks and deviations
└── ai_assistance_log.md       # Significant prompts and human verification
```

## Setup & Reproducibility
1. **Clone the repository and navigate to the project root:**
   ```bash
   cd AITR_Lab02_Project
   ```
2. **Install verified dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the interactive citation verification entrypoint:**
   ```bash
   python scripts/run_verification.py
   ```
   *(Note: Requires outbound HTTPS access to `https://api.crossref.org/works`.)*

## Scope & Limitations
- The Crossref verification module checks bibliographic existence and field-level consistency (title, authors, publication year, venue, and DOI).
- It serves as a preliminary bibliographic check and does **not** prove whether a real cited source actually supports the claim made in running text.
