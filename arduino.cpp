#include <iostream>
#include <wiringPi.h>
using namespace std;

#define TRIGGER_PIN 0
#define ECHO_PIN 1
#define MOTOR_PIN 2
#define LED_PIN 3

void setup() {
  wiringPiSetup();
  pinMode(TRIGGER_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  pinMode(MOTOR_PIN, OUTPUT);
  pinMode(LED_PIN, OUTPUT);
}

long readUltrasonicDistance() {
  digitalWrite(TRIGGER_PIN, LOW);
  delay(2);
  digitalWrite(TRIGGER_PIN, HIGH);
  delay(10);
  digitalWrite(TRIGGER_PIN, LOW);
  while(digitalRead(ECHO_PIN) == LOW);
  long startTime = micros();
  while(digitalRead(ECHO_PIN) == HIGH);
  long travelTime = micros() - startTime;
  long distance = (travelTime / 2) / 29.1;
  return distance;
}

void controlTrashCan() {
  long distance = readUltrasonicDistance();
  if (distance < 10) {
    digitalWrite(MOTOR_PIN, HIGH);
    digitalWrite(LED_PIN, HIGH);
    delay(5000);
    digitalWrite(MOTOR_PIN, LOW);
    digitalWrite(LED_PIN, LOW);
  }
}

int main() {
  setup();
  while(true) {
    controlTrashCan();
    delay(1000);
  }
  return 0;
}
