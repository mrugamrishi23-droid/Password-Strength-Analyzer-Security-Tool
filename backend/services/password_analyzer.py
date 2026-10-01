import re
from pathlib import Path
from .pattern_detector import detect_sequences, detect_keyboard_patterns, detect_repetition, detect_predictable_structure
from .entropy_estimator import estimate_theoretical_entropy
from .scoring_engine import calculate_score, classify
from .suggestion_engine import generate_suggestions

COMMON_FILE = Path(__file__).resolve().parents[2] / "data" / "common_passwords.txt"


def load_common_passwords():
    try:
        return {line.strip().lower() for line in COMMON_FILE.read_text(encoding="utf-8").splitlines() if line.strip() and not line.startswith("#")}
    except OSError:
        return set()


def is_common_password(password: str) -> bool:
    return password.casefold() in load_common_passwords()


def analyze_length(password: str):
    n = len(password)
    band = "Very short" if n < 8 else "Short" if n < 12 else "Better length" if n < 16 else "Strong length contribution"
    return {"length": n, "band": band}


def analyze_password(password: str, context=None):
    if not isinstance(password, str):
        raise ValueError("Password must be text.")
    if len(password) > 128:
        raise ValueError("Password exceeds the supported 128-character analysis limit.")
    context = context or {}
    lower = any(c.islower() for c in password)
    upper = any(c.isupper() for c in password)
    digit = any(c.isdigit() for c in password)
    symbol = any(not c.isalnum() and not c.isspace() for c in password)
    space = any(c.isspace() for c in password)
    unique_ratio = len(set(password)) / len(password) if password else 0
    types = sum([lower, upper, digit, symbol, space])
    sequences = detect_sequences(password)
    keyboard = detect_keyboard_patterns(password)
    repetition = detect_repetition(password)
    predictable = detect_predictable_structure(password)
    common = is_common_password(password)
    overlap = []
    for key in ("first_name", "birth_year", "organization"):
        value = str(context.get(key, "")).strip()
        if value and len(value) >= 3 and value.casefold() in password.casefold():
            overlap.append(key)
    metrics = {
        "length": len(password), "lowercase": lower, "uppercase": upper, "digit": digit, "symbol": symbol,
        "space": space, "unique_character_count": len(set(password)), "character_type_count": types,
        "unique_character_ratio": round(unique_ratio, 3), "sequences": sequences, "keyboard_patterns": keyboard,
        "repetition": repetition, "is_common": common, "predictable_structure": predictable,
        "personal_info_overlap": overlap, "entropy": estimate_theoretical_entropy(password)
    }
    findings = []
    if len(password) < 8: findings.append({"type":"length", "severity":"high", "description":"Password is very short."})
    elif len(password) < 12: findings.append({"type":"length", "severity":"medium", "description":"Password is shorter than the project's 12-character policy target."})
    if common: findings.append({"type":"common_password", "severity":"critical", "description":"Password matches a commonly used password pattern."})
    if sequences: findings.append({"type":"sequence", "severity":"high", "description":"Predictable sequence detected."})
    if keyboard: findings.append({"type":"keyboard_pattern", "severity":"high", "description":"Predictable keyboard pattern detected."})
    if repetition["repeated_characters"] or repetition["repeated_substrings"]: findings.append({"type":"repetition", "severity":"high", "description":"Repeated character or substring pattern detected."})
    for item in predictable: findings.append({"type":"predictable_structure", "severity":"medium", "description":item})
    if overlap: findings.append({"type":"personal_information", "severity":"high", "description":"Password appears to contain voluntarily supplied personal or organization context."})
    score = calculate_score(metrics)
    return {"score": score, "classification": classify(score), "findings": findings,
            "suggestions": generate_suggestions(metrics), "metrics": metrics,
            "policy": {"minimum_length": 12, "common_password_check": not common, "personal_info_check": not bool(overlap),
                       "passes": len(password) >= 12 and not common and not overlap}}
