/*
  >^/M1 (FL)       \^< M2 (FR)
   ----------------
  |                |
  |                |
  |                |
  |                |
  |                |
   ----------------
  <^\M4 (BL)       /^> M3 (BR)
  left - ACW <
  right - CW >
*/

int x1, x2, y1, y2, p1, p2, p3, p4, s, vec;
int m11 = 6; //FL
int m12 = 7;
int m21 = 10; //FR
int m22 = 12;
int m31 = 9; //BL
int m32 = 13;
int m41 = 5; //BR
int m42 = 4;
int m51 = 11;
int m52 = 8;
int s1 = 200;
int s2 = 200;
int s3 = 200;
int s4 = 200;
int c1 = A2, c2 = A3, c3 = A1, c4 = A0; //Channels ()
int v1 = 0, v2 = 0, v3 = 0, v4 = 0;

void setup()
{
  Serial.begin(115200);
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
  pinMode(c1, INPUT);
  pinMode(c2, INPUT);
  pinMode(c3, INPUT);
  pinMode(c4, INPUT);
  analogWrite(m11, 0);
  analogWrite(m21, 0);
  analogWrite(m31, 0);
  analogWrite(m41, 0);
  analogWrite(m51, 0);

  delay(1000);
  analogWrite(m11, 200);
  digitalWrite(m12,HIGH);
  delay(1000);
  analogWrite(m11, 0);
  digitalWrite(m12,HIGH);
  delay(1000);
  analogWrite(m11, 200);
  digitalWrite(m12,LOW);
  delay(1000);
  analogWrite(m11, 0);
  digitalWrite(m12,LOW);

  delay(1000);
  analogWrite(m21, 200);
  digitalWrite(m22,HIGH);
  delay(1000);
  analogWrite(m21, 0);
  digitalWrite(m22,HIGH);
  delay(1000);
  analogWrite(m21, 200);
  digitalWrite(m22,LOW);
  delay(1000);
  analogWrite(m21, 0);
  digitalWrite(m22,LOW);

  delay(1000);
  analogWrite(m31, 200);
  digitalWrite(m32,HIGH);
  delay(1000);
  analogWrite(m31, 0);
  digitalWrite(m32,HIGH);
  delay(1000);
  analogWrite(m31, 200);
  digitalWrite(m32,LOW);
  delay(1000);
  analogWrite(m31, 0);
  digitalWrite(m32,LOW);

  delay(1000);
  analogWrite(m41, 200);
  digitalWrite(m42,HIGH);
  delay(1000);
  analogWrite(m41, 0);
  digitalWrite(m42,HIGH);
  delay(1000);
  analogWrite(m41, 200);
  digitalWrite(m42,LOW);
  delay(1000);
  analogWrite(m41, 0);
  digitalWrite(m42,LOW);

  delay(1000);
//  analogWrite(m51, 200);
//  digitalWrite(m52,HIGH);
//  delay(1000);
//  analogWrite(m51, 0);
//  digitalWrite(m52,HIGH);
//  delay(1000);
//  analogWrite(m51, 200);
//  digitalWrite(m52,LOW);
//  delay(1000);
//  analogWrite(m51, 0);
//  digitalWrite(m52,LOW);
  digitalWrite(m51, HIGH);
  digitalWrite(m52, LOW);
  delay(1000);
  digitalWrite(m51, LOW);
  digitalWrite(m52, LOW);
  delay(1000);
  digitalWrite(m51, LOW);
  digitalWrite(m52, HIGH);
  delay(1000);
  digitalWrite(m51, LOW);
  digitalWrite(m52, LOW);
}

void loop()
{
}
