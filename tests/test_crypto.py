import unittest
from crypto import encrypt_data, decrypt_data, solve_cipher
from utils.crypto_utils import validate_encryption_scheme, generate_random_key
from data.configurations import configuration_schema

class TestCrypto(unittest.TestCase):

    def setUp(self):
        # Setup configurations and test data
        self.test_data = "NationalSecurityData"
        self.encryption_scheme = configuration_schema['encryption_scheme']
        self.key = generate_random_key(self.encryption_scheme)

    def test_encrypt_data(self):
        # Test encryption functionality
        encrypted_data = encrypt_data(self.test_data, self.key, self.encryption_scheme)
        self.assertNotEqual(encrypted_data, self.test_data)
        self.assertTrue(validate_encryption_scheme(encrypted_data, self.encryption_scheme))

    def test_decrypt_data(self):
        # Test decryption functionality
        encrypted_data = encrypt_data(self.test_data, self.key, self.encryption_scheme)
        decrypted_data = decrypt_data(encrypted_data, self.key, self.encryption_scheme)
        self.assertEqual(decrypted_data, self.test_data)

    def test_solve_cipher(self):
        # Test cipher solving functionality
        cipher_text = "Vjku ku pqv vjg swguvkqp"
        solved_text = solve_cipher(cipher_text, 'Caesar', 2)  # Assuming a Caesar cipher with a shift of 2
        self.assertEqual(solved_text, "This is not the solution")

    def test_invalid_encryption_scheme(self):
        # Test handling of invalid encryption schemes
        with self.assertRaises(ValueError):
            encrypt_data(self.test_data, self.key, "InvalidScheme")

    def test_invalid_key(self):
        # Test handling of invalid key
        with self.assertRaises(ValueError):
            encrypt_data(self.test_data, "InvalidKey", self.encryption_scheme)

if __name__ == '__main__':
    unittest.main()