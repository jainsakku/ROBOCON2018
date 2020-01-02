/*
 >^/M1 (FL)       \^< M2 (FR)
   ----------------
  |                |
  |                |
  |                |
  |                |
  |                |
   ----------------
 <^\M3 (BL)       /^> M4 (BR)
 left - ACW <
 right - CW >
 */

#include <SPI.h>
#include <PS3BT.h>

USB Usb;
BTD Btd(&Usb);
PS3BT PS3(&Btd);

int x1, x2, y1, y2, p1, p2, p3, p4, s, vec;
int m11 = 9; //FL
int m12 = 1;
int m21 = 5; //FR
int m22 = 4;
int m31 = 6; //BL
int m32 = 7;
int m41 = 10; //BR
int m42 = 0;
int m51 = 14;
int m52 = 3;
int s1 = 255;
int s2 = 255;
int s3 = 255;
int s4 = 255;


void setup() {

   //Serial.begin(115200);

  //Serial.print(F("\r\nPS3 Bluetooth Library Started"));
  pinMode(m11, OUTPUT);
  pinMode(m21, OUTPUT);
  pinMode(m31, OUTPUT);
  pinMode(m41, OUTPUT);
  pinMode(m51, OUTPUT);
  pinMode(m12, OUTPUT);
  pinMode(m22, OUTPUT);
  pinMode(m32, OUTPUT);
  pinMode(m42, OUTPUT);
  pinMode(m52, OUTPUT);
  analogWrite(m11, 0);
  analogWrite(m21, 0);
  analogWrite(m31, 0);
  analogWrite(m41, 0);
  digitalWrite(m52, LOW);
 

   if (Usb.Init() == -1) 
   {
     //Serial.print(F("\r\nOSC did not start"));
     while (1); //halt
   }
}

void loop() 
{
  Usb.Task();
  if (PS3.PS3Connected || PS3.PS3NavigationConnected) {
    
    // Analog button values can be read from almost all buttons
    if (PS3.getAnalogButton(L2) > 0 || PS3.getAnalogButton(R2) > 0)
    {
      int l2 = PS3.getAnalogButton(L2);
      int r2 = PS3.getAnalogButton(R2);
      //Serial.print(F("\r\nL2: "));
      //Serial.print(l2);
      //Serial.print(F("\r\nR2: "));
      //Serial.print(r2);

      if(l2 > 0)
      {
        digitalWrite(m51,HIGH);
        digitalWrite(m52,HIGH);
      }
      if(r2 > 0)
      {
        digitalWrite(m51,HIGH);
        digitalWrite(m52,LOW);
      }
    }
    else
    {
        digitalWrite(m51,LOW);
    }
    //Taking Analog input from joystick
    x1 =  map(PS3.getAnalogHat(LeftHatX), 0, 255, -122, 123);
    y1 =  map(PS3.getAnalogHat(LeftHatY), 0, 255, -122, 123);
    x2 =  map(PS3.getAnalogHat(RightHatX), 0, 255, -122, 123);
    //Projections on motor lines
    s = sqrt(2);
    p1 = -x1+y1/s;
    p2 = x1+y1/s;
    p3 = x1-y1/s;
    p4 = x1+y1/s;
    //Printing all values
    //Serial.println(x1);
    //Serial.println(y1);
    //Serial.println(x2);
    //Serial.println(p1);
    //Serial.println(p2);
    //Serial.println(p3);
    //Serial.println(p4); 
  if (x2 == 0) {
    if (p1>0) {
      //Serial.println("I");
      p1 = map(p1, 0, 173, 0, s1);
      analogWrite(m11, p1);
      digitalWrite(m12, LOW);
    }
    else {
      //Serial.println("II");
      p1 = map(p1, -173, 0, s1, 0);
      analogWrite(m11, p1);
      digitalWrite(m12, HIGH);
    }
    if (p2>0) {
      //Serial.println("III");
      p2 = map(p2, 0, 173, 0, s2);
      analogWrite(m21, p2);
      digitalWrite(m22, LOW);
    }
    else {
      //Serial.println("IV");
      p2 = map(p2, -173, 0, s2, 0);
      analogWrite(m21, p2);
      digitalWrite(m22, HIGH);
    }
    if (p3>0) {
      //Serial.println("V");
      p3 = map(p3, 0, 173, 0, s3);
      analogWrite(m31, p3);
      digitalWrite(m32, LOW);
    }
    else {
      //Serial.println("VI");
      p3 = map(p3, -173, 0, s3, 0);
      analogWrite(m31, p3);
      digitalWrite(m32, HIGH);
    }
    if (p4>0) {
      //Serial.println("VII");
      p4 = map(p4, 0, 173, 0, s4);
      analogWrite(m41, p4);
      digitalWrite(m42, LOW);
    }
    else {
      //Serial.println("VIII");
      p4 = map(p4, -173, 0, s4, 0);
      analogWrite(m41, p4);
      digitalWrite(m42, HIGH);
    }
  }

  else {
  if (x2>0) { //CW turn
    vec = map(x2, 0, 123, 0, 150);
    analogWrite(m11, vec);
    analogWrite(m21, vec);
    analogWrite(m31, vec);
    analogWrite(m41, vec);
    digitalWrite(m12, HIGH);
    digitalWrite(m22, LOW);
    digitalWrite(m32, HIGH);
    digitalWrite(m42, HIGH);   
  }
  else { //ACW turn
    vec = map(x2, -122, 0, 150, 0);
    analogWrite(m11, vec);
    analogWrite(m21, vec);
    analogWrite(m31, vec);
    analogWrite(m41, vec);
    digitalWrite(m12, LOW);
    digitalWrite(m22, HIGH);
    digitalWrite(m32, LOW);
    digitalWrite(m42, LOW); 
  }
  }

  if (PS3.getButtonClick(UP)) {

    //Serial.print(F("\r\nUp"));

     if (PS3.PS3Connected) {
      PS3.setLedOff();
      PS3.setLedOn(LED1);
    }

  }

}

  //Serial.println("------------"); 
}
