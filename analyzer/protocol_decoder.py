# analyzer/protocol_decoder.py
import threading

# ---------------- Global trackers ---------------- #
# Nested dict to track packets per IP per protocol
packet_count = {}       # {IP: {"TCP":0, "UDP":0, "ICMP":0, "OTHER":0}}
warnings = []           # High traffic warnings
total_packets = 0       # Total packets captured

protocol_count_over_time = {
    "TCP": [],
    "UDP": [],
    "ICMP": [],
    "OTHER": []
}

# GUI callback
gui_callback = None
def set_gui_callback(callback):
    global gui_callback
    gui_callback = callback

# ---------------- Packet decoding ---------------- #
def decode_packet(pkt):
    global total_packets
    total_packets += 1

    src = pkt.get("src", "Unknown")
    dst = pkt.get("dst", "Unknown")
    proto = pkt.get("protocol", "OTHER")
    if proto not in ["TCP", "UDP", "ICMP"]:
        proto = "OTHER"

    # Initialize nested dicts if first time
    for ip in [src, dst]:
        if ip not in packet_count:
            packet_count[ip] = {"TCP":0, "UDP":0, "ICMP":0, "OTHER":0}

    # Count packets per protocol per IP
    packet_count[src][proto] += 1
    packet_count[dst][proto] += 1

    # Protocol count over time for graphs
    while len(protocol_count_over_time[proto]) < total_packets:
        protocol_count_over_time[proto].append(0)
    protocol_count_over_time[proto][-1] += 1

    # High traffic detection
    total_ip_packets = sum(packet_count[src].values())
    if total_ip_packets > 50 and f"⚠ High traffic detected from {src}" not in warnings:
        warnings.append(f"⚠ High traffic detected from {src}")

    # Send live updates to GUI
    if gui_callback:
        gui_callback(f"Source IP: {src}\nDestination IP: {dst}\nProtocol: {proto}\n\n")