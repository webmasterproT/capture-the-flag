import socket
import struct
from scapy.all import sniff, IP, TCP
from utils.network_utils import analyze_traffic, detect_intrusion, monitor_network
from utils.logging_utils import log_action, log_error, log_info
from data.configurations import api_key

class NetworkAnalysis:
    def __init__(self):
        self.api_key = api_key

    def start_sniffing(self, filter="", iface=None, prn=None, store=0):
        try:
            log_info("Starting network sniffing...")
            sniff(filter=filter, iface=iface, prn=prn, store=store)
            log_action("Network sniffing started successfully.")
        except Exception as e:
            log_error(f"Error starting network sniffing: {e}")

    def analyze_packet(self, packet):
        try:
            if IP in packet and TCP in packet:
                src_ip = packet[IP].src
                dst_ip = packet[IP].dst
                src_port = packet[TCP].sport
                dst_port = packet[TCP].dport
                log_info(f"Packet: {src_ip}:{src_port} -> {dst_ip}:{dst_port}")
                analyze_traffic(packet)
                intrusion_detected = detect_intrusion(packet)
                if intrusion_detected:
                    log_action(f"Intrusion detected from {src_ip}")
        except Exception as e:
            log_error(f"Error analyzing packet: {e}")

    def get_host_by_name(self, hostname):
        try:
            ip_address = socket.gethostbyname(hostname)
            log_info(f"IP address of {hostname} is {ip_address}")
            return ip_address
        except Exception as e:
            log_error(f"Error resolving hostname {hostname}: {e}")
            return None

    def get_service_by_port(self, port, protocol='tcp'):
        try:
            service = socket.getservbyport(port, protocol)
            log_info(f"Service running on port {port}/{protocol}: {service}")
            return service
        except Exception as e:
            log_error(f"Error getting service for port {port}/{protocol}: {e}")
            return None

    def monitor_for_intrusions(self):
        self.start_sniffing(prn=self.analyze_packet)

if __name__ == "__main__":
    network_analyzer = NetworkAnalysis()
    network_analyzer.monitor_for_intrusions()