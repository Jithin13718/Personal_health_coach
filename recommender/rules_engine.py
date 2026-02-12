def generate_rule_based_recommendations(metrics: dict) -> list:
    """
    Input: normalized metrics dict
    Output: list of recommendation strings
    """

    recs = []

    steps = metrics.get("steps", 0)
    sleep = metrics.get("sleep_hours", 0)
    protein = metrics.get("protein", 0)

    if steps < 5000:
        recs.append("You’re a bit low on movement today. A 15–20 min walk would help.")

    if sleep and sleep < 7:
        recs.append("Try to get at least 7 hours of sleep for better recovery.")

    if protein and protein < 50:
        recs.append("Your protein intake seems low. Consider eggs, yogurt, or legumes.")

    return recs
