#include <WiFi.h>
#include <HTTPClient.h>
#include "DHT.h"

#define DHTPIN 4
#define DHTTYPE DHT22

#define CURRENT_SENSOR 34
#define VIBRATION_SENSOR 35
#define VOLTAGE_SENSOR 32

const char* ssid = "YOUR_WIFI";
const char* password = "YOUR_PASSWORD";
const char* serverName = "http://YOUR_PC_IP:5000/predict";

DHT dht(DHTPIN, DHTTYPE);

void connectWiFi() {
  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nConnected!");
}

void setup() {
  Serial.begin(115200);
  dht.begin();
  connectWiFi();
}

void loop() {

  if (WiFi.status() != WL_CONNECTED) {
    connectWiFi();
  }

  float temperature = dht.readTemperature();
  float current = analogRead(CURRENT_SENSOR);
  float vibration = analogRead(VIBRATION_SENSOR);
  float voltage = analogRead(VOLTAGE_SENSOR);

  if (isnan(temperature)) {
    Serial.println("Failed to read DHT sensor!");
    return;
  }

  HTTPClient http;
  http.begin(serverName);
  http.addHeader("Content-Type", "application/json");

  String jsonData = "{";
  jsonData += "\"temperature\":" + String(temperature) + ",";
  jsonData += "\"current\":" + String(current) + ",";
  jsonData += "\"vibration\":" + String(vibration) + ",";
  jsonData += "\"voltage\":" + String(voltage);
  jsonData += "}";

  int httpResponseCode = http.POST(jsonData);

  Serial.print("Response Code: ");
  Serial.println(httpResponseCode);

  http.end();

  delay(5000);
}
