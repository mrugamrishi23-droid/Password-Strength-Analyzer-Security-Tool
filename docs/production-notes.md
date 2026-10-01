# Production Notes

This student project is a local educational prototype. Before production use, an engineering team should consider:

- HTTPS everywhere.
- Strict rate limiting and abuse controls.
- CSRF protection where applicable.
- Secure headers and content security policy.
- Mature password-strength estimation rather than a small heuristic.
- Privacy-preserving breached-password checks.
- Strong operational secrets management.
- Structured security logging that excludes credentials and sensitive input.
- Database access controls and backups.
- Monitoring and alerting.
- Accessibility and localization.
- Established IAM, SSO and MFA integration.
- Passkeys/WebAuthn education and migration paths.
