# Security Verification Checklist

- [ ] No plaintext password column exists in SQLite.
- [ ] Submitted password is not logged.
- [ ] Submitted password is not returned by `/api/analyze`.
- [ ] Submitted password is not placed in URL parameters.
- [ ] Password field defaults to hidden.
- [ ] Frontend does not use localStorage/sessionStorage for passwords.
- [ ] Optional context is compared locally and not persisted.
- [ ] Generated passwords are not stored.
- [ ] Analytics stores only metadata and finding descriptions.
- [ ] Test screenshots use synthetic passwords only.
- [ ] Production deployment uses HTTPS.
- [ ] Production API uses rate limiting.
