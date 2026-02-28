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
```bash
pip install scapy
