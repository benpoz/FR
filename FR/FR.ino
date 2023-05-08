char data;

int led = 5;
void setup() 
{ 
  Serial.begin(9600);  
  digitalWrite (led, LOW); //initially set to low
  Serial.println("This is my First Example.");
}
 
void loop() 
{
// while (Serial.available())
//   {
//     data = Serial.read();
//   }
  data = Serial.read();
  if (data == '1') {
    digitalWrite (led, HIGH);
    digitalWrite (LED_BUILTIN, HIGH);
  }


  if (data == '0') {
    digitalWrite (led, LOW);
    digitalWrite (LED_BUILTIN, LOW);
  }

}