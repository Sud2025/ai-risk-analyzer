def analyze_risk(text):
    text = text.lower()

    risk_scores = {
        "Privacy": 0,
        "Misuse": 0,
        "Bias": 0,
        "Hallucination": 0
    }

    # Rules
    if "personal data" in text:
        risk_scores["Privacy"] += 3

    if "fake news" in text or "misinformation" in text:
        risk_scores["Misuse"] += 3

    if "bias" in text or "discrimination" in text:
        risk_scores["Bias"] += 2

    if "hallucinate" in text or "make up facts" in text:
        risk_scores["Hallucination"] += 2

    # Calculate total score
    total_score = sum(risk_scores.values())

    # Determine level
    if total_score == 0:
        level = "Low"
    elif total_score <= 3:
        level = "Medium"
    else:
        level = "High"

    # Filter only triggered risks
    triggered_risks = [k for k, v in risk_scores.items() if v > 0]

    return {
        "level": level,
        "score": total_score,
        "types": triggered_risks
    }
