#include <Arduino.h>
#line 1 "C:\\Users\\benpo\\OneDrive - mail.tau.ac.il\\לימודים\\סמסטר ב\\חשיפה לחומרה\\3 - FR\\FR\\FR.ino"
int data;

int led = 10;
void setup() 
{ 
  Serial.begin(9600);  
  digitalWrite (LED_BUILTIN, LOW); //initially set to low
  Serial.println("This is my First Example.");
}
 
void loop() 
{
while (Serial.available())
  {
    data = Serial.read();
  }

  if (data == '1')
  digitalWrite (led, HIGH);

  else if (data == '0')
  digitalWrite (led, LOW);

}
