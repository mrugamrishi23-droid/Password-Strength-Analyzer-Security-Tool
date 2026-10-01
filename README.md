# Password Strength Analyzer & Security Suggestion Tool

Privacy-focused defensive cybersecurity project for evaluating password strength using length, predictability, common-password checks, pattern analysis, entropy concepts and security recommendations.

## Overview
The application analyzes passwords locally through a Flask API and provides a real-time web interface. The analyzer does **not** store plaintext passwords, log them, put them in URLs, or send them to external password-analysis services by default.

> **Important:** Use synthetic/demo passwords for screenshots and testing. This project is an educational analyzer, not a guarantee of password security.

## Problem Statement
Composition rules alone are insufficient. A value such as `Password123!` can contain uppercase letters, lowercase letters, digits and symbols while still following a predictable human pattern.

## Objectives
- Measure password length and character diversity.
- Detect common passwords and predictable patterns.
- Provide an entropy-style educational estimate.
- Produce actionable suggestions.
- Demonstrate privacy-safe aggregate analytics.
- Teach password managers, MFA, hashing and password policy concepts.

## Features
- 0–100 project-defined strength score.
- VERY WEAK / WEAK / MODERATE / STRONG / VERY STRONG classification.
- Length and character diversity analysis.
- Common-password detection.
- Numeric and alphabetic sequence detection.
- Keyboard-pattern detection.
- Repeated-character and repeated-substring detection.
- Predictable word + number/year detection.
- Optional local personal-context overlap check.
- Theoretical entropy-style estimate.
- Specific security recommendations.
- Show/hide password field.
- `secrets`-based password generator.
- Policy pass/fail separate from strength score.
- Metadata-only SQLite dashboard.
- Automated tests.
- Separate synthetic-password hashing demonstration.

## Architecture
`docs/architecture.md` contains the architecture diagram.

## Technology Stack
- Python 3.11+
- Flask
- SQLite
- HTML/CSS/JavaScript
- pytest

The project intentionally keeps dependencies small for a beginner-friendly implementation.

## Project Structure
```text
Password-Strength-Analyzer-Security-Tool/
├── backend/
│   ├── app.py
│   ├── services/
│   │   ├── password_analyzer.py
│   │   ├── pattern_detector.py
│   │   ├── entropy_estimator.py
│   │   ├── scoring_engine.py
│   │   ├── suggestion_engine.py
│   │   ├── password_generator.py
│   │   ├── policy_checker.py
│   │   └── hash_demo.py
├── frontend/
│   ├── index.html
│   ├── css/style.css
│   └── js/app.js
├── data/common_passwords.txt
├── tests/test_analyzer.py
├── docs/architecture.md
├── reports/project_report.md
├── requirements.txt
├── .env.example
└── .gitignore
```

## Installation — Windows PowerShell
```powershell
cd Password-Strength-Analyzer-Security-Tool
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If `py` is not available, use the Python command installed on your machine:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

## Run
```powershell
cd backend
python app.py
```
Open `http://127.0.0.1:5000` in your browser.

## Test
From the project root:
```powershell
pytest -q
```

## Safe Demo Cases
Use only synthetic examples:
- `123456` → expected VERY WEAK.
- `Password123!` → expected weak/moderate depending on calibration; predictable common word + numbers.
- `aaaaaaaaaaaaaaaa` → expected weak; long but repetitive.
- `qwerty2026!` → expected weak; keyboard pattern + year.
- Generate a fresh 20-character synthetic password at runtime → typically strong/very strong.

Do not reuse examples from documentation as real passwords.

## API
### POST `/api/analyze`
Request:
```json
{"password":"<processed transiently>","context":{"first_name":"Demo","birth_year":"2000","organization":"Example"}}
```
Response contains only analysis results; it does not return the submitted password.

### GET `/api/dashboard/stats`
Returns aggregate counts, average score and length distribution.

### GET `/api/analytics/weaknesses`
Returns aggregate weakness frequencies.

### POST `/api/generate-password`
Generates a transient random password using `secrets`.

## Privacy Design
- No plaintext-password database column.
- No password logging.
- No password in URLs.
- No password in API response.
- No localStorage/sessionStorage use for passwords.
- Context fields are compared in memory and are not persisted.
- Analytics contains only safe aggregate metadata.

## Security Concepts Demonstrated
### Plaintext vs hash
Production authentication systems should not store plaintext passwords. Password hashing is one-way verification, while encryption is designed for reversible confidentiality. Modern password hashing examples include Argon2id, bcrypt, scrypt and PBKDF2.

### Entropy
The formula `L × log2(N)` is an educational theoretical estimate. It assumes random selection. Human-created passwords can be substantially more predictable.

### Real-world authentication
Password security is only one layer. Strong authentication also benefits from MFA, rate limiting, secure password hashing, abuse protection, session security, phishing protection and monitoring.

## Security Testing Checklist
Verify that:
1. Passwords are not stored.
2. Passwords do not appear in logs.
3. Passwords do not appear in the database.
4. Passwords are not returned by the API.
5. Passwords are not placed in URL parameters.
6. The frontend uses `type=password` by default.
7. Frontend does not persist passwords.
8. localStorage contains no password.
9. sessionStorage contains no password.
10. Analytics contains metadata only.

## Industry Relevance
This project demonstrates practical concepts for cybersecurity analyst, application security analyst, IAM analyst, security engineer, SOC analyst and secure software developer roles: input validation, privacy-by-design, API security, defensive detection, secure randomness, authentication concepts, testing and security awareness.

## Limitations
The scoring model is a project-defined heuristic, not a universal security standard. A small educational common-password list cannot represent all breached or commonly used passwords. Entropy estimates are not exact attacker timelines.

## Future Improvements
- Mature password-strength estimation library integration.
- Configurable enterprise password policies.
- Privacy-preserving breach-corpus checks.
- Password-manager integration concepts.
- IAM/SSO integration.
- Passkey/WebAuthn education.
- Accessibility and localization.
- Organization-level aggregate reporting.

## Security Disclaimer
This is a defensive educational project. It does not crack passwords, attempt authentication against accounts, collect credentials, or transmit submitted passwords to external services by default.

## GitHub
Repository name: `Password-Strength-Analyzer-Security-Tool`

Suggested topics: `cybersecurity`, `password-security`, `password-strength`, `application-security`, `python`, `flask`, `secure-coding`, `iam`, `security-awareness`, `defensive-security`.
