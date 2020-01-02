    /*
    * Arduino Wireless Communication Tutorial
    *     Example 1 - Transmitter Code
    *                
    * by Dejan Nedelkovski, www.HowToMechatronics.com
    * 
    * Library: TMRh20/RF24, https://github.com/tmrh20/RF24/
    */
    #include <SPI.h>
    #include <nRF24L01.h>
    #include <RF24.h>
    RF24 radio(9,10); // CE, CSN
    const byte address[6] = "00001";
    const char text='g';
    const char text2='o';
    void setup() 
    {
      Serial.begin(9600);
      radio.begin();
      radio.openWritingPipe(address);
      radio.setPALevel(RF24_PA_MAX);
      radio.stopListening();
      radio.printDetails();
     // radio.setChannel(10);
    }
    void loop() 
    {
      radio.write(&text, sizeof(text));
      delay(2000);
      Serial.println("sent");
      radio.write(&text2, sizeof(text2));
      delay(2000);
    }
