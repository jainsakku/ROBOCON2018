/*
  >^/M1 (FL)       \^< M2 (FR)
   ----------------
  |                |
  |                |
  |                |
  |                |
  |                |
   ----------------
  >v\M4 (BL)       /v< M3 (BR)
  left - ACW <
  right - CW >
*/

#include <SPI.h>
#include <PS3BT.h>
#include <Servo.h>

int pins[] = {A3, A0, A1, A2};
int m11 = 9; //FL
int m12 = A5;
int m21 = 6; //FR
int m22 = 7;
int m31 = 5; //BL
int m32 = 4;
int m41 = 10; //BR
int m42 = A4;
int spd = 255;
int pwm[] = {spd, spd, spd, spd};
boolean flag[4];
int count[4];
const int sizee = 390;
boolean vals[sizee][4];
void setup()
{
  Serial.begin(9600);
  Serial.print("start");
  pinMode(m11, OUTPUT);
  pinMode(m21, OUTPUT);
  pinMode(m31, OUTPUT);
  pinMode(m41, OUTPUT);
  pinMode(m12, OUTPUT);
  pinMode(m22, OUTPUT);
  pinMode(m32, OUTPUT);
  pinMode(m42, OUTPUT);
  analogWrite(m11, 0);
  analogWrite(m21, 0);
  analogWrite(m31, 0);
  analogWrite(m41, 0);
  pinMode(pins[0], INPUT);
  pinMode(pins[1], INPUT);
  pinMode(pins[2], INPUT);
  pinMode(pins[3], INPUT);

  analogWrite(m11, pwm[0]);
  analogWrite(m21, pwm[1]);
  analogWrite(m31, pwm[2]);
  analogWrite(m41, pwm[3]);
}

void loop()
{
  for (int i = 0; i < 4; i++)
  {
    flag[i] = LOW;
    count[i] = 0;
  }
  for (int i = 0; i < sizee; i++)
  {
    for (int j = 0; j < 4; j++)
    {
      vals[i][j] = digitalRead(pins[j]);
    }

  }

  for (int i = 0; i < sizee; i++)
  {
    for (int j = 0; j < 4; j++)
    {
      if (vals[i][j] != flag[j])
      {
        if (vals[i][j] == HIGH)
        {
          flag[j] = HIGH;
          count[j]++;
        }
        else
        {
          flag[j] = LOW;
        }
      }
    }
  }

  for (int i = 0; i < 4; i++)
  {
    Serial.print(count[i]);
    Serial.print("\t");
  }
  Serial.println(" ");
  Serial.println("-------------");
  delay(1000);
}

