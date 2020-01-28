/* Sweep
 by BARRAGAN <http://barraganstudio.com>
 This example code is in the public domain.

 modified 8 Nov 2013
 by Scott Fitzgerald
 http://www.arduino.cc/en/Tutorial/Sweep
*/

#include <Servo.h>

Servo myservo; 
Servo bin// create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position
int onoff_signal = 6;// 
int = binSignal = 2;

int i = 0;
int j = 0;

void setup() {
  pinMode(onoff_signal, INPUT);
  pinMode(binSignal, INPUT);
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
  bin.attach(10);

  Serial.begin(9600);
}

void loop() {
Serial.println(digitalRead(onoff_signal));
if (digitalRead(onoff_signal) == HIGH){
    if (i <= 160){
        Serial.println(i);
        myservo.write(i);              // tell servo to go to position in variable 'pos'
        delay(60);                       // waits 15ms for the servo to reach the position
        i += 1;
        j += 1;
        if (i == 160){
            i = 0;
        }
    }
    if (j >= 160){
        Serial.println(j - i);
        myservo.write(j - i);              // tell servo to go to position in variable 'pos'
        delay(10);                       // waits 15ms for the servo to reach the position
        if ((j - i)<= 0 )
            j = 0;
            i = 0;
            delay(1000);
         }
    }
}