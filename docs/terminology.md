# Password Security Fundamentals

**Authentication:** establishing that a user is who they claim to be.

**Authorization:** determining what an authenticated identity may access.

**Password hash:** a one-way verification representation used instead of plaintext storage.

**Salt:** unique random data used with a password before hashing.

**Key stretching / password hashing:** deliberately expensive password-processing approaches designed to make large-scale guessing more costly.

**MFA:** authentication using more than one factor.

**Passphrase:** a longer password-like secret, ideally composed of randomly selected words rather than a famous quotation or predictable sentence.

**Password reuse:** using the same secret across multiple services.

**Credential stuffing:** automated attempts to use credentials exposed from one service against other services; this is why unique passwords matter.

**Plaintext vs hash:** plaintext can directly reveal the secret; a properly designed password hash is intended for verification without storing the original secret.
