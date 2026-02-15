from flask import Flask, request, jsonify
from ml_model.predict import predict_pump_status

app = Flask(__name__)

latest_data = {}

@app.route('/predict', methods=['POST'])
def predict():

    global latest_data

    data = request.json

    temp = data['temperature']
    current = data['current']
    vibration = data['vibration']
    voltage = data['voltage']

    status = predict_pump_status(temp, current, vibration, voltage)

    latest_data = {
        "temperature": temp,
        "current": current,
        "vibration": vibration,
        "voltage": voltage,
        "status": status
    }

    print("Pump Status:", status)

    return jsonify({"status": status})


@app.route('/latest', methods=['GET'])
def get_latest():
    return jsonify(latest_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
