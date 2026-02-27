# Network Packet Analyzer 🕵️‍♂️📡

A **GUI-based Network Packet Analyzer** built using **Python**.  
This application captures live network packets, analyzes network protocols, detects high traffic, and generates a final analysis report.

---

## 🚀 Features

- Live network packet capturing  
- Supports **TCP, UDP, ICMP** protocols  
- Displays source & destination IP addresses and ports  
- High traffic detection with real-time warnings  
- Generates a final network analysis report  
- Easy-to-use **GUI application**  
- Can be converted into a standalone **Windows EXE**

---

## 🧠 Technologies Used

- Python 3  
- Scapy  
- Tkinter (GUI)  
- PyInstaller (for EXE build)  
- Git & GitHub  

---

## 📁 Project Structure


NetworkPacketAnalyzer/
├── analyzer/ # Packet analysis & report generation
├── capture/ # Packet capturing logic
├── gui/ # GUI application
├── main.py # Entry point
├── test_report.py # Testing script
└── README.md


---

## ▶️ How to Run (Using Python)

### 1️⃣ Install Dependencies

```bash
pip install scapy
2️⃣ Run the GUI Application
python -m gui.gui_app

⚠️ Important:
You must run Command Prompt as Administrator to allow packet capturing.
📊 Output
🔹 Live Packet Capture

🔹 High Traffic Warning

🔹 Final Network Analysis Report

🪟 Windows EXE (No Python Required)

You can run this application without installing Python by using the Windows executable.

🔽 Download EXE

Go to GitHub → Releases

Download gui_app.exe

Run it as Administrator

🎓 Use Cases

Computer Networks mini / final year project

Learning packet sniffing & protocol analysis

Understanding TCP, UDP, ICMP behavior

Introduction to cybersecurity & network monitoring

Building real-world GUI-based Python applications

👨‍💻 Author

Mohan
GitHub: https://github.com/Mohan-10-15

⚠️ Disclaimer

This project is strictly for educational and learning purposes.
Do NOT use this application on networks without proper authorization.
The author is not responsible for any misuse.

⭐ If you found this project helpful, consider giving it a star on GitHub!

