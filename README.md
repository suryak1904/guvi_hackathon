
# Contract Analysis & Risk Assessment Bot

## Overview

The **Contract Analysis & Risk Assessment Bot** is a GenAI-powered assistant designed to help **Small and Medium Enterprises (SMEs)** understand complex legal contracts, identify potential business risks, and make informed decisions **before signing**.

The system analyzes contracts at the **clause level**, translating dense legal language into **clear, business-friendly explanations**, highlighting unfavorable terms, and generating risk insights—while maintaining strict privacy and compliance with hackathon constraints.

### Supported Contract Types
- Employment Agreements  
- Vendor & Service Contracts  
- Lease Agreements  
- Partnership Deeds  

---

## Project Objectives

- Convert unstructured legal contracts into **structured, explainable clauses**
- Provide **plain-language explanations** for each clause
- Identify **unfavorable, one-sided, or risky terms**
- Assign **clause-level and contract-level risk scores**
- Support **multilingual contracts (English & Hindi)**
- Ensure **privacy, transparency, and auditability**
- Remain **compliant with tool and data restrictions**

---

## High-Level System Flow

```

Contract Upload
↓
Metadata Capture
↓
Text Extraction & Language Detection
↓
Clause Segmentation & Structuring
↓
Clause-Level Risk Analysis
↓
Risk Scoring & Aggregation
↓
Summary & Insights Generation

````

---

## Tech Stack

### Core
- **Python**

### Document Processing
- **PyMuPDF** – PDF text extraction  
- **python-docx** – DOC/DOCX extraction  
- **Native Python** – TXT file handling  

### NLP & Text Processing
- **Regex (re)** – Rule-based clause segmentation  
- **langdetect** – Language detection (English / Hindi)  

### GenAI
- **GPT-4** – Clause explanation and risk reasoning  
  > Used strictly for **text understanding**, not legal advice

### Data Handling
- **JSON** – Structured clause representation  
- **In-memory processing** – No persistent storage  

---

## Phase 1: Contract Ingestion & Metadata

### Functionality
- User uploads a contract (PDF / DOC / TXT)
- System captures:
  - File type
  - File size
  - Optional contract category

### Design Rationale
- Contracts are processed **only within the session**
- No files or extracted text are stored permanently
- Ensures confidentiality and data safety

---

## Phase 2: Clause Extraction & Structuring

### Objective
Transform raw contract text into **clean, structured, language-aware clauses** that can be safely analyzed and audited.

### Key Capabilities
- Multi-format text extraction
- Noise removal (headers, footers, page numbers)
- Rule-based clause segmentation
- Clause-level language detection

### Clause Segmentation Logic
- Identifies numbered clauses (`1`, `1.1`, `2.3`, etc.)
- Preserves original clause wording
- Maintains clause order for traceability

### Clause Data Structure
```json
{
  "clause_id": "C5",
  "title": "Termination",
  "text": "Either party may terminate...",
  "position": 5,
  "language": "en"
}
````

This structure enables:

* Explainability
* Risk attribution
* Audit-safe analysis

---

## Phase 3: Clause-Level Risk Analysis

### Purpose

Identify **business and operational risk**, not legal judgments.

### Analysis Per Clause

* Clause intent (e.g., termination, liability, confidentiality)
* Detection of one-sided or unfavorable terms
* Pattern-based risk indicators
* Plain-language explanation

### Common Risk Indicators

* Termination without notice
* Unlimited or uncapped liability
* Excessive penalties
* Foreign jurisdiction clauses
* Missing dispute resolution mechanisms

### Risk Categories

* **Low Risk** – Standard and balanced clauses
* **Medium Risk** – Requires attention or clarification
* **High Risk** – Potentially harmful for SMEs

---

##  Phase 4: Risk Scoring & Aggregation

### Clause-Level Scoring

* Each clause receives a **risk severity score**
* Based on:

  * Clause type
  * Detected risk indicators
  * Contract context

### Contract-Level Insights

* Aggregated overall risk level
* Identification of top high-risk clauses
* Prioritized areas for review

---

## Phase 5: Summary & Insights

The system generates a **business-friendly summary**, including:

* Overall contract risk assessment
* List of high-risk clauses
* Key areas requiring attention
* Clear explanations to guide next steps

This helps SMEs:

* Quickly understand complex contracts
* Decide when professional legal consultation is required

---

## Multilingual Support

* Supports **English and Hindi contracts**
* Language detected at clause level
* Ensures accessibility for Indian SMEs

---

## Privacy & Compliance

* All processing is **session-based and in-memory**
* No contract data is stored or logged
* No integration with:

  * Legal databases
  * Case law systems
  * External legal APIs
* Fully compliant with hackathon tool restrictions

---

## Out of Scope (By Design)

* Legal advice or legal validation
* Statutory interpretation or case law references
* Persistent data storage
* External legal API integrations

---

##  Design Principles

* **Explainability over opacity**
* **Deterministic logic before GenAI**
* **Risk awareness, not legal advice**
* **Privacy-first architecture**
* **Modular and extensible system design**

---


##  Disclaimer

This system provides **contract understanding and risk awareness only**.
It does **not** provide legal advice and should not replace professional legal consultation.


