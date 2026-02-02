"""Simple email validation utility."""

from __future__ import annotations

import re


LOCAL_PART_PATTERN = re.compile(r"^[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+$")
DOMAIN_LABEL_PATTERN = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?$")


def validate_email(address: str) -> bool:
    """Return True if the address matches a pragmatic email format.

    The validation enforces:
    - Exactly one '@' symbol.
    - Non-empty local and domain parts.
    - Local part uses common RFC 5322 characters (no spaces).
    - Domain has at least one dot and valid labels (letters/digits/hyphens).
    - Top-level domain is at least two characters long.
    """
    if address.count("@") != 1:
        return False

    local_part, domain_part = address.split("@")
    if not local_part or not domain_part:
        return False

    if not LOCAL_PART_PATTERN.match(local_part):
        return False

    domain_labels = domain_part.split(".")
    if len(domain_labels) < 2:
        return False

    if any(not label for label in domain_labels):
        return False

    if any(not DOMAIN_LABEL_PATTERN.match(label) for label in domain_labels):
        return False

    if len(domain_labels[-1]) < 2:
        return False

    return True
