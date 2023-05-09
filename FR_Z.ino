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
  if (data == 'u') {
    servo.write(93);
    Serial.println('left');
  }

  if (data == 'd') {
    servo.write(87);
    Serial.println('right');
  }

  if (data == 's'){
    servo.write(90);
    Serial.println('stop');
  }
}