# 🔐 Lightweight Edge AI Model for IoT Network Traffic Classification and Threat Detection

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Edge AI](https://img.shields.io/badge/Edge-AI-informational.svg)]()
[![Made with Flask](https://img.shields.io/badge/Backend-Flask-blue.svg)](https://flask.palletsprojects.com/)
[![Platform](https://img.shields.io/badge/Platform-RaspberryPi-lightgrey.svg)]()

> A lightweight and privacy-preserving AI model for real-time **network traffic classification** and **threat detection (SQLi, XSS, DoS, etc.)**, optimized for **IoT Edge Devices** such as Raspberry Pi.

---

## 🧭 Table of Contents
- [🎯 Objectives](#-objectives)
- [🧠 System Architecture](#-system-architecture)
- [🛠️ Features](#-features)
- [📁 Folder Structure](#-folder-structure)
- [🚀 How to Run](#-how-to-run)
- [📊 Model Performance](#-model-performance)
- [📚 Dataset Sources](#-dataset-sources)
- [📌 Future Enhancements](#-future-enhancements)
- [🧑‍💻 Author](#-author)

---

## 🎯 Objectives

- Detect anomalous and malicious traffic at the edge (routers, Raspberry Pi, etc.)
- Handle encrypted traffic using statistical flow metadata
- Support attacks like **SQLi**, **XSS**, **Botnets**, **DoS**, etc.
- Deploy efficient, quantized ML models on constrained devices

---

## 🧠 System Architecture

> ⚙️ This system consists of 5 layers: **Capture**, **Feature Extraction**, **Inference Engine**, **Alert System**, and optional **Dashboard**.

---

## 🛠️ Features

- ✅ PCAP packet capture using `tcpdump` / `tshark`
- ✅ Feature extraction using `pyshark` (protocol, byte count, entropy, etc.)
- ✅ Model training with `Random Forest`, `Autoencoder`, `TFLite CNN`
- ✅ Real-time inference engine
- ✅ Detection of **SQLi** and **XSS** attacks
- ✅ Works offline on Edge Devices

---

## 📁 Folder Structure

```
EdgeAI_IoT_Traffic_Detection/
├── capture/               → Packet sniffing (tcpdump/tshark)
├── preprocessing/         → Flow feature extraction from PCAP
├── models/                → ML/DL model training and TFLite conversion
├── inference/             → Real-time prediction on edge
├── utils/                 → Evaluation metrics (accuracy, F1)
├── api/                   → Flask API for payload detection (SQLi/XSS)
├── data/                  → PCAP & CSV traffic data
├── model/                 → Saved .pkl / .tflite models
├── requirements.txt
└── main.py
```

---

## 🚀 How to Run

### 🧪 Install Requirements
```bash
pip install -r requirements.txt
```

### ▶️ Execute Pipeline
```bash
python main.py
```

### 🌐 Run Flask API for Payload Detection
```bash
cd api
python app.py
```

### 📬 Test SQLi/XSS Detection API
```bash
curl -X POST http://localhost:5000/predict \
     -H "Content-Type: application/json" \
     -d '{"payload": "SELECT * FROM users WHERE 1=1"}'
```

---

## 📊 Model Performance (Expected)

| Metric      | Value      |
|-------------|------------|
| Accuracy    | > 90%      |
| Latency     | < 100 ms   |
| RAM Usage   | < 200 MB   |
| CPU Usage   | < 40%      |

---

## 📚 Dataset Sources

- [UNSW-NB15](https://www.unsw.adfa.edu.au/unsw-canberra-cyber/cybersecurity/ADFA-NB15-Datasets/)
- [CICIDS 2017/2018](https://www.unb.ca/cic/datasets/ids.html)
- [TON_IoT Datasets](https://research.unsw.edu.au/projects/toniot-datasets)
- [ISCX VPN-nonVPN](https://www.unb.ca/cic/datasets/vpn.html)

---

## 📌 Future Enhancements

- ✅ Online Learning / Incremental training
- ✅ Federated Edge Training
- ✅ MQTT Gateway Integration
- ✅ SDN + OpenWRT support
- ✅ Add Deep Models (URLNet, RIDIT-CNN) with OpenVINO

---

## 🧑‍💻 Author

**Aruna Raj**  
📧 rajaru3112@gmail.com  
🔗  [LinkedIn](https://www.linkedin.com/in/aruna-raj-6b64a727b/)

---

## 📝 License

This project is licensed under the MIT License 
