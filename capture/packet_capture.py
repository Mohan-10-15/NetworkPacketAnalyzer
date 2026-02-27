# capture/packet_capture.py
import random
import time

raw_packets = []

def capture_packets(timeout=1):
    """
    Simulate capturing packets.
    Replace with scapy or real packet capture logic.
    """
    sample_ips = ["192.168.1.10", "192.168.1.23", "116.119.64.143"]
    sample_protocols = ["TCP", "UDP", "ICMP"]

    pkt = {
        "src": random.choice(sample_ips),
        "dst": random.choice(sample_ips),
        "protocol": random.choice(sample_protocols),
        "src_port": random.randint(1024, 65535),
        "dst_port": random.randint(80, 8080)
    }
    raw_packets.append(pkt)

    # Normally decode_packet would be called here
    from analyzer.protocol_decoder import decode_packet
    decode_packet(pkt)
    time.sleep(timeout)