def analyze_risk(text):
    risk_types = []

    if "personal data" in text.lower():
        risk_types.append("Privacy")

    if "fake news" in text.lower():
        risk_types.append("Misuse")

    if "bias" in text.lower():
        risk_types.append("Bias")

    if len(risk_types) == 0:
        level = "Low"
    elif len(risk_types) == 1:
        level = "Medium"
    else:
        level = "High"

    return {
        "level": level,
        "types": risk_types
    }
