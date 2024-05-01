import os
import json
from datetime import datetime
from utils.forensic_utils import analyze_log_file, analyze_packet_capture, detect_intrusion_attempts
from utils.logging_utils import log_action, log_error
from utils.helpers import parse_data, validate_input
from data.configurations import forensic_data_schema

class DigitalForensics:
    def __init__(self, api_key):
        self.api_key = api_key
        self.forensic_reports = []

    def analyze_system_logs(self, log_directory):
        try:
            for filename in os.listdir(log_directory):
                if filename.endswith(".log"):
                    log_path = os.path.join(log_directory, filename)
                    log_data = analyze_log_file(log_path)
                    self.forensic_reports.append(log_data)
                    log_action(f"Analyzed log file: {filename}")
        except Exception as e:
            log_error(f"Error analyzing system logs: {str(e)}")

    def analyze_network_traffic(self, pcap_file):
        try:
            traffic_analysis = analyze_packet_capture(pcap_file)
            self.forensic_reports.append(traffic_analysis)
            log_action(f"Analyzed network traffic from pcap file: {pcap_file}")
        except Exception as e:
            log_error(f"Error analyzing network traffic: {str(e)}")

    def detect_intrusions(self, log_directory):
        try:
            for filename in os.listdir(log_directory):
                if filename.endswith(".log"):
                    log_path = os.path.join(log_directory, filename)
                    intrusion_attempts = detect_intrusion_attempts(log_path)
                    self.forensic_reports.extend(intrusion_attempts)
                    log_action(f"Detected intrusion attempts in log file: {filename}")
        except Exception as e:
            log_error(f"Error detecting intrusions: {str(e)}")

    def generate_forensic_report(self):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        report_filename = f"forensic_report_{timestamp}.json"
        try:
            with open(report_filename, 'w') as report_file:
                json.dump(self.forensic_reports, report_file, indent=4)
            log_action(f"Generated forensic report: {report_filename}")
            return report_filename
        except Exception as e:
            log_error(f"Error generating forensic report: {str(e)}")
            return None

    def run_forensic_analysis(self, log_directory, pcap_file):
        self.analyze_system_logs(log_directory)
        self.analyze_network_traffic(pcap_file)
        self.detect_intrusions(log_directory)
        return self.generate_forensic_report()

# Example usage
if __name__ == "__main__":
    api_key = validate_input("Enter your API key: ")
    forensic_analyzer = DigitalForensics(api_key)
    log_dir = validate_input("Enter the path to the log directory: ")
    pcap_path = validate_input("Enter the path to the pcap file: ")
    forensic_report = forensic_analyzer.run_forensic_analysis(log_dir, pcap_path)
    if forensic_report:
        print(f"Forensic analysis completed. Report saved as: {forensic_report}")
    else:
        print("Forensic analysis failed. Please check the logs for more information.")