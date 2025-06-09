#include <WiFi.h>
#include <HTTPClient.h>
#include <DHT.h>

#define DHTPIN 4
#define DHTTYPE DHT22
#define POTPIN 34

const char* ssid = "Wokwi-GUEST";
const char* password = "";
const char* serverUrl = "http://192.168.0.151:5001/coletar";

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  Serial.print("Conectando ao Wi-Fi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println(" Conectado!");
  dht.begin();
}

void loop() {
  float temperatura = dht.readTemperature();
  float umidade = dht.readHumidity();
  int vibracao = analogRead(POTPIN);

  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(serverUrl);
    http.addHeader("Content-Type", "application/json");

    Serial.print("🌡️ Temp: ");
    Serial.print(temperatura);
    Serial.print(" °C | 💧 Umid: ");
    Serial.print(umidade);
    Serial.print(" % | 📈 Vibração: ");
    Serial.println(vibracao);

    String json = "{\"temperatura\":" + String(temperatura, 2) +
                  ",\"umidade\":" + String(umidade, 2) +
                  ",\"vibracao\":" + String(vibracao) + "}";

    int resp = http.POST(json);
    Serial.print("POST -> ");
    Serial.println(resp);
    http.end();
  }

  delay(3000);
}
