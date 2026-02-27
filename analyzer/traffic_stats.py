# This list will store packet information
packet_list = []

def add_packet(src_ip, dst_ip, protocol):
    packet_list.append({
        "source": src_ip,
        "destination": dst_ip,
        "protocol": protocol
    })

def show_statistics():
    print("\n📊 TRAFFIC STATISTICS")

    protocol_count = {}

    for packet in packet_list:
        proto = packet["protocol"]
        protocol_count[proto] = protocol_count.get(proto, 0) + 1

    for proto, count in protocol_count.items():
        print(f"{proto} packets : {count}")