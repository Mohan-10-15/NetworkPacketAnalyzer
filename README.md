# Network Packet Analyzer 🕵️‍♂️📡

A **GUI-based Network Packet Analyzer** built using **Python** that captures live network packets, analyzes protocols, detects abnormal traffic, and generates a final network analysis report.

This project is designed for **Computer Networks learning**, **Cybersecurity basics**, and **mini / final-year project submissions**.

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
- Standalone **Windows EXE** support  

---

## 🧠 Technologies Used
- Python 3  
- Scapy  
- Tkinter  
- PyInstaller  
- Git & GitHub  

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

Captures live packets using Scapy

Decodes IP, ports, and protocol

Maintains packet statistics

Detects high traffic from single IPs

Generates a final report

Displays everything in the GUI

🛠 Installation & Setup
Prerequisites

Python 3.9+

Windows OS

Administrator privileges

Install Dependencies
pip install scapy
▶️ How to Run

⚠️ Run Command Prompt as Administrator

python -m gui.gui_app
🪟 Windows EXE Version

Build EXE:

pyinstaller --onefile --windowed gui/gui_app.py

Output:

dist/gui_app.exe
📊 Output & Reports

Live packet capture in GUI

Real-time traffic warnings

Final report with:

Total packets

Packet count per IP

Protocol statistics

🎓 Use Cases

Computer Networks mini / final-year project

Cybersecurity fundamentals

Packet analysis learning

GUI-based Python application

⚠️ Limitations

Windows only

Requires admin privileges

Educational use only

🚀 Future Enhancements

Protocol graphs

PDF report export

Advanced attack detection

Cross-platform support
👨‍💻 Author

Mohan
GitHub: 👉 https://github.com/Mohan-10-15

⚠️ Disclaimer

This project is strictly for educational and learning purposes only.
Do NOT use this application on networks without proper authorization.

The author is not responsible for any misuse of this software.

⭐ If you found this project helpful, consider giving it a star on GitHub!
