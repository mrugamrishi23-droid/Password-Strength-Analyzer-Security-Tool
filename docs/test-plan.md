# 30-Test Security and Functional Test Plan

Use synthetic/demo inputs only. `Actual Result` should be filled after running the application; automated tests cover core logic separately.

| ID | Scenario | Input | Expected Result | Actual Result | Pass/Fail |
|---:|---|---|---|---|---|
| 1 | Empty password | `""` | Score 0 or very weak; no exception | Run locally | — |
| 2 | One character | `A` | Very weak/short finding | Run locally | — |
| 3 | Short numeric | `1234` | Very weak; sequence/common finding | Run locally | — |
| 4 | Common password | `password` | Very weak; common-password finding | Run locally | — |
| 5 | Long repeated | `aaaaaaaaaaaaaaaa` | Weak; repetition finding | Run locally | — |
| 6 | Lowercase only | `syntheticpassword` | Limited diversity; length/predictability findings as applicable | Run locally | — |
| 7 | Uppercase only | `SYNTHETICPASSWORD` | Limited diversity | Run locally | — |
| 8 | Numbers only | `8492751630` | Limited diversity; possible sequence analysis | Run locally | — |
| 9 | Symbols only | `!@#$%^&*()` | Limited diversity/length finding | Run locally | — |
| 10 | Mixed characters | `V7!kP2#rL9@x` | Mixed-character metrics returned | Run locally | — |
| 11 | Sequential numbers | `123456` | Sequence finding | Run locally | — |
| 12 | Reverse numeric | `987654` | Reverse sequence finding | Run locally | — |
| 13 | Sequential letters | `abcdef` | Sequence finding | Run locally | — |
| 14 | Keyboard sequence | `qwerty` | Keyboard finding | Run locally | — |
| 15 | Repeated characters | `AAAA1111` | Repetition finding | Run locally | — |
| 16 | Repeated substring | `abcabcabc` | Repeated substring finding | Run locally | — |
| 17 | Common word + number | `welcome123` | Predictable structure finding | Run locally | — |
| 18 | Word + year | `admin2026` | Common word/year finding | Run locally | — |
| 19 | Personal name overlap | `Rahul@123` + name `Rahul` | Personal-information warning | Run locally | — |
| 20 | Birth year overlap | `Demo2000!` + year `2000` | Personal-information warning | Run locally | — |
| 21 | Long passphrase-like | `river-lantern-forest-demo` | Long-length contribution; no claim of randomness | Run locally | — |
| 22 | Unicode handling | `Demo密码123!` | Analyze without crashing | Run locally | — |
| 23 | Spaces | `demo phrase 123!` | Spaces handled as a character category | Run locally | — |
| 24 | Maximum supported length | 128-character synthetic string | Accepted | Run locally | — |
| 25 | Score boundaries | Synthetic values near 20/21/40/41/60/61/80/81 | Correct project-defined classification | Run locally | — |
| 26 | Suggestions | `qwerty2026!` | Specific suggestions returned | Run locally | — |
| 27 | Secure generation | length 20 | Exactly 20 characters; generated transiently | Run locally | — |
| 28 | Password not stored | Any synthetic input | No password column/value in DB | Inspect SQLite | — |
| 29 | Password not logged | Any synthetic input | Password absent from app logs | Inspect logs | — |
| 30 | Analytics storage | Multiple synthetic analyses | Only metadata/findings stored; no password field | Inspect SQLite schema | — |

## Automated Core Tests
Run:

```powershell
pytest -q
```

Current project test suite covers common-password detection, repetition, keyboard patterns, context overlap, entropy estimation, generator length and a high-score synthetic example.
