import unittest
from utils.helpers import parse_data, validate_input
from utils.logging_utils import log_action, log_error, log_info
from utils.network_utils import analyze_traffic, detect_intrusion, monitor_network
from utils.forensic_utils import forensic_data_schema
from utils.crypto_utils import encrypt_data, decrypt_data, solve_cipher
from utils.osint_utils import gather_intelligence, search_social_media
from utils.reverse_engineering_utils import disassemble_binary, analyze_executable
from utils.steganography_utils import hide_message, reveal_message

class TestHelpers(unittest.TestCase):
    def test_parse_data(self):
        self.assertEqual(parse_data("test data"), "test data parsed")
        self.assertRaises(ValueError, parse_data, None)

    def test_validate_input(self):
        self.assertTrue(validate_input("valid input"))
        self.assertFalse(validate_input(""))

class TestLoggingUtils(unittest.TestCase):
    def test_log_action(self):
        self.assertIsNone(log_action("Action logged"))

    def test_log_error(self):
        self.assertIsNone(log_error("Error logged"))

    def test_log_info(self):
        self.assertIsNone(log_info("Info logged"))

class TestNetworkUtils(unittest.TestCase):
    def test_analyze_traffic(self):
        self.assertTrue(analyze_traffic("traffic data"))

    def test_detect_intrusion(self):
        self.assertTrue(detect_intrusion("intrusion data"))

    def test_monitor_network(self):
        self.assertTrue(monitor_network("network data"))

class TestForensicUtils(unittest.TestCase):
    def test_forensic_data_schema(self):
        self.assertIsInstance(forensic_data_schema, dict)

class TestCryptoUtils(unittest.TestCase):
    def test_encrypt_data(self):
        self.assertEqual(encrypt_data("data", "key"), "encrypted data")

    def test_decrypt_data(self):
        self.assertEqual(decrypt_data("encrypted data", "key"), "data")

    def test_solve_cipher(self):
        self.assertEqual(solve_cipher("cipher text"), "solved cipher")

class TestOsintUtils(unittest.TestCase):
    def test_gather_intelligence(self):
        self.assertTrue(gather_intelligence("target"))

    def test_search_social_media(self):
        self.assertTrue(search_social_media("username"))

class TestReverseEngineeringUtils(unittest.TestCase):
    def test_disassemble_binary(self):
        self.assertTrue(disassemble_binary("binary data"))

    def test_analyze_executable(self):
        self.assertTrue(analyze_executable("executable data"))

class TestSteganographyUtils(unittest.TestCase):
    def test_hide_message(self):
        self.assertEqual(hide_message("message", "cover medium"), "stego object")

    def test_reveal_message(self):
        self.assertEqual(reveal_message("stego object"), "hidden message")

if __name__ == '__main__':
    unittest.main()