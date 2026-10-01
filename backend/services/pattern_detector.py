import re

KEYBOARD_PATTERNS = ["qwerty", "asdf", "zxcv", "qwerty123", "123qwe", "asdfgh", "qaz", "wsx"]
COMMON_SEQUENCES = ["0123", "1234", "2345", "3456", "4567", "5678", "6789", "9876", "8765", "7654", "6543", "5432", "4321", "3210"]
LETTER_SEQUENCES = ["abcd", "bcde", "cdef", "defg", "efgh", "fghi", "ghij", "hijk", "dcba", "cbaz", "zyxw", "wvut", "tsrq", "rqpo"]


def detect_sequences(password: str):
    p = password.lower()
    found = []
    for seq in COMMON_SEQUENCES + LETTER_SEQUENCES:
        if seq in p and seq not in found:
            found.append(seq)
    # Generic monotonic runs of 4+ ASCII letters/digits.
    for i in range(len(p) - 3):
        chunk = p[i:i+4]
        if len(set(chunk)) == 4:
            vals = [ord(c) for c in chunk]
            if all(vals[j+1] - vals[j] == 1 for j in range(3)) or all(vals[j] - vals[j+1] == 1 for j in range(3)):
                if chunk not in found:
                    found.append(chunk)
    return found


def detect_keyboard_patterns(password: str):
    p = password.lower()
    return [x for x in KEYBOARD_PATTERNS if x in p]


def detect_repetition(password: str):
    repeated_chars = sorted(set(re.findall(r"(.)\1{2,}", password)))
    repeated_substrings = []
    for size in range(2, min(6, len(password) // 2 + 1)):
        for i in range(len(password) - 2 * size + 1):
            part = password[i:i+size]
            if part * 2 in password and part not in repeated_substrings:
                repeated_substrings.append(part)
    return {"repeated_characters": repeated_chars, "repeated_substrings": repeated_substrings}


def detect_predictable_structure(password: str):
    p = password.lower()
    findings = []
    common_words = ["password", "welcome", "admin", "hello", "letmein", "qwerty", "user", "login"]
    if any(word in p for word in common_words):
        findings.append("Common word used")
    if re.search(r"(?:19|20)\d{2}", p):
        findings.append("Year-like pattern detected")
    if re.search(r"[a-zA-Z]+(?:123|1234|12|321|2020|2021|2022|2023|2024|2025|2026)$", p):
        findings.append("Predictable word-plus-number structure")
    if re.search(r"^[A-Za-z]+\d+$", password):
        findings.append("Word followed only by numbers")
    return findings
