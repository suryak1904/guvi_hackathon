# risk_engine.py

HEATMAP_WEIGHTS = {
    "Low": 1,      # 🟢 green
    "Medium": 3,   # 🟡 yellow
    "High": 6      # 🔴 red
}


def calculate_overall_risk(analysis_results):
    total_score = 0

    for clause in analysis_results:
        total_score += HEATMAP_WEIGHTS.get(clause["risk_level"], 1)

    max_score = len(analysis_results) * HEATMAP_WEIGHTS["High"]
    risk_percentage = int((total_score / max_score) * 100)

    if risk_percentage < 35:
        label = "Low Risk"
    elif risk_percentage < 65:
        label = "Medium Risk"
    else:
        label = "High Risk"

    return risk_percentage, label
