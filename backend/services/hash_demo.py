"""Separate educational hashing demonstration. Never use this to persist analyzer inputs."""
from werkzeug.security import generate_password_hash, check_password_hash


def hash_password(synthetic_password: str) -> str:
    return generate_password_hash(synthetic_password, method="scrypt")


def verify_password(synthetic_password: str, stored_hash: str) -> bool:
    return check_password_hash(stored_hash, synthetic_password)


if __name__ == "__main__":
    demo = "Synthetic-Demo-Password-Only!"
    hashed = hash_password(demo)
    print("Demo hash:", hashed)
    print("Verification:", verify_password(demo, hashed))
