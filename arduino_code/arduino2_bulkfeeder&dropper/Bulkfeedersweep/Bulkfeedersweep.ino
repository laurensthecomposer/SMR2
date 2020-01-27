/* Sweep
 by BARRAGAN <http://barraganstudio.com>
 This example code is in the public domain.

 modified 8 Nov 2013
 by Scott Fitzgerald
 http://www.arduino.cc/en/Tutorial/Sweep
*/

#include <Servo.h>

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position
int onoff_signal = 6;// 



void setup() {
  pinMode(onoff_signal, INPUT);
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object

  Serial.begin(9600);
}

void loop() {
Serial.println(digitalRead(onoff_signal));
if (digitalRead(onoff_signal) == HIGH){
  for (pos = 0; pos <= 160; pos++) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    Serial.println(pos);
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(60);                       // waits 15ms for the servo to reach the position
    }
  for (pos = 160; pos >= 0; pos--) { // goes from 180 degrees to 0 degrees
    
    Serial.println(pos);
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(10);                       // waits 15ms for the servo to reach the position
    }
  delay(1000);
  }
}
