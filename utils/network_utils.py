```python
import socket
import struct
from scapy.all import sniff, IP, TCP, UDP, ICMP
from utils.logging_utils import log_info, log_error

def analyze_traffic(packet_count=100, filter_protocol=None, callback=None):
    """
    Capture and analyze network traffic.
    
    :param packet_count: Number of packets to capture.
    :param filter_protocol: Protocol to filter for (e.g., 'tcp', 'udp', 'icmp').
    :param callback: Optional callback function to process each packet.
    """
    try:
        # Define the packet processing function
        def process_packet(packet):
            if callback:
                callback(packet)
            else:
                # Default processing
                log_info(f"Packet: {packet.summary()}")

        # Start sniffing the network
        sniff(filter=filter_protocol, count=packet_count, prn=process_packet)
        log_info("Traffic analysis completed.")
    except Exception as e:
        log_error(f"Error analyzing traffic: {e}")

def detect_intrusion(packet):
    """
    Analyze a single packet to detect potential intrusions.
    
    :param packet: The packet to analyze.
    :return: Boolean indicating whether an intrusion was detected.
    """
    try:
        # Simple intrusion detection logic (placeholder for more complex analysis)
        if packet.haslayer(IP) and packet[IP].dst == '127.0.0.1':
            log_info("Intrusion detected: Packet targeted at localhost.")
            return True
        return False
    except Exception as e:
        log_error(f"Error detecting intrusion: {e}")
        return False

def monitor_network(interface='eth0', filter_protocol=None):
    """
    Monitor network traffic on a given interface.
    
    :param interface: Network interface to monitor.
    :param filter_protocol: Protocol to filter for (e.g., 'tcp', 'udp', 'icmp').
    """
    try:
        log_info(f"Starting network monitoring on interface {interface}...")
        sniff(iface=interface, filter=filter_protocol, prn=detect_intrusion)
    except Exception as e:
        log_error(f"Error monitoring network: {e}")

def get_open_ports(target_ip, port_range):
    """
    Scan for open ports on a target IP within the specified range.
    
    :param target_ip: IP address of the target.
    :param port_range: Tuple indicating the range of ports to scan (start, end).
    :return: List of open ports.
    """
    open_ports = []
    for port in range(*port_range):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                open_ports.append(port)
    log_info(f"Open ports on {target_ip}: {open_ports}")
    return open_ports

def craft_packet(destination_ip, destination_port, payload):
    """
    Craft a custom packet with the given payload.
    
    :param destination_ip: IP address of the destination.
    :param destination_port: Port number of the destination.
    :param payload: Payload to include in the packet.
    :return: Crafted packet.
    """
    try:
        packet = IP(dst=destination_ip) / TCP(dport=destination_port) / payload
        return packet
    except Exception as e:
        log_error(f"Error crafting packet: {e}")
        return None

def send_packet(packet):
    """
    Send a crafted packet.
    
    :param packet: The packet to send.
    """
    try:
        send(packet)
        log_info(f"Packet sent: {packet.summary()}")
    except Exception as e:
        log_error(f"Error sending packet: {e}")

# Example usage:
# analyze_traffic(packet_count=50, filter_protocol='tcp')
# monitor_network(interface='eth0', filter_protocol='tcp')
# ports = get_open_ports('192.168.1.1', (1, 1024))
# packet = craft_packet('192.168.1.1', 80, 'GET / HTTP/1.1\r\nHost: target\r\n\r\n')
# send_packet(packet)
```