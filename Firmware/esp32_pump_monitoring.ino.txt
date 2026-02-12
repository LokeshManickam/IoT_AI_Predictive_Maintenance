#include <WiFi.h>
#include <HTTPClient.h>
#include <DHT.h>

#define DHTPIN 4
#define DHTTYPE DHT22
#define CURRENT_SENSOR_PIN 34
#define VIBRATION_PIN 35
#define FLOW_SENSOR_PIN 27

DHT dht(DHTPIN, DHTTYPE);

const char* ssid = "YOUR_WIFI";
const char* password = "YOUR_PASSWORD";
const char* serverName = "http://your-server/api/data";

void setup() {
  Serial.begin(115200);
  dht.begin();
  
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting...");
  }
  Serial.println("WiFi Connected");
}

void loop() {

  float temperature = dht.readTemperature();
  int currentValue = analogRead(CURRENT_SENSOR_PIN);
  int vibrationValue = analogRead(VIBRATION_PIN);
  int flowValue = digitalRead(FLOW_SENSOR_PIN);

  Serial.println("---- Pump Data ----");
  Serial.println("Temp: " + String(temperature));
  Serial.println("Current: " + String(currentValue));
  Serial.println("Vibration: " + String(vibrationValue));
  Serial.println("Flow: " + String(flowValue));

  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(serverName);
    http.addHeader("Content-Type", "application/json");

    String jsonData = "{\"temperature\":" + String(temperature) +
                      ",\"current\":" + String(currentValue) +
                      ",\"vibration\":" + String(vibrationValue) +
                      ",\"flow\":" + String(flowValue) + "}";

    http.POST(jsonData);
    http.end();
  }

  delay(5000);
}
