def check_policy(password: str, common: bool, personal_overlap: bool, minimum_length=12):
    return {
        "minimum_length": minimum_length,
        "common_password_check": not common,
        "personal_info_check": not personal_overlap,
        "passes": len(password) >= minimum_length and not common and not personal_overlap,
    }
