import unittest
from reverse_engineering import disassemble_binary, analyze_executable
from utils.reverse_engineering_utils import is_executable_format

class TestReverseEngineering(unittest.TestCase):

    def setUp(self):
        # Setup code for the tests, like creating test files or inputs
        self.test_executable_path = "test_data/test_executable.bin"
        self.test_non_executable_path = "test_data/test_file.txt"

    def test_disassemble_binary_executable(self):
        # Test disassembling a binary executable
        result = disassemble_binary(self.test_executable_path)
        self.assertIsNotNone(result, "Disassembling binary should not return None")
        self.assertIsInstance(result, str, "Disassembling binary should return a string")

    def test_disassemble_binary_non_executable(self):
        # Test disassembling a non-executable file
        with self.assertRaises(ValueError):
            disassemble_binary(self.test_non_executable_path)

    def test_analyze_executable_executable(self):
        # Test analyzing an executable file
        result = analyze_executable(self.test_executable_path)
        self.assertIsNotNone(result, "Analyzing executable should not return None")
        self.assertIsInstance(result, dict, "Analyzing executable should return a dictionary")

    def test_analyze_executable_non_executable(self):
        # Test analyzing a non-executable file
        with self.assertRaises(ValueError):
            analyze_executable(self.test_non_executable_path)

    def test_is_executable_format(self):
        # Test if the file format is recognized as executable
        self.assertTrue(is_executable_format(self.test_executable_path), "File should be recognized as an executable format")
        self.assertFalse(is_executable_format(self.test_non_executable_path), "File should not be recognized as an executable format")

    def tearDown(self):
        # Tear down code for the tests, like deleting test files or cleaning up resources
        pass

if __name__ == '__main__':
    unittest.main()