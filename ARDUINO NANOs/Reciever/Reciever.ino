    /*
    * Arduino Wireless Communication Tutorial
    *       Example 1 - Receiver Code
    *                
    * by Dejan Nedelkovski, www.HowToMechatronics.com
    * 
    * Library: TMRh20/RF24, https://github.com/tmrh20/RF24/
    */
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
#include<Servo.h>
Servo myservo;
char text;
int flag=1;
RF24 radio(9, 10); // CE, CSN
const byte address[6] = "00001";
void setup() 
{
//  Serial.begin(9600);
  radio.begin();
  radio.openReadingPipe(0, address);
  radio.setPALevel(RF24_PA_MAX);
  radio.startListening();
  pinMode(3,OUTPUT);
  digitalWrite(3,LOW);
  myservo.attach(6);
  myservo.write(180);
  delay(2000);
  myservo.write(90);
}

void loop() 
{
  if (radio.available()) 
  {
    radio.read(&text, sizeof(text));
    if (text=='g')
    {
      myservo.write(50);
      delay(3000);
      myservo.write(70);
      digitalWrite(3,HIGH);
    }
    else if(text=='o')
    {
      myservo.write(180);
      delay(1000);
      myservo.write(90);
      digitalWrite(3,LOW);
    }
  }
}
