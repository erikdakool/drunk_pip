#include <Arduino.h>

unsigned int val = 0;
unsigned int PIN = 0;
unsigned intNumber = 1023;

void setup() {
    Serial.begin(9600);
}

void loop() {
    val = analogRead(A0);
    if(val > 735 && val < 800){
        float bac = val * 0.015 - 1.1125;
        Serial.print(bac,3);
    }else if(val > 800){
        float bac = val * 0.0053-4.687;
        Serial.print(bac,3);
    }
    Serial.print(val);
    Serial.print("\n");
    delay(1000);
}