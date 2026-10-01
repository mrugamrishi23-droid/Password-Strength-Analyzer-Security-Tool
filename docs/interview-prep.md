# Interview Preparation — Exactly 10 Questions and Answers

## 1. Explain your project.
**Answer:** I built a defensive Password Strength Analyzer and Security Suggestion Tool using Python Flask, HTML, CSS, JavaScript and SQLite. A user enters a synthetic or demo password, and the application analyzes it in memory for length, character diversity, common-password usage, sequences, keyboard patterns, repetition, predictable structures and optional personal-context overlap. It combines those signals into a project-defined 0–100 score and classification, then gives specific recommendations. I deliberately designed it so the submitted password is not logged or stored in the analytics database.

## 2. How do you measure password strength?
**Answer:** I do not rely only on uppercase, lowercase, numbers and symbols. I combine length, character diversity, unique-character ratio, common-password status and pattern resistance. I also apply penalties for sequences, keyboard patterns, repetition, predictable word-plus-number structures and optional personal-context overlap. The final score is a project-defined heuristic rather than a universal standard.

## 3. What is password entropy?
**Answer:** Entropy is a way to describe uncertainty in a password. My educational estimate uses `L × log2(N)`, where L is length and N is the estimated character pool. The limitation is important: the formula assumes random character selection. Human-created passwords can be much more predictable, so I never use entropy alone.

## 4. Why did you implement pattern detection?
**Answer:** Human users often create predictable structures such as `1234`, `qwerty`, repeated characters or a common word followed by a year. Pattern detection catches weaknesses that simple character-composition rules can miss.

## 5. What is password hashing and why is salting important?
**Answer:** Password hashing transforms a password into a value intended for one-way verification rather than reversible storage. A salt is unique random data combined with the password before hashing so identical passwords do not produce identical stored hashes. Modern password-hashing choices include Argon2id, bcrypt, scrypt and PBKDF2. My separate educational demo uses scrypt through a password-hashing library and a synthetic password.

## 6. What is the difference between a password policy and a strength score?
**Answer:** A policy is a rule that can be checked consistently, such as a minimum length or rejecting common passwords. A strength score is an assessment of several signals. A password can pass a policy and still be predictable, so I keep the two results separate in the application.

## 7. How did you protect user privacy?
**Answer:** The analyzer processes the submitted password only during the request. I do not create a password database column, do not log the password, do not return it in the API response, do not put it in a URL, and do not persist it in localStorage or sessionStorage. The analytics database stores only safe metadata such as score, classification, length, weakness count and timestamps.

## 8. Why is MFA important if a password is strong?
**Answer:** A strong password reduces some guessing risk, but it does not eliminate phishing, session theft, credential reuse or other account threats. MFA adds another authentication factor, so I present it as an additional security control rather than a replacement for password hygiene.

## 9. What secure-coding practices did you apply?
**Answer:** I used input validation, bounded request size, transient password processing, no sensitive logging, parameterized SQLite queries, a password input field, `secrets` for security-sensitive random generation, a small dependency footprint and automated tests. For production deployment I would also require HTTPS, rate limiting, secure headers, stronger operational logging controls and a mature password-strength library.

## 10. What are the main limitations of your project?
**Answer:** The score and classification are project-defined, not universal standards. The common-password list is intentionally small and educational. The entropy estimate assumes randomness and cannot provide a guaranteed attacker time. A production system would need mature strength-estimation and breach-checking controls, configurable enterprise policies and integration with established identity systems.
