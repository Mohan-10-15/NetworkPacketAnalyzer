# analyzer/final_report.py
import os
import sys
from datetime import datetime
from analyzer.protocol_decoder import packet_count, warnings, total_packets

def generate_report():
    if getattr(sys, 'frozen', False):
        output_dir = os.path.join(os.path.dirname(sys.executable), "logs")
    else:
        output_dir = "logs"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(output_dir, f"final_report_{timestamp}.txt")

    lines = []
    lines.append("========= FINAL NETWORK ANALYSIS REPORT =========\n")
    lines.append(f"Total packets captured: {total_packets}\n\n")

    # NEW: Packet count per IP by protocol
    lines.append("Packet count per IP (by protocol):\n")
    for ip, proto_dict in packet_count.items():
        proto_counts = ", ".join([f"{p}={c}" for p,c in proto_dict.items()])
        lines.append(f"{ip} : {proto_counts}\n")

    # Warnings
    lines.append("\nWarnings:\n")
    if warnings:
        for w in warnings:
            lines.append(w + "\n")
    else:
        lines.append("No suspicious activity detected\n")

    lines.append("\n===============================================\n")

    # Save report
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(lines)

    return "".join(lines) + f"\n📁 Report saved at: {filename}\n"