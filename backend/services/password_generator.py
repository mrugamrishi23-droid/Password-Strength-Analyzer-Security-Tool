import secrets
import string


def generate_password(length=20, uppercase=True, lowercase=True, numbers=True, symbols=True):
    if not 16 <= length <= 128:
        raise ValueError("Length must be between 16 and 128.")
    groups = []
    if uppercase: groups.append(string.ascii_uppercase)
    if lowercase: groups.append(string.ascii_lowercase)
    if numbers: groups.append(string.digits)
    if symbols: groups.append(string.punctuation)
    if not groups:
        raise ValueError("Select at least one character type.")
    chars = [secrets.choice(group) for group in groups]
    alphabet = ''.join(groups)
    chars.extend(secrets.choice(alphabet) for _ in range(length - len(chars)))
    secrets.SystemRandom().shuffle(chars)
    return ''.join(chars)
