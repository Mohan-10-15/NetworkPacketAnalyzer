from analyzer.final_report import generate_report, add_packet
from analyzer.attack_detector import warnings

# simulate packets
add_packet("UDP", "192.168.1.1")
add_packet("UDP", "192.168.1.1")
add_packet("TCP", "192.168.1.2")

# simulate warning
warnings.append("⚠ High traffic detected from 192.168.1.1")

# generate report
text = generate_report()

print("\nREPORT GENERATED:\n")
print(text)