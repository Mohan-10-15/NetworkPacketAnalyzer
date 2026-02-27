ip_counter = {}
warnings = []   # <-- NEW (important)

THRESHOLD = 5   # demo-friendly (you can change to 20 later)

def detect_attack(source_ip):
    ip_counter[source_ip] = ip_counter.get(source_ip, 0) + 1

    if ip_counter[source_ip] == THRESHOLD:
        warning_msg = f"⚠ High traffic detected from {source_ip}"
        print(warning_msg)
        warnings.append(warning_msg)