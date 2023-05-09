#include <Servo.h>

Servo servo;

char data;

void setup() 
{ 
  Serial.begin(9600);  
  servo.attach(7);
}
 
void loop() 
{
  data = Serial.read();
  if (data == 'l') {
    servo.write(96);
    Serial.println('left');
  }

  if (data == 'r') {
    servo.write(82);
    Serial.println('right');
  }

  if (data == 's'){
    servo.write(90);
    Serial.println('stop');
  }
}