import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
import joblib
import seaborn as sns

# -----------------------------
# 1. SIMULATE SENSOR DATA
# -----------------------------

np.random.seed(42)
samples = 1000

# Normal condition
normal_current = np.random.normal(5, 0.5, samples)
normal_temp = np.random.normal(40, 3, samples)
normal_vibration = np.random.normal(1, 0.2, samples)
normal_flow = np.random.normal(10, 1, samples)

# Fault condition
fault_current = np.random.normal(9, 1, samples)
fault_temp = np.random.normal(70, 5, samples)
fault_vibration = np.random.normal(4, 1, samples)
fault_flow = np.random.normal(3, 1, samples)

# Combine data
current = np.concatenate((normal_current, fault_current))
temperature = np.concatenate((normal_temp, fault_temp))
vibration = np.concatenate((normal_vibration, fault_vibration))
flow = np.concatenate((normal_flow, fault_flow))

# Labels (0 = Normal, 1 = Fault)
labels = np.array([0]*samples + [1]*samples)

# Create DataFrame
data = pd.DataFrame({
    'Current': current,
    'Temperature': temperature,
    'Vibration': vibration,
    'Flow': flow,
    'Status': labels
})

print("Dataset Preview:")
print(data.head())

# -----------------------------
# 2. TRAIN ML MODEL
# -----------------------------

X = data[['Current', 'Temperature', 'Vibration', 'Flow']]
y = data['Status']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

# -----------------------------
# 3. EVALUATION
# -----------------------------

y_pred = model.predict(X_test)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)

# Plot Confusion Matrix
plt.figure()
sns.heatmap(cm, annot=True, fmt='d')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.savefig("model_evaluation.png")
plt.show()

# -----------------------------
# 4. SAVE MODEL
# -----------------------------

joblib.dump(model, "pump_predictive_model.pkl")
print("\nModel saved as pump_predictive_model.pkl")
