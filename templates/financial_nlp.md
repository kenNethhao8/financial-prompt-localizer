# Financial NLP Prompt Template

```text
Task:
Analyze or extract structured information from [news / reports / announcements / transcripts].

Context:
The user wants financial text converted into research-ready structured data.

Requirements:
- Define document type, timestamp, source, company or ticker mapping, and extraction fields.
- Separate text evidence from model inference.
- Include confidence flags and source references.
- Avoid treating extracted opinions as investment advice.
- Respect copyright limits when quoting source text.

Inputs and assumptions:
- Required fields: document_id, source, publication time, text, ticker/company mapping if available.

Output format:
- Return structured JSON or CSV-ready rows.
- Include fields for extracted thesis, sentiment, event type, risk warnings, target price, or catalysts as relevant.

Validation:
- Check duplicate articles, timestamp alignment, missing tickers, and repeated syndicated content.
```
