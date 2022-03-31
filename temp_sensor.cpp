#include "DHT.h"

#define DHTPIN 2
#define DHTTYPE DHT11

int buttonPin = 10; 
int btnState = 0;
DHT dht(DHTPIN, DHTTYPE);

void setup()
{   
    Serial.begin(9600);
    dht.begin();
}

void loop()
{   
    btnState = digitalRead(buttonPin);
    int h = dht.readHumidity();
    int t = dht.readTemperature(0);

    Serial.print(h);
    Serial.print(";");
    Serial.print(t);
    Serial.println();
    delay(5000); 
}