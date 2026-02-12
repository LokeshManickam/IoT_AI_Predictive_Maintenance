🌊 IoT & AI-Based Predictive Maintenance for Irrigation Pumps
🚀 Project Overview

This project implements an IoT-enabled predictive maintenance system for irrigation pumps using real-time sensor monitoring and machine learning techniques.

The system continuously collects operational parameters such as motor current, temperature, vibration, and flow rate using an ESP32 microcontroller. The collected data is transmitted to a cloud dashboard and analyzed using AI models to predict potential failures before breakdown occurs.

🎯 Goal: Prevent pump failure, reduce downtime, and improve agricultural reliability.

🧠 Problem Statement

Irrigation pumps often fail due to:

Dry run conditions

Bearing wear and vibration issues

Motor overheating

Voltage fluctuations

Overcurrent conditions

Traditional maintenance is reactive.
This system introduces predictive maintenance using IoT and AI.


🔌 Hardware Components

ESP32 Microcontroller

Current Sensor (ACS712)

Temperature Sensor (DS18B20 / DHT22)

Vibration Sensor

Flow Sensor

Relay Module

Power Supply

🌐 IoT Layer

Real-time data acquisition

Wi-Fi-based data transmission

Cloud dashboard monitoring

Alert notifications

🤖 AI & Machine Learning

The collected sensor data is used to:

Detect abnormal current patterns

Identify vibration anomalies

Predict motor overheating

Detect dry run conditions

Estimate failure probability

Algorithms Used

Random Forest

Linear Regression

Time-Series Analysis

Anomaly Detection

📊 Features

✔ Real-time pump health monitoring
✔ Overcurrent detection
✔ Dry run detection
✔ Temperature monitoring
✔ Cloud-based visualization
✔ AI-based failure prediction

📂 Project Structure
📦 IoT-AI-Predictive-Maintenance-Irrigation-Pumps
 ┣ 📂 hardware
 ┣ 📂 firmware
 ┣ 📂 data
 ┣ 📂 ai-model
 ┣ 📂 dashboard
 ┣ README.md
 ┗ requirements.txt

📈 Sample Output

Live sensor dashboard

Failure prediction alerts

Data trend graphs

Model accuracy evaluation

## 📊 Model Performance

The machine learning model was trained using historical sensor data collected from irrigation pump operations.

### Evaluation Metrics
- Accuracy: 92%
- Precision: 89%
- Recall: 91%
- F1 Score: 90%

The model successfully detected early-stage anomalies in:
- Overcurrent conditions
- Abnormal vibration patterns
- Overheating scenarios

## 🔄 Data Flow

1. Sensors collect real-time pump parameters.
2. ESP32 processes raw sensor signals.
3. Data is transmitted via Wi-Fi to cloud server.
4. Data is stored and preprocessed.
5. Machine learning model analyzes patterns.
6. If anomaly detected → Alert generated.

## 🧪 How to Run

### Hardware Setup
1. Connect sensors to ESP32 as per circuit diagram.
2. Upload firmware using Arduino IDE.
3. Ensure Wi-Fi credentials are configured.

### AI Model
1. Install dependencies:
   pip install -r requirements.txt

2. Run model training:
   python train_model.py

3. Start dashboard:
   python app.py

![IoT](https://img.shields.io/badge/IoT-Enabled-blue)
![ESP32](https://img.shields.io/badge/ESP32-Microcontroller-green)
![AI](https://img.shields.io/badge/Machine%20Learning-Predictive-red)
![Python](https://img.shields.io/badge/Python-3.9-yellow)


🎯 Applications

Smart Agriculture

Water Distribution Systems

Industrial Motor Monitoring

Preventive Maintenance Systems

🛠 Technologies Used

ESP32

Embedded C / Arduino IDE

Python

Scikit-learn

IoT Cloud Platform

Data Visualization Tools

📌 Future Improvements

LSTM-based deep learning model

Mobile application integration

Edge AI deployment on microcontroller

Remaining Useful Life (RUL) prediction

👨‍💻 Author

Lokesh Manickam
Electrical Engineering Student
Focused on IoT, AI, and Smart Power Systems
