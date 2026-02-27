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



```markdown
## 📊 Output

### 🔹 Live Packet Capture
Displays real-time packet information including:
- Source IP
- Destination IP
- Protocol
- Source and destination ports

### 🔹 High Traffic Warning
Detects excessive packet flow from specific IP addresses and displays real-time warning messages.

### 🔹 Final Network Analysis Report
Generates a summary report containing:
- Total packets captured
- Packet count per IP and protocol
- List of detected high-traffic IPs

## 🎓 Use Cases

- Computer Networks mini / final year project
- Learning packet sniffing and protocol analysis
- Understanding TCP, UDP, and ICMP behavior
- Introduction to cybersecurity & network monitoring
- Building real-world GUI-based Python applications

## 🪟 Windows EXE (No Python Required)

This application can be used without installing Python by running the Windows executable.

### 🔽 How to Use
1. Go to **GitHub → Releases**
2. Download `gui_app.exe`
3. Run the application as **Administrator**

## ⚠️ Disclaimer

This project is strictly for educational and learning purposes only.  
Do **NOT** use this application on networks without proper authorization.  
The author is not responsible for any misuse of this software.

## ⚠️ Disclaimer

This project is strictly for educational and learning purposes only.  
Do **NOT** use this application on networks without proper authorization.  
The author is not responsible for any misuse of this software.
