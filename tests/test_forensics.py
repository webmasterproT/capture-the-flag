import unittest
from forensics import analyze_log_files, network_packet_capture_analysis
from utils.forensic_utils import forensic_data_schema
from utils.logging_utils import log_action, log_error

class TestForensics(unittest.TestCase):

    def setUp(self):
        # Setup can include preparing log files, network packet captures, etc.
        self.sample_log_file = "data/logs/sample_log.log"
        self.sample_pcap_file = "data/logs/sample_capture.pcap"
        self.expected_log_analysis_result = True
        self.expected_pcap_analysis_result = True

    def test_analyze_log_files(self):
        try:
            result = analyze_log_files(self.sample_log_file)
            self.assertEqual(result, self.expected_log_analysis_result)
            log_action("Log file analysis test passed.")
        except Exception as e:
            log_error(f"Log file analysis test failed: {str(e)}")
            self.fail(f"Log file analysis test failed: {str(e)}")

    def test_network_packet_capture_analysis(self):
        try:
            result = network_packet_capture_analysis(self.sample_pcap_file)
            self.assertEqual(result, self.expected_pcap_analysis_result)
            log_action("Network packet capture analysis test passed.")
        except Exception as e:
            log_error(f"Network packet capture analysis test failed: {str(e)}")
            self.fail(f"Network packet capture analysis test failed: {str(e)}")

    def test_forensic_data_schema(self):
        # This test ensures that the forensic data schema is valid and usable
        try:
            self.assertIsInstance(forensic_data_schema, dict)
            log_action("Forensic data schema test passed.")
        except AssertionError:
            log_error("Forensic data schema test failed.")
            self.fail("Forensic data schema test failed.")

if __name__ == '__main__':
    unittest.main()