/* Sweep
 by BARRAGAN <http://barraganstudio.com>
 This example code is in the public domain.

 modified 8 Nov 2013
 by Scott Fitzgerald
 http://www.arduino.cc/en/Tutorial/Sweep
*/

#include <Servo.h>

Servo myservo; 
int z;
int pos = 0;    // variable to store the servo position
int onoff_signal = 6;// 

int i = 0;
int j = 0;

void setup() {
  pinMode(onoff_signal, INPUT);
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
  myservo.write(i);
  Serial.begin(9600);
}

void loop() {
Serial.println(digitalRead(onoff_signal));
 if (digitalRead(onoff_signal) == HIGH){
    if (j >= 160){
        i += 1;
        Serial.println(j - i);
        myservo.write(j - i);              // tell servo to go to position in variable 'pos'
        delay(10);                       // waits 15ms for the servo to reach the position
        if ((j - i)<= 0 ){
            j = 0;
            i = 0;
            delay(1000);
         }
    }
    else if (i <= 160){
        Serial.println(i);
        myservo.write(i);              // tell servo to go to position in variable 'pos'
        delay(60);                       // waits 15ms for the servo to reach the position
        i += 1;
        j += 1;
        if (i == 160){
            i = 0;
        }
    }
  }
}
