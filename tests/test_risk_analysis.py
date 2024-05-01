import unittest
from risk_analysis import analyze_risk, calculate_risk_score
from utils.helpers import parse_data, validate_input

class TestRiskAnalysis(unittest.TestCase):

    def setUp(self):
        # Setup can include loading test data, configurations, etc.
        self.test_data = {
            'threat_level': 'high',
            'vulnerabilities': ['SQLi', 'XSS', 'RCE'],
            'impact': 'critical'
        }
        self.expected_risk_score = 95  # Example risk score based on test data

    def test_analyze_risk(self):
        # Test the analyze_risk function with predefined test data
        risk_analysis_result = analyze_risk(self.test_data)
        self.assertIsNotNone(risk_analysis_result)
        self.assertIn('risk_score', risk_analysis_result)
        self.assertIn('recommendations', risk_analysis_result)

    def test_calculate_risk_score(self):
        # Test the calculate_risk_score function with predefined test data
        risk_score = calculate_risk_score(self.test_data['threat_level'], self.test_data['vulnerabilities'], self.test_data['impact'])
        self.assertEqual(risk_score, self.expected_risk_score)

    def test_parse_data(self):
        # Test the parse_data utility function
        parsed_data = parse_data(self.test_data)
        self.assertEqual(parsed_data, self.test_data)

    def test_validate_input(self):
        # Test the validate_input utility function
        is_valid = validate_input(self.test_data)
        self.assertTrue(is_valid)

    def test_invalid_data(self):
        # Test analyze_risk with invalid data to ensure it handles errors
        with self.assertRaises(ValueError):
            analyze_risk({'invalid': 'data'})

    def test_risk_score_bounds(self):
        # Ensure that risk score is within acceptable bounds (0-100)
        risk_score = calculate_risk_score(self.test_data['threat_level'], self.test_data['vulnerabilities'], self.test_data['impact'])
        self.assertGreaterEqual(risk_score, 0)
        self.assertLessEqual(risk_score, 100)

if __name__ == '__main__':
    unittest.main()