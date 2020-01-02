const int ledPin = 13;
char input='0';

void setup() 
{
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
  digitalWrite(ledPin,HIGH);
  delay(1000);
  digitalWrite(ledPin,LOW);
  delay(1000);
  Serial.println();
}

void loop() 
{
  if (Serial.available())
  {
    input = Serial.read();
//    light(input - '0');
    if(input=='s')
    {
      Serial.println("T");
    }
  }
  delay(500);
}

void light(int n)
{
    for(int i=0;i<n;i++)
  {
    digitalWrite(ledPin,HIGH);
    delay(1000);
    digitalWrite(ledPin,LOW);
    delay(1000);
  }
}
