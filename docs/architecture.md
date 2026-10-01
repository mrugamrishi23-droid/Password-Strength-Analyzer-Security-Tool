# System Architecture

```text
User
  |
  v
Secure Web Interface
  |
  v
Password Input (transient)
  |
  v
In-Memory Analysis
  +--> Length Analyzer
  +--> Character Analyzer
  +--> Common Password Checker
  +--> Sequence Detector
  +--> Keyboard Pattern Detector
  +--> Repetition Detector
  +--> Context Checker
  +--> Entropy Estimator
  |
  v
Strength Scoring Engine
  |
  +--> Classification
  +--> Suggestion Engine
  |
  v
User Feedback

Optional safe metadata only
  |
  v
SQLite Analytics
  |
  v
Aggregate Dashboard
```

The password itself has no database column and is not included in analytics records.
