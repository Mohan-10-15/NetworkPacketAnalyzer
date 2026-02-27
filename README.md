# Network Packet Analyzer 🕵️‍♂️📡

A GUI-based Network Packet Analyzer built using Python.  
This project captures live network packets, analyzes protocols, detects high traffic, and generates a final analysis report.

---

## 🚀 Features
- Live packet capturing
- Supports TCP, UDP, ICMP protocols
- Source & destination IP and port analysis
- High traffic detection with warnings
- Final network analysis report
- GUI-based application (easy to use)
- Can be converted into a standalone Windows EXE

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
│
├── analyzer/ # Packet analysis & report generation
├── capture/ # Packet capturing logic
├── gui/ # GUI application
├── main.py # Entry point
├── test_report.py # Testing script
└── README.md


---

## ▶️ How to Run (Using Python)

### 1️⃣ Install dependencies
```bash
pip install scapy
2️⃣ Run the GUI
python -m gui.gui_app

⚠️ Run Command Prompt as Administrator (required for packet capture)

🪟 Windows EXE (No Python Needed)

You can download the ready-to-use Windows EXE from the Releases section.

➡️ Go to Releases → Download gui_app.exe

📊 Output

Live packet details shown in GUI

High traffic warnings displayed in real-time

Final analysis report generated after capture

🎓 Use Cases

Computer Networks mini / final year project

Learning packet analysis & network monitoring

Cybersecurity fundamentals practice

👨‍💻 Author

Mohan
GitHub: https://github.com/Mohan-10-15

⚠️ Disclaimer

This project is for educational purposes only.


### 4️⃣ Save the file  
Close Notepad

---

# ✅ STEP 3: Add README.md to GitHub

Open **Command Prompt** in your project folder and run:

```bat
git status

You should see:

README.md

Now add it:

git add README.md

Commit it:

git commit -m "Add professional README"

Push to GitHub:

git push