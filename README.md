# Network Packet Analyzer 🕵️‍♂️📡

A **GUI-based Network Packet Analyzer** built using **Python**.  
This application captures live network packets, analyzes network protocols, detects high traffic activity, and generates a detailed final network analysis report.

This project is suitable for **students, beginners, and cybersecurity learners**, and it can be shared as a **standalone Windows application**.

---

## 🚀 Features

- Live network packet capturing
- Supports **TCP, UDP, and ICMP** protocols
- Displays source & destination IP addresses and ports
- High traffic detection with real-time warnings
- Generates a final network analysis report
- Easy-to-use **GUI application (Tkinter)**
- Can be converted into a **standalone Windows EXE**

---

## 🧠 Technologies Used

- **Python 3**
- **Scapy** – Packet capturing and analysis
- **Tkinter** – GUI development
- **PyInstaller** – Windows EXE build
- **Git & GitHub** – Version control

---

## 📁 Project Structure

```text
NetworkPacketAnalyzer/
├── analyzer/       # Packet analysis & report generation
│   ├── protocol_decoder.py
│   └── final_report.py
├── capture/        # Packet capturing logic
│   └── packet_capture.py
├── gui/            # GUI application
│   └── gui_app.py
├── main.py         # Optional entry point
├── test_report.py  # Testing script
└── README.md       # Project documentation
▶️ How to Run (Using Python)
1️⃣ Install Dependencies

Make sure Python 3 is installed, then run:

pip install scapy
2️⃣ Run the GUI Application
python -m gui.gui_app

⚠️ Important:
You must run Command Prompt as Administrator to allow packet capturing.

📊 Output
🔹 Live Packet Capture

Displays real-time packet information:

Source IP

Destination IP

Protocol

Source & destination ports

🔹 High Traffic Warning

Detects excessive packet flow from specific IP addresses

Displays warning messages in real time

🔹 Final Network Analysis Report

Total packets captured

Packet count per IP and protocol

Detected high-traffic IPs

Automatically generated after capture

🪟 Windows EXE (No Python Required)

You can run this application without installing Python by using the Windows executable.

🔽 Download EXE

Go to GitHub → Releases

Download gui_app.exe

Run the EXE as Administrator

🎓 Use Cases

Computer Networks mini / final year project

Learning packet sniffing and protocol analysis

Understanding TCP, UDP, and ICMP behavior

Introduction to cybersecurity & network monitoring

Building real-world GUI-based Python applications

👨‍💻 Author

Mohan
GitHub: https://github.com/Mohan-10-15

⚠️ Disclaimer

This project is strictly for educational and learning purposes only.
Do NOT use this application on networks without proper authorization.

The author is not responsible for any misuse of this software.

⭐ If you found this project helpful, consider giving it a star on GitHub!
