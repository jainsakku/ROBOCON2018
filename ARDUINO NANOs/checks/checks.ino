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
int laser[]={ A2 ,A0 ,A3 ,A1 };                                                // Receiver input
int servo = 6, servo2 = 5;                      // Servo pins
RF24 radio(10, 9);                     // CE, CSN
NewPing sonar[SONAR_NUM] = {           // Sensor object array.
  NewPing(7, 8, MAX_DISTANCE),         // Each sensor's trigger pin, echo pin, and max distance to ping.
  NewPing(5, 2, MAX_DISTANCE),
};

// variables
const int s1 = 200, s2 = 55, s3 = -20, s4 = 150, s5 = 90, sms1 = 35, sms2 = 120, sp = 50, acc = 0; // Servo variables
int count = 0, tCount = 10, dl = 270;  // Count and releasing delay
int d0 = 15, d1 = 15;                  // Ultrasonic distances
int upSpeed = 255, downSpeed = 140;    // motor speed
boolean state = false;
int maxi[]={0,0,0};
int mini[]={1000,1000,1000};

void setup()
{
// define pins
  pinMode(dir,OUTPUT);
  pinMode(pwm,OUTPUT);
  pinMode(dswitch,INPUT_PULLUP);
  pinMode(tswitch,INPUT_PULLUP);
 
// Initialize
  Serial.begin(9600);

  radio.begin();  radio.openWritingPipe(address);
  radio.setPALevel(RF24_PA_MIN);
  radio.stopListening();

  myservo.attach(servo);

// initial calls
  openServo();

  digitalWrite(dir,downValue);
  analogWrite(pwm,downSpeed);
  delay(1000);
  digitalWrite(dir,!downValue);
  analogWrite(pwm,upSpeed);
  delay(1000);
  analogWrite(pwm,0);
  myservo.write(0);
  delay(1000);
  myservo.write(180);
  delay(1000);
}

void openServo()
{
  Serial.println("openServo");
  const char text = 'o';
  radio.write(&text, sizeof(text));
}

void loop() 
{
    Serial.print("Receiver 1 : ");
    Serial.println(analogRead(laser[0]));
    Serial.print("Receiver 2 : ");
    Serial.println(analogRead(laser[1]));
    Serial.print("Receiver 3 : ");
    Serial.println(analogRead(laser[2]));
    Serial.print("Receiver 4 : ");
    Serial.println(analogRead(laser[3]));
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
//    Serial.print("A0 : ");
//    Serial.println(analogRead(A0));
//    Serial.print("A1 : ");
//    Serial.println(analogRead(A1));
//    Serial.print("A2 : ");
//    Serial.println(analogRead(A2));
//    Serial.print("A3 : ");
//    Serial.println(analogRead(A3));
//    Serial.print("A4 : ");
//    Serial.println(analogRead(A4));
//    Serial.print("A5 : ");
//    Serial.println(analogRead(A5));
//    Serial.print("A6 : ");
//    Serial.println(analogRead(A6));
//    Serial.print("A7 : ");
//    Serial.println(analogRead(A7));
//    Serial.println();
    delay(1000);
}
