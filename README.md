# 🕵️‍♂️ Network Packet Analyzer 📡

A **GUI-based Network Packet Analyzer** built using **Python** that captures live network packets, analyzes network protocols, detects abnormal traffic, and generates a final network analysis report.

This project is intended for **Computer Networks learning**, **Cybersecurity fundamentals**, and **mini / final-year academic projects**.

---

## 🚀 Features

- Live network packet capturing  
- Supports **TCP, UDP, and ICMP** protocols  
- Displays:
  - Source IP & Destination IP  
  - Source Port & Destination Port  
  - Protocol type  
- High-traffic detection with real-time warnings  
- Final network analysis report generation  
- User-friendly **Graphical User Interface (GUI)**  
- Can be converted into a standalone **Windows EXE**

---

## 🧠 Technologies Used

- Python 3  
- Scapy – packet capturing and decoding  
- Tkinter – GUI development  
- PyInstaller – EXE creation  
- Git & GitHub – version control  

---

## ⚙️ How It Works

- Captures live network packets using **Scapy**  
- Decodes each packet to extract:
  - IP addresses  
  - Ports  
  - Protocol information  
- Maintains packet statistics internally  
- Detects high traffic from a single IP using predefined thresholds  
- Generates a final network analysis report  
- Displays all results in a GUI window  

---

## 🛠 Installation & Setup

### 1️⃣ Prerequisites
- Python 3.9 or higher  
- Windows OS  
- Administrator privileges (required for packet capture)

### 2️⃣ Install Dependencies
pip install scapy
### ▶️ How to Run

⚠️ IMPORTANT:
Run Command Prompt as Administrator.

python -m gui.gui_app

The GUI window will open and begin capturing network packets.

🪟 Windows EXE Version (No Python Required)

You can build a standalone Windows executable using PyInstaller:

pyinstaller --onefile --windowed gui/gui_app.py

After build:

dist/gui_app.exe
EXE Features

- No Python installation required

- Easily shareable

- Runs on any Windows PC

📌 Recommended: Upload the EXE using GitHub Releases.

📊 Output & Reports

- Live packet details displayed in the GUI

- Real-time high-traffic warnings

- Final report includes:

     - Total packets captured

     - Packet count per IP

     - Protocol-wise statistics

     - Detected anomalies

🎓 Use Cases

- Computer Networks mini / final-year project

- Cybersecurity fundamentals practice

- Packet analysis learning tool

- Network monitoring demonstrations

⚠️ Limitations

- Works only on Windows OS

- Requires administrator privileges

- Not intended for production network monitoring

- For educational use only

🚀 Future Enhancements

- Protocol-wise graphical analysis (TCP / UDP / ICMP)

- Export reports as PDF

- Advanced attack detection (SYN flood, port scanning)

- Cross-platform support

- Enhanced GUI design

👨‍💻 Author

Mohan
GitHub: https://github.com/Mohan-10-15

⚠️ Disclaimer

This project is strictly for educational and learning purposes only.
Do NOT use this application on networks without proper authorization.

The author is not responsible for any misuse of this software.

⭐ If you found this project helpful, consider giving it a star on GitHub!
