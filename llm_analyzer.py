# llm_analyzer.py

SYSTEM_PROMPT = """
You are a contract risk analysis assistant for Indian SMEs.
You do NOT provide legal advice.
You explain business risks in simple language.
"""

USE_LIVE_AI = False  # keep FALSE for hackathon demo


def analyze_clause(clause: dict) -> dict:
    text = clause["text"].lower()
    title = clause["title"].lower()

    # Defaults
    risk_level = "Low"
    risk_type = "Operational"
    favors = "Neutral"
    explanation = ""
    reason = ""
    alternative = ""

    # TERMINATION
    if "termination" in title or "terminate" in text:
        risk_level = "High"
        risk_type = "Legal"
        favors = "Counterparty"
        explanation = (
            "This clause explains how the contract can be terminated. "
            "Unfavorable termination terms can abruptly disrupt business operations."
        )
        reason = (
            "Termination without adequate notice or safeguards may expose SMEs "
            "to sudden financial or operational loss."
        )
        alternative = (
            "Consider adding a reasonable notice period and limiting unilateral termination rights."
        )

    # PAYMENT
    elif "payment" in title or "pay" in text:
        risk_level = "Medium"
        risk_type = "Financial"
        explanation = (
            "This clause governs how and when payments are made. "
            "Delayed payments can strain SME cash flow."
        )
        reason = "Extended payment timelines increase working capital pressure."
        alternative = "Specify clear payment timelines and penalties for late payment."

    # LIABILITY / INDEMNITY
    elif "liability" in title or "indemnity" in text:
        risk_level = "High"
        risk_type = "Financial"
        favors = "Counterparty"
        explanation = (
            "This clause determines financial responsibility in case of losses or damages. "
            "Unlimited liability can expose SMEs to severe financial risk."
        )
        reason = "No liability cap may exceed the SME’s financial capacity."
        alternative = "Consider capping liability to the contract value."

    # CONFIDENTIALITY
    elif "confidential" in title:
        risk_level = "Medium"
        risk_type = "Compliance"
        explanation = (
            "This clause restricts how sensitive information is shared. "
            "Overly broad confidentiality obligations may be hard to comply with."
        )
        reason = "Ambiguous scope increases compliance risk."
        alternative = "Clearly define what qualifies as confidential information."

    # JURISDICTION / GOVERNING LAW
    elif "jurisdiction" in title or "governing law" in text:
        risk_level = "Medium"
        risk_type = "Legal"
        explanation = (
            "This clause determines where disputes will be resolved. "
            "Foreign jurisdictions can increase legal cost and complexity."
        )
        reason = "Disputes outside India may be expensive for SMEs."
        alternative = "Prefer Indian jurisdiction where possible."

    # GENERAL
    else:
        explanation = (
            "This clause outlines general contractual obligations. "
            "While it may not be immediately risky, it should still be reviewed."
        )
        reason = "General clauses can interact with other terms in unexpected ways."
        alternative = "Ensure consistency with related clauses."

    return {
        "plain_language_explanation": explanation,
        "risk_level": risk_level,
        "risk_type": risk_type,
        "favors": favors,
        "risk_reason": reason,
        "safer_alternative": alternative
    }
