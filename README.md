#  Contract Analysis & Risk Assessment Bot

## Project Overview

The **Contract Analysis & Risk Assessment Bot** is a system designed to help **small and medium businesses (SMEs)** understand complex legal contracts, identify potential risks, and receive clear, actionable insights in simple business language.

The platform processes contracts such as:

* Employment Agreements
* Vendor & Service Contracts
* Lease Agreements
* Partnership Deeds

The system follows a **structured, explainable pipeline** that transforms raw legal documents into clause-level insights and risk indicators, while maintaining confidentiality and compliance with hackathon constraints.

---

##  Project Objectives

* Convert unstructured contracts into **structured clauses**
* Explain clauses in **simple business language**
* Identify **unfavorable or risky terms**
* Assign **clause-level and contract-level risk scores**
* Support **English and Hindi contracts**
* Maintain **privacy, auditability, and explainability**

---

##  High-Level System Flow

```
Contract Upload
      ↓
Metadata Capture
      ↓
Text Extraction & Language Detection
      ↓
Clause Segmentation & Structuring
      ↓
Clause-Level Analysis
      ↓
Risk Scoring & Aggregation
      ↓
Summary Report Generation
```

---

##  Tech Stack

### Core Technologies

* **Python**

### Document Processing

* **PyMuPDF** – PDF text extraction
* **python-docx** – DOC/DOCX extraction
* **Native Python** – TXT files

### Text & NLP Processing

* **Regex (re)** – rule-based clause segmentation
* **langdetect** – language detection (English / Hindi)

### AI / Analysis

* **LLM (GPT-4 )** – clause explanation & risk reasoning
  *(Used only for text analysis, not legal advice)*

### Output & Processing

* **JSON** – structured clause representation
* **In-memory processing** – no data persistence

---

##  Phase 1: Contract Ingestion & Metadata

### What Happens

* User uploads a contract (PDF / DOC / TXT)
* System captures:

  * File type
  * Contract size
  * Optional contract category

### Design Choice

* Files are processed **temporarily**
* No contracts are stored permanently

---

##  Phase 2: Clause Extraction & Structuring (Core Foundation)

### Objective

Transform raw contract text into **clean, structured, language-aware clauses**.

### Key Capabilities

* Multi-format text extraction
* Noise-tolerant preprocessing
* Rule-based clause splitting
* Multilingual language detection

### Clause Segmentation Logic

* Detects numbered clauses (`1`, `1.1`, `2.3`, etc.)
* Preserves original wording
* Avoids data loss (audit-safe)

### Clause Output Structure

```json
{
  "clause_id": "C5",
  "title": "Termination",
  "text": "Either party may terminate...",
  "position": 5,
  "language": "en"
}
```

This structure enables:

* Explainability
* Risk scoring
* Downstream AI processing

---

##  Phase 3: Clause-Level Risk Analysis

### Purpose

Identify **business risk**, not legal judgment.

### What the System Analyzes

For each clause, the system determines:

* Clause intent (e.g., termination, liability, confidentiality)
* Presence of **one-sided or unfavorable terms**
* Risk triggers based on predefined patterns

### Examples of Risk Indicators

* Termination without notice
* Unlimited liability
* Excessive penalties
* Foreign jurisdiction clauses
* Missing dispute resolution

### Risk Categories

* **Low Risk** – Standard, balanced clauses
* **Medium Risk** – Needs attention or clarification
* **High Risk** – Potentially harmful to SMEs

---

## Phase 4: Risk Scoring & Aggregation

### Clause-Level Scoring

* Each clause receives a **risk severity score**
* Score is based on:

  * Clause type
  * Detected risk indicators
  * Contract context

### Contract-Level Risk

* Clause scores are aggregated to determine:

  * Overall contract risk level
  * Top risky clauses
  * Priority areas for review

---

##  Phase 5: Summary & Insights

The system generates:

* Plain-language contract summary
* List of **high-risk clauses**
* Suggested areas for mitigation
* Business-friendly explanations

This allows SMEs to:

* Understand contracts without legal background
* Decide when to consult a legal expert

---

## Multilingual Support

* Contracts in **English and Hindi**
* Language detected at clause level
* Enables inclusive access for Indian SMEs

---

##  Privacy & Compliance

* All processing is **in-memory**
* No contract data stored
* No external legal databases
* No case law integration
* Fully compliant with hackathon constraints

---

## Out of Scope (By Design)

* Legal advice or legal validation
* Court judgments or case law references
* Persistent data storage
* External legal APIs

---

##  Design Principles

* **Explainable over opaque**
* **Deterministic before AI**
* **Risk awareness, not legal advice**
* **Privacy-first architecture**
* **Modular & extensible**

---

##  Team Contributions

* **Clause Extraction & Structuring (Phase 2)**

  * Document parsing
  * Rule-based segmentation
  * Multilingual handling
  * Structured output design

* **Risk Analysis & Scoring**

  * Clause interpretation
  * Risk categorization
  * Contract-level aggregation

---

##  Disclaimer

This system provides **contract understanding and risk awareness only**.
It does **not** provide legal advice and should not replace professional legal consultation.


