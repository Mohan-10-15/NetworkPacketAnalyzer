import tkinter as tk
import threading
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import time

from capture.packet_capture import capture_packets
from analyzer.protocol_decoder import set_gui_callback, packet_count, warnings, total_packets, protocol_count_over_time
from analyzer.final_report import generate_report

# ----------------- Setup GUI ----------------- #
root = tk.Tk()
root.title("Professional Network Packet Analyzer")
root.geometry("1400x800")

# Logs Frame
log_frame = tk.Frame(root)
log_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

output_box = tk.Text(log_frame, width=90, height=35)
output_box.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
scrollbar = tk.Scrollbar(log_frame, command=output_box.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
output_box.config(yscrollcommand=scrollbar.set)

status = tk.Label(root, text="Status: Idle", font=("Arial", 12))
status.pack(side=tk.TOP, pady=5)

# Graphs Frame
graph_frame = tk.Frame(root)
graph_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(7,7))
plt.tight_layout(pad=3.0)
canvas = FigureCanvasTkAgg(fig, master=graph_frame)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# ----------------- GUI Callback ----------------- #
def gui_output(text):
    output_box.insert(tk.END, text)
    output_box.see(tk.END)

set_gui_callback(gui_output)

# ----------------- Update Graphs ----------------- #
def update_graphs():
    # Protocol Distribution
    ax1.clear()
    protocols = {"TCP":0, "UDP":0, "ICMP":0, "OTHER":0}
    for proto, lst in protocol_count_over_time.items():
        protocols[proto] = sum(lst)
    ax1.bar(protocols.keys(), protocols.values(), color=['blue','green','red','gray'])
    ax1.set_title("Protocol Distribution")
    ax1.set_ylabel("Packet Count")

    # Packets per IP (high traffic in red)
    ax2.clear()
    ips = list(packet_count.keys())
    counts = [sum(packet_count[ip].values()) for ip in ips]
    colors = ['red' if count > 50 else 'orange' for count in counts]
    ax2.bar(ips, counts, color=colors)
    ax2.set_title("Packets per IP (High traffic in red)")
    ax2.set_ylabel("Packet Count")
    ax2.set_xticks(range(len(ips)))
    ax2.set_xticklabels(ips, rotation=45, ha="right")

    # Traffic over time
    ax3.clear()
    for proto, lst in protocol_count_over_time.items():
        ax3.plot(range(len(lst)), lst, label=proto)
    ax3.set_title("Packet Traffic Over Time")
    ax3.set_ylabel("Packets")
    ax3.set_xlabel("Time (s)")
    ax3.legend()

    canvas.draw()

# ----------------- Start Capture ----------------- #
def start_capture():
    output_box.delete("1.0", tk.END)
    status.config(text="Status: Capturing packets...")
    output_box.insert(tk.END, "🔍 Packet capture started...\n\n")

    CAPTURE_TIME = 15  # seconds

    def run():
        start_time = time.time()
        while time.time() - start_time < CAPTURE_TIME:
            capture_packets(timeout=1)
            update_graphs()

        # Final Report
        output_box.insert(tk.END, "\n📌 Capture finished. Generating FINAL REPORT...\n\n")
        output_box.insert(tk.END, "="*100 + "\n")
        report = generate_report()
        output_box.insert(tk.END, report)
        output_box.insert(tk.END, "="*100 + "\n")
        status.config(text="Status: Completed")
        update_graphs()

    threading.Thread(target=run, daemon=True).start()

# ----------------- Start Button ----------------- #
btn = tk.Button(root, text="Start Capture", font=("Arial", 12), command=start_capture)
btn.pack(pady=5)

root.mainloop()