import math
import string


def estimate_theoretical_entropy(password: str) -> dict:
    pool = 0
    if any(c in string.ascii_lowercase for c in password): pool += 26
    if any(c in string.ascii_uppercase for c in password): pool += 26
    if any(c in string.digits for c in password): pool += 10
    if any(c in string.punctuation for c in password): pool += len(string.punctuation)
    if any(c.isspace() for c in password): pool += 1
    if pool == 0 or not password:
        bits = 0.0
    else:
        bits = len(password) * math.log2(pool)
    return {"estimated_bits": round(bits, 2), "estimated_character_pool": pool,
            "explanation": "Educational theoretical estimate; it assumes random character selection and does not model human predictability."}
