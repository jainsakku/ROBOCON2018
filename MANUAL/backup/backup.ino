void setup() {
//  Serial.begin(9600);
  // put your setup code here, to run once:
  pinMode(12,INPUT);
  pinMode(11,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int r = pulseIn(12,HIGH);
//  Serial.println(r);
  if(r<1200)
    digitalWrite(11,LOW);
  else if(r>1800)
    digitalWrite(11,HIGH);
}
