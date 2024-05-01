import os
import subprocess
from utils.forensic_utils import analyze_logs, extract_artifacts
from utils.logging_utils import log_action, log_error
from data.configurations import forensic_data_schema

class ForensicTools:
    def __init__(self, api_key):
        self.api_key = api_key

    def run_digital_forensics(self, target_directory):
        try:
            # Check if the target directory exists
            if not os.path.exists(target_directory):
                raise FileNotFoundError(f"Target directory {target_directory} not found.")

            # Log the forensic action
            log_action(f"Starting digital forensics on {target_directory}")

            # Analyze logs and extract artifacts
            logs_analysis = analyze_logs(target_directory)
            artifacts = extract_artifacts(target_directory)

            # Log the results of the analysis
            log_action(f"Logs analysis completed: {logs_analysis}")
            log_action(f"Artifacts extracted: {artifacts}")

            # Return the results
            return {
                "logs_analysis": logs_analysis,
                "artifacts": artifacts
            }
        except Exception as e:
            log_error(f"Error running digital forensics: {str(e)}")
            return None

    def perform_memory_forensics(self, memory_dump):
        try:
            # Ensure memory dump file exists
            if not os.path.isfile(memory_dump):
                raise FileNotFoundError(f"Memory dump file {memory_dump} not found.")

            # Log the forensic action
            log_action(f"Starting memory forensics on {memory_dump}")

            # Placeholder for memory analysis logic
            # This would involve using external tools like Volatility or Rekall
            memory_analysis = self._analyze_memory_dump(memory_dump)

            # Log the results of the memory analysis
            log_action(f"Memory analysis completed: {memory_analysis}")

            # Return the results
            return memory_analysis
        except Exception as e:
            log_error(f"Error performing memory forensics: {str(e)}")
            return None

    def _analyze_memory_dump(self, memory_dump):
        # Placeholder function for memory dump analysis
        # This function would interface with external tools and return analysis results
        # For example, using Volatility framework for memory analysis
        volatility_command = f"volatility -f {memory_dump} --profile=Win7SP1x64 pslist"
        process = subprocess.Popen(volatility_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if process.returncode != 0:
            log_error(f"Memory analysis failed: {stderr.decode().strip()}")
            return None

        return stdout.decode().strip()

    def analyze_network_traffic(self, pcap_file):
        try:
            # Ensure pcap file exists
            if not os.path.isfile(pcap_file):
                raise FileNotFoundError(f"PCAP file {pcap_file} not found.")

            # Log the forensic action
            log_action(f"Starting network traffic analysis on {pcap_file}")

            # Placeholder for network traffic analysis logic
            # This would involve using tools like Wireshark/tshark or tcpdump
            network_analysis = self._analyze_pcap(pcap_file)

            # Log the results of the network analysis
            log_action(f"Network traffic analysis completed: {network_analysis}")

            # Return the results
            return network_analysis
        except Exception as e:
            log_error(f"Error analyzing network traffic: {str(e)}")
            return None

    def _analyze_pcap(self, pcap_file):
        # Placeholder function for PCAP file analysis
        # This function would interface with external tools and return analysis results
        # For example, using tshark for extracting information from pcap files
        tshark_command = f"tshark -r {pcap_file} -T fields -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport"
        process = subprocess.Popen(tshark_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if process.returncode != 0:
            log_error(f"PCAP analysis failed: {stderr.decode().strip()}")
            return None

        return stdout.decode().strip()

# Example usage:
# forensic_tools = ForensicTools(api_key='your_api_key_here')
# forensic_results = forensic_tools.run_digital_forensics('/path/to/target/directory')
# memory_forensics_results = forensic_tools.perform_memory_forensics('/path/to/memory/dump')
# network_traffic_results = forensic_tools.analyze_network_traffic('/path/to/pcap/file')