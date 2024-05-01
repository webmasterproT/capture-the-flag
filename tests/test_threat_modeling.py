import unittest
from threat_modeling import model_threat, assess_risk
from utils.helpers import validate_input

class TestThreatModeling(unittest.TestCase):

    def setUp(self):
        # Setup can include initializing API keys, setting up test data, etc.
        self.valid_threat_data = {
            "asset": "Critical Infrastructure",
            "threat_actor": "Nation State",
            "vulnerability": "Unpatched Software",
            "likelihood": 0.7,
            "impact": 0.9
        }
        self.invalid_threat_data = {
            "asset": "",
            "threat_actor": "Script Kiddie",
            "vulnerability": "Social Engineering",
            "likelihood": 1.2,  # Invalid likelihood value
            "impact": -0.1  # Invalid impact value
        }

    def test_model_threat_valid_input(self):
        # Test threat modeling with valid input data
        result = model_threat(self.valid_threat_data)
        self.assertIsNotNone(result)
        self.assertIn('risk_score', result)
        self.assertTrue(0 <= result['risk_score'] <= 1)

    def test_model_threat_invalid_input(self):
        # Test threat modeling with invalid input data
        with self.assertRaises(ValueError):
            model_threat(self.invalid_threat_data)

    def test_assess_risk_valid_input(self):
        # Test risk assessment with valid input data
        risk_score = assess_risk(self.valid_threat_data['likelihood'], self.valid_threat_data['impact'])
        self.assertTrue(0 <= risk_score <= 1)

    def test_assess_risk_invalid_input(self):
        # Test risk assessment with invalid input data
        with self.assertRaises(ValueError):
            assess_risk(self.invalid_threat_data['likelihood'], self.invalid_threat_data['impact'])

    def test_input_validation(self):
        # Test input validation utility
        self.assertTrue(validate_input(self.valid_threat_data))
        self.assertFalse(validate_input(self.invalid_threat_data))

if __name__ == '__main__':
    unittest.main()