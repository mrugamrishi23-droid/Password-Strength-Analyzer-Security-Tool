def generate_suggestions(metrics: dict):
    suggestions = []
    if metrics["length"] < 12:
        suggestions.append("Consider using a longer password or passphrase (12+ characters is a useful project policy target).")
    if metrics["is_common"]:
        suggestions.append("Do not use a commonly used password pattern.")
    if metrics["sequences"]:
        suggestions.append("Your password contains a predictable numeric or letter sequence.")
    if metrics["keyboard_patterns"]:
        suggestions.append("Avoid predictable keyboard sequences such as qwerty or asdf.")
    if metrics["repetition"]["repeated_characters"] or metrics["repetition"]["repeated_substrings"]:
        suggestions.append("Reduce repeated characters or repeated substrings to improve unpredictability.")
    if metrics["predictable_structure"]:
        suggestions.append("Avoid common words followed by predictable numbers or years.")
    if metrics["personal_info_overlap"]:
        suggestions.append("Avoid including your name, birth year, or organization-related information.")
    if metrics["character_type_count"] < 3:
        suggestions.append("Use a broader character mix when it does not make the password harder to manage.")
    suggestions.extend(["Use a password manager to generate and store unique passwords.", "Enable MFA where available.", "Never reuse passwords across important accounts."])
    return list(dict.fromkeys(suggestions))
