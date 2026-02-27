# Network Packet Analyzer 🕵️‍♂️📡

A **GUI-based Network Packet Analyzer** built using **Python** that captures live network packets, analyzes protocols, detects abnormal traffic, and generates a final network analysis report.

This project is designed for **Computer Networks learning**, **Cybersecurity basics**, and **mini / final-year project submissions**.

---

## 📌 Table of Contents
- Features
- Technologies Used
- Project Structure
- How It Works
- Installation & Setup
- How to Run
- Windows EXE Version
- Output & Reports
- Use Cases
- Limitations
- Future Enhancements
- Author
- Disclaimer

---

## 🚀 Features
- Live network packet capturing  
- Supports **TCP, UDP, ICMP**  
- Displays:
  - Source IP & Destination IP  
  - Source Port & Destination Port  
  - Protocol type  
- High traffic detection with warnings  
- Final network analysis report generation  
- Graphical User Interface (GUI)  
- Can be converted into a standalone **Windows EXE**

---

## 🧠 Technologies Used
- Python 3  
- Scapy – packet capturing and decoding  
- Tkinter – GUI development  
- PyInstaller – EXE creation  
- Git & GitHub – version control  

---

## 📁 Project Structure

```text
NetworkPacketAnalyzer/
├── analyzer/              # Packet analysis & report generation
│   ├── protocol_decoder.py
│   └── final_report.py
├── capture/               # Packet capturing logic
│   └── packet_capture.py
├── gui/                   # GUI application
│   └── gui_app.py
├── main.py                # Entry point
├── test_report.py         # Testing script
├── README.md              # Project documentation
└── .gitignore             # Git ignore rules
⚙️ How It Works

Captures live network packets using Scapy

Decodes each packet to extract:

IP addresses

Ports

Protocol type

Maintains packet statistics internally

Detects high traffic from a single IP using thresholds

Generates a final analysis report

Displays all results in the GUI

🛠 Installation & Setup
1️⃣ Prerequisites

Python 3.9 or higher

Windows OS

Administrator privileges (required for packet capture)

2️⃣ Install Dependencies
pip install scapy
▶️ How to Run

⚠️ IMPORTANT:
Run Command Prompt as Administrator.

python -m gui.gui_app

The GUI window will open and start capturing packets.

🪟 Windows EXE Version (No Python Needed)

Build a standalone EXE using PyInstaller:

pyinstaller --onefile --windowed gui/gui_app.py

After build:

dist/gui_app.exe
EXE Features

Does NOT require Python

Can be shared with anyone

Runs on Windows PCs

📌 Recommended to upload the EXE using GitHub Releases.

📊 Output & Reports

Live packet details shown in GUI

High traffic warnings displayed in real time

Final report includes:

Total packets captured

Packet count per IP

Protocol-wise statistics

Detected anomalies

🎓 Use Cases

Computer Networks mini / final-year project

Cybersecurity fundamentals practice

Packet analysis learning tool

Network monitoring demonstration

⚠️ Limitations

Works only on Windows

Requires administrator access

Not intended for production use

Educational purpose only

🚀 Future Enhancements

Protocol-wise graphs (TCP / UDP / ICMP)

Export reports as PDF

Advanced attack detection (SYN flood, port scanning)

Cross-platform support

Improved GUI design

## 👨‍💻 Author

**Mohan**  
🔗 GitHub: https://github.com/Mohan-10-15
⚠️ Disclaimer

This project is strictly for educational and learning purposes only.
Do NOT use this application on networks without proper authorization.

The author is not responsible for any misuse of this software.

⭐ If you found this project helpful, consider giving it a star on GitHub!