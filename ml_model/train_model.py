import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
import joblib
import seaborn as sns

# -----------------------------
# 1. SIMULATE SENSOR DATA
# -----------------------------

np.random.seed(42)
samples = 1000

# Slightly overlapping distributions (more realistic)
normal_current = np.random.normal(6, 0.8, samples)
fault_current = np.random.normal(8, 1.2, samples)

normal_temp = np.random.normal(45, 5, samples)
fault_temp = np.random.normal(65, 7, samples)

normal_vibration = np.random.normal(1.5, 0.5, samples)
fault_vibration = np.random.normal(3.5, 1, samples)

normal_flow = np.random.normal(9, 2, samples)
fault_flow = np.random.normal(4, 2, samples)

# Combine
current = np.concatenate((normal_current, fault_current))
temperature = np.concatenate((normal_temp, fault_temp))
vibration = np.concatenate((normal_vibration, fault_vibration))
flow = np.concatenate((normal_flow, fault_flow))

labels = np.array([0]*samples + [1]*samples)

data = pd.DataFrame({
    'Current': current,
    'Temperature': temperature,
    'Vibration': vibration,
    'Flow': flow,
    'Status': labels
})

print("Dataset Shape:", data.shape)
print(data.head())

# -----------------------------
# 2. TRAIN MODEL
# -----------------------------

X = data[['Current', 'Temperature', 'Vibration', 'Flow']]
y = data['Status']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(
    n_estimators=150,
    max_depth=8,
    random_state=42
)

model.fit(X_train, y_train)

# -----------------------------
# 3. EVALUATION
# -----------------------------

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)

plt.figure()
sns.heatmap(cm, annot=True, fmt='d')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.savefig("model_evaluation.png")
plt.close()

# -----------------------------
# 4. FEATURE IMPORTANCE
# -----------------------------

importance = model.feature_importances_
features = X.columns

plt.figure()
sns.barplot(x=importance, y=features)
plt.title("Feature Importance")
plt.xlabel("Importance Score")
plt.savefig("feature_importance.png")
plt.close()

# -----------------------------
# 5. SAVE MODEL
# -----------------------------

joblib.dump(model, "pump_predictive_model.pkl")
print("\nModel saved as pump_predictive_model.pkl")
