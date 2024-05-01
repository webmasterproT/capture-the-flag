import unittest
from unittest.mock import patch
from dynamic_code_exec import execute_dynamic_code

class TestDynamicCodeExec(unittest.TestCase):
    def test_execute_dynamic_code_valid_code(self):
        # Test executing valid dynamic code
        dynamic_code = "x = 5"
        expected_result = {'x': 5}
        result = execute_dynamic_code(dynamic_code)
        self.assertEqual(result, expected_result)

    def test_execute_dynamic_code_invalid_code(self):
        # Test executing invalid dynamic code
        dynamic_code = "x ="
        with self.assertRaises(SyntaxError):
            execute_dynamic_code(dynamic_code)

    def test_execute_dynamic_code_with_return_value(self):
        # Test executing dynamic code with a return value
        dynamic_code = "def test_func(): return 'test_passed'"
        execute_dynamic_code(dynamic_code)
        result = test_func()
        self.assertEqual(result, 'test_passed')

    def test_execute_dynamic_code_with_external_dependency(self):
        # Test executing dynamic code that depends on an external function
        dynamic_code = "result = external_function()"
        with patch('dynamic_code_exec.external_function', return_value='mocked_result'):
            result = execute_dynamic_code(dynamic_code)
            self.assertEqual(result['result'], 'mocked_result')

    def test_execute_dynamic_code_security(self):
        # Test executing dynamic code with potential security issues
        dynamic_code = "import os; os.system('echo insecure')"
        with self.assertRaises(Exception):
            execute_dynamic_code(dynamic_code)

    def test_execute_dynamic_code_resource_limit(self):
        # Test executing dynamic code with resource limits (e.g., time limit)
        dynamic_code = "while True: pass"
        with self.assertRaises(TimeoutError):
            execute_dynamic_code(dynamic_code, timeout=1)

    def test_execute_dynamic_code_with_context(self):
        # Test executing dynamic code with a predefined context
        dynamic_code = "result = a + b"
        context = {'a': 2, 'b': 3}
        expected_result = {'result': 5}
        result = execute_dynamic_code(dynamic_code, context=context)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()