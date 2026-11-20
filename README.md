# ATR_Lab02_Project
# The Influence of Citation Formatting on Human Trust in Fabricated Resources

## Research Question & Overview
**Research Question:** How does citation formatting influence perceived trustworthiness and verification behavior when a cited scholarly resource is fabricated or non-existent?[cite: 3, 29, 109]

This repository supports research on **The Influence of Citation Formatting on Human Trust in Fabricated Resources**, examining how visible citation formatting cues—such as citation style (author-date vs. numbered), bibliographic completeness, consistency, and persistent identifiers (DOIs)—shape initial credibility before verification[cite: 3, 29, 109]. Alongside the manuscripts, it includes a reproducible Crossref metadata verification baseline (`src/verify_citation.py`) to check whether cited works exist and compare submitted bibliographic fields against Crossref records.

## Literature & Empirical Context
- **Anti-Monitoring & Trust in AI Citations:** Experimental research on LLM-generated responses shows that the presence of citations can increase perceived trust—even when citations are random or irrelevant—while trust drops when users actually check citations[cite: 109, 111].
- **Heuristic Credibility & Trust Transfer:** Frameworks such as the **MAIN Model** and trust-transfer cues explain how formal presentation and authority signals can lower verification effort and transfer perceived credibility to unverified statements[cite: 109].
- **Fabricated Citations in the Scholarly Record:** Large-scale audits—including an audit of 2.5 million biomedical papers (`The Lancet`, 2026) and a 2020–2025 analysis of preprints and repositories—document rising occurrences of fabricated or hallucinated citations and highlight risks of downstream contamination[cite: 109, 110].

## Repository Structure

AITR_Lab02_CitationFormattingTrust/

├── README.md                                       
├── requirements.txt                                
├── configs/                                       
│   └── verification_config.yaml
├── data/                                           
│   └── README.md
├── notebooks/                                      
│   └── Citation_Formatting_Trust_Research.ipynb
├── src/                                            
│   ├── __init__.py
│   └── verify_citation.py
├── scripts/                                        
│   └── run_verification.py
├── results/                                         
│   ├── sample_verification_report.txt
│   └── sample_verification_results.csv
├── paper/                                           # Unmodified research papers
│   ├── ATR MNS_11_final.pdf
│   └── Overleaf_Final_Paper.pdf
├── research_decisions.md                            # Literature-to-experiment decisions
├── baseline_validation.md                           # Reproduction checks, edge cases, and limitations
└── ai_assistance_log.md                             # AI-assisted tasks and human verification log
