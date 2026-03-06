#include "DHT.h"

#define DHTPIN 32 //GPIO32
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

const int potPin = 27; //GPIO27
const int btnPin = 13; //GPIO13

int potValue = 0; // starting value
float voltage;
bool logging = false;

void setup() {
  Serial.begin(115200);
  pinMode(btnPin, INPUT);
  dht.begin();
}

void loop() {
  if (digitalRead(btnPin) == HIGH) // pressed button
  {
    logging = true;
  }

  if (logging){
    float h = dht.readHumidity();
    float t = dht.readTemperature();

    // Check if any reads failed and exit early (to try again).
    if (isnan(h) || isnan(t)) {
    Serial.println("Failed to read from DHT sensor!");
    delay(1000);
    return;
    }

    // Compute heat index in Celsius (isFahreheit = false)
  float hic = dht.computeHeatIndex(t, h, false);

    // Use potentiometer to simulate changes in voltage
    potValue = analogRead(potPin); // 0-4095
    voltage = potValue * (3.3 / 4095.0);

    // Print results in CSV friendly format
    Serial.print(millis()); // time
    Serial.print(",");
    Serial.print(voltage);
    Serial.print(",");
    Serial.print(h); // humidity
    Serial.print(","); 
    Serial.print(t); // temperature
    Serial.print(",");
    Serial.println(hic); // heat index
      
    delay(1000);
    }
  else{
      Serial.println("Press button to start readings.");
      delay(1000);
  }
}