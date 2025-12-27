# app.py

import streamlit as st
import pandas as pd
from collections import Counter

from extraction.extractor import extract_and_split
from llm_analyzer import analyze_clause
from risk_engine import calculate_overall_risk

st.set_page_config(page_title="Contract Risk Analyzer", layout="wide")
st.title("GenAI Contract Risk Analyzer for Indian SMEs")

uploaded_file = st.file_uploader(
    "Upload Contract (PDF, DOCX, TXT)",
    type=["pdf", "docx", "txt"]
)

if uploaded_file:
    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())

    file_type = uploaded_file.name.split(".")[-1]

    with st.spinner("Analyzing contract..."):
        clauses = extract_and_split(uploaded_file.name, file_type)
        analysis_results = [analyze_clause(c) for c in clauses]

    # 🔢 Heatmap-driven risk score
    risk_score, risk_label = calculate_overall_risk(analysis_results)

    color = {
        "Low Risk": "green",
        "Medium Risk": "orange",
        "High Risk": "red"
    }[risk_label]

    st.markdown(
        f"<h2 style='color:{color}'>Overall Risk Score: {risk_score}% ({risk_label})</h2>",
        unsafe_allow_html=True
    )

    # Heatmap summary
    counts = Counter(a["risk_level"] for a in analysis_results)
    st.write(
        f"🟢 Low: {counts.get('Low',0)} | "
        f"🟡 Medium: {counts.get('Medium',0)} | "
        f"🔴 High: {counts.get('High',0)}"
    )

    st.divider()
    st.subheader("Clause Risk Heatmap")

    COLOR_MAP = {
        "Low": "#c8e6c9",
        "Medium": "#fff9c4",
        "High": "#ffcdd2d"
    }

    for clause, analysis in zip(clauses, analysis_results):
        bg = COLOR_MAP[analysis["risk_level"]]

        st.markdown(
            f"""
            <div style="
                background-color:{bg};
                padding:15px;
                border-radius:8px;
                margin-bottom:10px;
                border-left:6px solid black">
                <b>{clause['title']} ({analysis['risk_level']})</b><br><br>
                {analysis['plain_language_explanation']}
            </div>
            """,
            unsafe_allow_html=True
        )

        with st.expander("Why is this risky?"):
            st.write(analysis["risk_reason"])
            st.info(f"Suggested Mitigation: {analysis['safer_alternative']}")

    st.divider()
    st.subheader("📊 Risk Distribution")
    df = pd.DataFrame(analysis_results)
    st.bar_chart(df["risk_level"].value_counts())
