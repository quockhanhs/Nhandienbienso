#include <Servo.h>
Servo servo;

int servo_pin = D1;

void setup() {
  Serial.begin(9600);
  servo.attach(servo_pin);
  servo.write(0);
}

unsigned long old_time_run_servo = millis();
unsigned long time_interval = 5000;

void loop() {
  if (millis() - old_time_run_servo > time_interval) {
    servo.write(0);
  }
  if (Serial.available()) {
    char c = Serial.read();
    servo.write(90);
    old_time_run_servo = millis();
  }
}
