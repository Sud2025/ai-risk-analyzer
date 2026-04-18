def analyze_risk(text):
    text = text.lower()

    # Base risk scores
    risk_scores = {
        "Privacy": 0,
        "Misuse": 0,
        "Bias": 0,
        "Hallucination": 0
    }

    # --- Base Rules ---
    if "personal data" in text:
        risk_scores["Privacy"] += 3

    if "fake news" in text or "misinformation" in text:
        risk_scores["Misuse"] += 3

    if "bias" in text or "discrimination" in text:
        risk_scores["Bias"] += 2

    if "hallucinate" in text or "make up facts" in text:
        risk_scores["Hallucination"] += 2

    # --- Context Detection ---
    context_multiplier = 1.0

    if "healthcare" in text or "medical" in text:
        context_multiplier = 1.5

    elif "finance" in text or "banking" in text:
        context_multiplier = 1.5

    # --- Intent Detection ---
    intent_multiplier = 1.0

    if "generate" in text and ("fake news" in text or "misinformation" in text):
        intent_multiplier = 1.5

    if "exploit" in text or "manipulate" in text:
        intent_multiplier = 1.5

    # --- Final Score Calculation ---
    base_score = sum(risk_scores.values())
    final_score = int(base_score * context_multiplier * intent_multiplier)

    # --- Risk Level ---
    if final_score == 0:
        level = "Low"
    elif final_score <= 3:
        level = "Medium"
    else:
        level = "High"

    triggered_risks = [k for k, v in risk_scores.items() if v > 0]

    return {
        "level": level,
        "score": final_score,
        "base_score": base_score,
        "types": triggered_risks,
        "context_multiplier": context_multiplier,
        "intent_multiplier": intent_multiplier
    }
