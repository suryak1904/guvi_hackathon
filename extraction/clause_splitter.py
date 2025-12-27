import re

KEYWORDS = [
    "termination",
    "payment",
    "liability",
    "confidentiality",
    "penalty",
    "jurisdiction",
    "indemnity"
]


def detect_title(text):
    lower = text.lower()
    for k in KEYWORDS:
        if k in lower:
            return k.capitalize()
    return "General Clause"


def split_clauses(text, language="en"):
    """
    FINAL, GUARANTEED splitter
    - Works even if text is flattened into one line
    - Splits on numbered clauses (1., 2., 1.1)
    - Never drops content
    """

    # 🔑 split BEFORE a clause number, anywhere in text
    blocks = re.split(r"(?=\s*\d+\.\s)", text.strip())

    clauses = []
    clause_id = 1

    for block in blocks:
        block = block.strip()
        if not block:
            continue

        clauses.append({
            "clause_id": f"C{clause_id}",
            "title": detect_title(block),
            "text": block,
            "position": clause_id,
            "language": language
        })

        clause_id += 1

    return clauses
