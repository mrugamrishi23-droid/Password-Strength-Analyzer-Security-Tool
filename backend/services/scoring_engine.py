
def classify(score: int) -> str:
    if score <= 20: return "VERY WEAK"
    if score <= 40: return "WEAK"
    if score <= 60: return "MODERATE"
    if score <= 80: return "STRONG"
    return "VERY STRONG"


def calculate_score(metrics: dict) -> int:
    length = metrics["length"]
    length_points = min(35, max(0, (length - 4) * 3.0)) if length < 16 else 35
    diversity_points = min(15, metrics["character_type_count"] * 3.75)
    unique_points = min(10, metrics["unique_character_ratio"] * 10)
    pattern_points = 20
    pattern_points -= min(8, len(metrics["sequences"]) * 5)
    pattern_points -= min(7, len(metrics["keyboard_patterns"]) * 5)
    pattern_points -= min(8, len(metrics["repetition"]["repeated_characters"]) * 3)
    pattern_points -= min(8, len(metrics["repetition"]["repeated_substrings"]) * 4)
    pattern_points = max(0, pattern_points)
    common_points = 10 if not metrics["is_common"] else 0
    unpredictability = 10
    for key in ("predictable_structure", "personal_info_overlap"):
        if metrics[key]:
            unpredictability -= 5
    score = round(length_points + diversity_points + unique_points + pattern_points + common_points + max(0, unpredictability))
    penalties = 0
    if metrics["is_common"]: penalties += 55
    if metrics["sequences"]: penalties += 18
    if metrics["keyboard_patterns"]: penalties += 18
    if metrics["repetition"]["repeated_characters"] or metrics["repetition"]["repeated_substrings"]: penalties += 30
    if metrics["personal_info_overlap"]: penalties += 15
    if metrics["predictable_structure"]: penalties += 25
    return max(0, min(100, score - penalties))
