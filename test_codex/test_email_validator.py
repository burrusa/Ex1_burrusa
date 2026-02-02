import unittest

from email_validator import validate_email


class TestValidateEmail(unittest.TestCase):
    def test_valid_addresses(self):
        valid_addresses = [
            "user@example.com",
            "user.name+tag@example.co.uk",
            "user_name@example.io",
            "user-name@sub.domain.org",
            "user123@domain.dev",
        ]
        for address in valid_addresses:
            with self.subTest(address=address):
                self.assertTrue(validate_email(address))

    def test_invalid_addresses(self):
        invalid_addresses = [
            "plainaddress",
            "missing-at-sign.example.com",
            "@missinglocal.com",
            "missingdomain@",
            "double@@example.com",
            "space in@address.com",
            "user@domain",
            "user@.com",
            "user@domain..com",
            "user@domain.c",
            "user@-domain.com",
            "user@domain-.com",
        ]
        for address in invalid_addresses:
            with self.subTest(address=address):
                self.assertFalse(validate_email(address))


if __name__ == "__main__":
    unittest.main()
