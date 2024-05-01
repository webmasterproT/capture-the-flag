import unittest
from ctf_simulation import simulate_ctf, evaluate_performance
from utils.helpers import parse_data, validate_input
from data.configurations import config_schema
from data.logs import log_schema

class TestCTFSimulation(unittest.TestCase):
    def setUp(self):
        # Load configurations for CTF simulation
        self.config = parse_data(config_schema, 'data/configurations/ctf_config.json')
        validate_input(self.config, config_schema)

    def test_simulate_ctf(self):
        # Test the CTF simulation function
        result = simulate_ctf(self.config)
        self.assertTrue(result['success'], "CTF simulation should be successful")

    def test_evaluate_performance(self):
        # Test the performance evaluation function
        log_data = parse_data(log_schema, 'data/logs/ctf_log.json')
        performance = evaluate_performance(log_data)
        self.assertIsNotNone(performance, "Performance evaluation should return a result")
        self.assertIn('score', performance, "Performance evaluation should include a score")
        self.assertGreaterEqual(performance['score'], 0, "Performance score should be non-negative")

    def test_ctf_simulation_with_invalid_config(self):
        # Test CTF simulation with invalid configuration
        with self.assertRaises(ValueError):
            simulate_ctf({})

    def test_evaluate_performance_with_invalid_log(self):
        # Test performance evaluation with invalid log data
        with self.assertRaises(ValueError):
            evaluate_performance({})

if __name__ == '__main__':
    unittest.main()