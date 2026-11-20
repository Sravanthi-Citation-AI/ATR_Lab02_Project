# Research Decisions: Literature-to-Experiment Log

## 1. Identified Literature Gap
- Existing studies establish that **citation presence** increases perceived credibility in AI-generated answers (Ding et al., 2025) and that **fabricated references** appear at scale in peer-reviewed literature with realistic formatting (Walters & Wilder, 2023; Topaz et al., 2026).
- However, direct experimental evidence isolating **citation formatting** (completeness, consistency, style, persistent identifier presence) from source validity remains limited (`paper/ATR MNS_11_final.pdf`, Section 6 & Section 7).

## 2. Operationalizing Verification
- Because visual formatting cues (e.g., well-structured author-date entries or DOI-like strings) can create an appearance of verifiability before checking, the experimental baseline separates **pre-verification presentation** from **post-verification bibliographic existence**.
- `src/verify_citation.py` implements an automated Crossref metadata verification check using DOI resolution (`https://api.crossref.org/works/{doi}`) with fallback title search (`query.title`) and sequence-similarity thresholds (`>= 0.90` for titles, `>= 0.80` for authors and venues).

## 3. Scope Boundaries
- The automated checker detects missing records, non-resolving DOIs, and field mismatches (`INCONSISTENT - MANUAL REVIEW` vs. `UNVERIFIED` vs. `POSSIBLE GENUINE MATCH`).
- It explicitly avoids claiming proof of authenticity or semantic claim support, aligning with the paper's distinction between metadata existence and evidentiary validity.

## 4. Extended Heuristic & Anti-Monitoring Decisions (Topic Alignment)
- **Authority & Trust-Transfer Heuristics (MAIN Model & Hu & Sundar):** Visual formatting cues—such as APA author-date vs. numbered styles, complete bibliographic fields, and DOI strings—can act as heuristic authority signals that transfer perceived credibility from presentation to unverified claims. Our experimental framing therefore treats formatting as a pre-verification cue rather than an indicator of factual validity.
- **Anti-Monitoring & Verification Cost:** Empirical evidence on LLM-generated citations (Ding et al., 2025) indicates that citations can boost trust even when irrelevant if users do not click or check them, and that trust drops primarily upon active inspection. Consequently, our verification pipeline (`src/verify_citation.py`) is designed to lower verification friction at the metadata layer while preserving manual review flags (`INCONSISTENT - MANUAL REVIEW`) for ambiguous or mismatched records.
- **Heterogeneity of Fabricated & Mismatched Citations:** Rather than collapsing all suspicious references into a single "fake" label, we separate non-existent/unmatched records (`UNVERIFIED`) from metadata or DOI-to-title discrepancies (`INCONSISTENT - MANUAL REVIEW`), reflecting distinctions noted in our literature review and audits (such as fabricated references, metadata mismatches, and sparse contamination in scholarly corpora).
- **Multi-Source & Downstream Contamination Awareness:** Because single-index lookups can miss records or encounter publisher metadata anomalies, Crossref checks are framed as a reproducible baseline rather than a sole arbiter of truth, especially given warnings about citation contamination propagating through repositories and downstream AI training corpora.
