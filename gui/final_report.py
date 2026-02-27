import tkinter as tk
import threading
import time

from capture.packet_capture import capture_packets
from analyzer.protocol_decoder import set_gui_callback
from analyzer.final_report import generate_report

root = tk.Tk()
root.title("Network Packet Analyzer")

output_box = tk.Text(root, width=90, height=30)
output_box.pack()

status = tk.Label(root, text="Status: Idle")
status.pack()

def gui_output(text):
    output_box.insert(tk.END, text)
    output_box.see(tk.END)

def start_capture():
    status.config(text="Status: Capturing packets...")
    output_box.insert(tk.END, "🔍 Packet capture started...\n\n")

    set_gui_callback(gui_output)

    CAPTURE_TIME = 15  # seconds

    def run():
        start = time.time()
        while time.time() - start < CAPTURE_TIME:
            capture_packets(timeout=1)

        output_box.insert(tk.END, "\n📌 Capture finished. Generating report...\n\n")
        report = generate_report()
        output_box.insert(tk.END, report)
        status.config(text="Status: Completed")

    threading.Thread(target=run, daemon=True).start()

btn = tk.Button(root, text="Start Capture", command=start_capture)
btn.pack()

root.mainloop()