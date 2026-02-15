import joblib
import numpy as np

model = joblib.load("pump_model.pkl")

def predict_pump_status(temp, current, vibration, voltage):

    input_data = np.array([[temp, current, vibration, voltage]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        return "Pump Failure Likely"
    else:
        return "Pump Healthy"
