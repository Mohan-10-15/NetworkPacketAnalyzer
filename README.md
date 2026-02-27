# Network Packet Analyzer 🕵️‍♂️📡

A **GUI-based Network Packet Analyzer** built using **Python**.  
This application captures live network packets, analyzes network protocols, detects high traffic activity, and generates a final network analysis report.

This project is ideal for **Computer Networks students, beginners, and cybersecurity learners**, and it can also be shared as a **standalone Windows application**.

---

## 🚀 Features

- Live network packet capturing
- Supports **TCP, UDP, and ICMP** protocols
- Displays source & destination IP addresses and ports
- High traffic detection with real-time warnings
- Generates a detailed final network analysis report
- Easy-to-use **GUI application**
- Can be converted into a **standalone Windows EXE**

---

## 🧠 Technologies Used

- **Python 3**
- **Scapy** – Packet capturing and analysis
- **Tkinter** – GUI development
- **PyInstaller** – Windows EXE generation
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

Ensure Python 3 is installed, then run:

pip install scapy
2️⃣ Run the GUI Application
python -m gui.gui_app

⚠️ Important:
Packet capturing requires Administrator privileges.
Always run the Command Prompt as Administrator.

📊 Output
🔹 Live Packet Capture

Displays real-time packet details:

Source IP

Destination IP

Protocol

Source & destination ports

🔹 High Traffic Detection

Detects excessive packet flow from specific IP addresses

Displays warning messages in real time

🔹 Final Network Analysis Report

Total packets captured

Packet count per IP and protocol

List of detected high-traffic IPs

Generated automatically after capture

🪟 Windows EXE (No Python Required)

This application can be used without installing Python by running the Windows executable.

🔽 How to Use

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

⭐ If you found this project useful, consider giving it a star on GitHub!
