/*
  Writes to :-
 Up-Down motor
 Down Servo
 
 Reads from :-
 Up-Down switches
 Laser Receiver
 Up ultrasonic sensor
 Down ultrasonic sensor
 
 Talks with :-
 Rasberry PI
 RF Module
 */

// libraries
#include <NewPing.h>
#include <Servo.h>
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

// constants
const byte address[6] = "00001";
boolean received = true, downValue = false; // down-going value here true=HIGH false=LOW
Servo myservo;
Servo smallServo;
#define MAX_DISTANCE 200               // Maximum distance (in cm) to ping.
#define SONAR_NUM 2                    // Number of sensors.
#define PINGDELAY 30

// pins
int dswitch = A6, tswitch = A7;        // up-down switch
int dir = 4, pwm = 3;                  // up-down motor
int laser[]={ 
  A1 ,A2,A3 };                                                // Receiver input
int servo = 6, servo2 = 5;                      // Servo pins
RF24 radio(10, 9);                     // CE, CSN
NewPing sonar[SONAR_NUM] = {           // Sensor object array.
  NewPing(7, 8, MAX_DISTANCE),         // Each sensor's trigger pin, echo pin, and max distance to ping.
  NewPing(5, 2, MAX_DISTANCE),
};

// variables
const int s1 = 200, s2 = 55, s3 = -20, s4 = 150, s5 = 90, sms1 = 35, sms2 = 110; // Servo variables
int count = 0, tCount = 10, dl = 270;  // Count and releasing delay
int d0 = 15, d1 = 15;                  // Ultrasonic distances
int upSpeed = 255, downSpeed = 140;    // motor speed
int acc = 0,sp=50;
boolean state = false;
int maxi[]={
  350,350,350};
int mini[]={
  100,100,100};

void setup()
{
  // define pins
  pinMode(dir, OUTPUT);
  pinMode(pwm, OUTPUT);
  pinMode(dswitch, INPUT_PULLUP);
  pinMode(tswitch, INPUT_PULLUP);
  // Initialize
  Serial.begin(9600);
  Serial.println();
  radio.begin();  
  radio.openWritingPipe(address);
  radio.setPALevel(RF24_PA_MIN);
  radio.stopListening();

  myservo.attach(servo);
  smallServo.attach(servo2);
  openServo();
}

void openServo()
{
  Serial.println("Open");
  const char text = 'o';
  radio.write(&text, sizeof(text));
}

void closeServo()
{
  Serial.println("Clos");
  const char text = 'g';
  radio.write(&text, sizeof(text));
}

void openSmallServo()
{
  //  Serial.print("Small open : ");
  //  Serial.println(sms1);
  smallServo.write(sms1);
}

void closeSmallServo()
{
  //  Serial.print("Small close : ");
  //  Serial.println(sms2);
  smallServo.write(sms2);
}

boolean calibrate()
{
  int l[3];
  unsigned long t = millis();
  int timer = 0;
  while(1)
  {
    for( int i =0 ; i<3 ; i++)
    {
      l[i] = analogRead(laser[i]);
    }
    for (int i=0;i<3 ; i++)
    {
      if (l[i] < mini[i])
      {
        mini[i]=l[i];
      }
      else if (l[i]>=maxi[i]) 
        maxi[i]=l[i];
    }
    if (((millis()-t) / 1000)==timer)
    {
      Serial.println(timer);
      timer++;
    }
    if(millis()-t >5000)
      break;
  }
  for ( int i=0 ; i<3 ; i++)
  {
    mini[i]=mini[i]+100;
    maxi[i]=maxi[i]-100;
  }
  return true;
}

boolean rackPick()
{
  Serial.println("Rack");

  openSmallServo();
  openServo();
  // go down
  digitalWrite(dir, downValue);
  analogWrite(pwm, downSpeed);
  while (!downSwitch());
  analogWrite(pwm, 0);

  // middle to rack
  int pos = s2;
  int a = 1;
  myservo.write(s1);
  delay(400);

  // rack to middle
  a = 2;
  for (pos = (s1); pos > s4;)
  {
    myservo.write(pos);
    delay(sp);
    pos -= a;
    a += acc;
  }
  closeSmallServo();
  delay(200);
    //go up
  digitalWrite(dir, !downValue);
  analogWrite(pwm, upSpeed);
  while (!upSwitch());
  analogWrite(pwm, upSpeed);

  //ball to middle
  pos = s4;
  a = 0;
  acc = 1;
  sp = 150;
  for (pos = s4; pos >= (s5);)
  {
    myservo.write(pos);
    delay(sp);
    pos -= a;
    a += acc;
  }
  for (pos = s5; pos >= (s3);)
  {
    myservo.write(pos);
    delay(sp);
    pos -= a;
    a -= acc;
    if(a<=0)
    {
      a=3;
      sp=50;
    }
  }
  acc=0;
  sp=50;
  myservo.write(s3);
  delay(100);

  closeServo();
  delay(1000);
  openSmallServo();
  delay(100);
  // arm to middle
  analogWrite(pwm, 0);
  myservo.write(s5);
  delay(100);
  return true;
}

boolean armLoad()
{
  Serial.println("Load");

  //   go up
  digitalWrite(dir, !downValue);
  analogWrite(pwm, upSpeed);
  while (!upSwitch());
  analogWrite(pwm, upSpeed);
  openServo();
  //
  //  // middle to arm
  int pos = s2;
  int a = 2;
  for (pos = s2; pos >= (s3);)
  {
    myservo.write(pos);
    delay(sp);
    pos -= a;
    a += acc;
  }
  myservo.write(s3);
  // grab
  //delay(1000);
  closeServo();
  delay(1000);
  openSmallServo();
  delay(100);
  // arm to middle
  analogWrite(pwm, 0);
  myservo.write(s5);
  delay(100);
  return true;
}

boolean countLoops(int t)
{
  Serial.println("Loop");
  count = 0;
  received = true;
//  Serial.println(mini[t-1]);
//  Serial.println(maxi[t-1]);
//  Serial.println(laser[t-1]);
  while (1)
  {
    int r;
    r= analogRead(laser[t-1]);
    //Serial.println(r);
    if (!received && r < mini[t-1])
    {
      received = true;
    }
    else if (received && r >maxi[t-1])
    {
      received = false;
      count++;
      //      Serial.print("count : ");
      Serial.println(count);
    }


    if (count == tCount)
    {
      delay(dl);
      openServo();
      return true;
    }
  }
}

boolean upSwitch()
{
  int r = analogRead(tswitch);
  if (r < 100)
    return false;
  else if (r > 900)
    return true;
  else
    return false;
}

boolean downSwitch()
{
  int r = analogRead(dswitch);
  if (r < 100)
    return false;
  else if (r > 900)
    return true;
  else
    return false;
}

boolean test()
{
  openServo();
  digitalWrite(dir, downValue);
  analogWrite(pwm, downSpeed);
  while (!downSwitch());
  analogWrite(pwm, 0);

  myservo.write(s1);
  delay(1000);

  openSmallServo();
  delay(1000);
  myservo.write(s2);
  delay(1000);

  digitalWrite(dir, !downValue);
  analogWrite(pwm, upSpeed);
  while (!upSwitch());
  analogWrite(pwm, 0);

  myservo.write(s3);
  delay(1000);

  closeSmallServo();
  delay(1000);

  myservo.write(s2);
  delay(1000);

  for (int i = 0; i < 5; i++)
  {
    Serial.print("Receiver 1 : ");
    Serial.println(analogRead(laser[0]));
    Serial.print("Receiver 2 : ");
    Serial.println(analogRead(laser[1]));
    Serial.print("Receiver 3 : ");
    Serial.println(analogRead(laser[2]));
    Serial.print("Up Switch : ");
    Serial.println(analogRead(tswitch));
    Serial.print("Down Switch : ");
    Serial.println(analogRead(dswitch));
    Serial.print("Up Sonic : ");
    Serial.println(sonar[0].ping_cm());
    delay(PINGDELAY);
    Serial.print("Down Sonic : ");
    Serial.println(sonar[1].ping_cm());
    Serial.println();
    delay(PINGDELAY);
  }
  return true;
}

void loop()
{
  if (Serial.available() > 0)
  {
    char input = Serial.read();
    state = false;
    Serial.println("Okay");

    if (input == 's')
      state = rackPick();
    else if (input == 'c')
      state = armLoad();
    else if (input == 't')
      state = countLoops(1);
    else if (input == 'u')
      state = countLoops(2);
    else if (input == 'v')
      state = countLoops(3);
    else if (input == 'q')
      state = test();
    else if (input == 'x')
      state = calibrate();
    else if (input == 'o')
      openServo();    
    else if (input == 'g')
      closeServo();
    Serial.println(state ? "TRUE" : "FALS");
  }
  //  if(!state)
  //  state = rackPick();
  //  state = armLoad();
  //  state = countLoops(1);
  //  state = test();
  // state = calibrate();
  // state = countLoops(1);
  //  Serial.println(state ? "TRUE" : "FALS");
}


