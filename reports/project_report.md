# Password Strength Analyzer & Security Suggestion Tool — Project Report

## Abstract
This project is a defensive cybersecurity application that evaluates password characteristics locally and provides security recommendations. It combines length, character diversity, common-password checks, sequence detection, keyboard-pattern detection, repetition detection, optional context overlap, and a theoretical entropy-style estimate. The application is designed around a privacy rule: submitted passwords are processed transiently and are never stored in analytics.

## Introduction
Passwords remain an important authentication factor. A password can satisfy composition rules and still be predictable. This project demonstrates a broader assessment approach that considers length, unpredictability, patterns, common-password usage, and context.

## Problem Statement
A simple rule such as “one uppercase, one number and one symbol” does not adequately describe password predictability. Users also need understandable feedback rather than only a numeric score.

## Objectives
- Analyze password characteristics locally.
- Detect common and predictable patterns.
- Explain entropy as a theoretical concept.
- Provide actionable security suggestions.
- Demonstrate privacy-aware analytics.
- Educate users about password managers and MFA.

## Password Security Background
Authentication establishes identity; authorization controls access. Passwords should not be stored as plaintext. Production systems should use a dedicated password-hashing approach with salts and an appropriate work factor. Examples include Argon2id, bcrypt, scrypt and PBKDF2. Fast general-purpose hashes are not the preferred design for password storage.

## Proposed System
The user enters a synthetic/demo password into a web interface. The backend analyzes it in memory and returns a score, classification, findings, metrics and suggestions. Only aggregate metadata is stored for the dashboard.

## Architecture
See `docs/architecture.md`.

## Feature Extraction
The analyzer measures length, character classes, unique character count and unique-character ratio.

## Pattern Detection
The tool detects common numeric/letter sequences, keyboard-like patterns, repeated characters, repeated substrings, common words, year-like patterns and word-plus-number structures.

## Entropy Concepts
The project calculates an educational estimate using `L × log2(N)`, where L is length and N is an estimated character pool. This is not a prediction of real attacker effort because human-created passwords are not uniformly random.

## Strength Scoring
The score is project-defined on a 0–100 scale. It combines length, diversity, uniqueness, pattern resistance and common-password status, then applies penalties for predictable structures. The classification bands are project-defined and are not universal security standards.

## Recommendation Engine
Suggestions are generated from detected weaknesses, such as short length, common passwords, keyboard patterns, repeated patterns, predictable numbers, personal-context overlap, password reuse and lack of MFA.

## Password Generator
The optional generator uses Python's `secrets` module rather than the general-purpose `random` module. Generated values are returned transiently and are not persisted.

## Policy Checker
Policy compliance is intentionally separate from strength scoring. The demo policy uses a 12-character minimum, rejects common passwords and warns about personal-context overlap.

## Secure Password Storage Concepts
A separate educational demonstration uses Werkzeug's scrypt-backed password hashing functions with a synthetic password. This is not integrated with the analyzer's analytics path.

## Privacy Design
There is no password column in the database. The API response also does not return the submitted password. The frontend uses a password input field and does not place passwords in URLs, localStorage or sessionStorage.

## Dashboard
The dashboard displays total analyses, average score, strength distribution and weakness frequency using aggregate metadata.

## Testing
Automated tests cover common passwords, repetition, keyboard patterns, context overlap, entropy estimation and secure generation. The recommended manual security checklist also verifies that plaintext passwords are not stored or logged.

## Limitations
- Pattern lists are intentionally small and educational.
- The score is a project-specific heuristic, not a universal standard.
- Entropy is theoretical and assumes randomness.
- The demo is not a replacement for enterprise identity controls or a mature password-strength library.
- A local educational common-password list is not equivalent to a full breach corpus.

## Future Scope
Configurable enterprise policies, privacy-preserving breach-corpus checks, password-manager concepts, IAM integration, SSO education, WebAuthn/passkey education, localization, accessibility, and privacy-preserving organization-level reporting.

## Conclusion
The project demonstrates defensive password-security analysis while making privacy a first-class design requirement. It shows how application security, secure coding, IAM concepts, testing and security awareness can be combined in a practical student project.
