# test_codex

This folder contains a small email validation utility and tests.

## Validation logic

The `validate_email` function applies a pragmatic set of checks that match common email formats while staying readable and testable:

1. **Exactly one `@` symbol** to separate the local and domain parts.
2. **Non-empty local and domain parts** to ensure something exists on each side.
3. **Local part character whitelist** using a regex that allows common RFC 5322 characters (letters, digits, and `.!#$%&'*+/=?^_`{|}~-`) and disallows spaces.
4. **Domain structure** requires at least one dot (`.`) so that `example.com` is valid but `example` is not.
5. **Domain labels** are validated to start and end with an alphanumeric character and only allow internal hyphens, preventing labels like `-domain` or `domain-`.
6. **Top-level domain length** must be at least two characters to avoid single-letter TLDs such as `.c`.

These checks intentionally avoid the full complexity of RFC 5322 (which allows many edge cases) in favor of a practical validation rule set suited to common applications.

## Running the tests

From this directory:

```bash
python -m unittest test_email_validator.py
```
