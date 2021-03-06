#include <Servo.h>

Servo blocker;

int data = 0;
bool gateStatus = 1;
bool oldGateStatus = 1;
bool SecondGateStatus;
const int gatePin =12;
const int bulkFeederPin = 13;

const int blockerPin = 11;
const int blockerOpen = 90;
const int blockerClosed = 180;

const int pwm_m1 = 100;
const int pwm_m2 = 200;
const int pwm_m3 = 255;

char pyInput;
int blockerVal = 0;


// connect motor controller pins to Arduino digital pins
// motor one
const int enA = 3; // pwm port 
const int in1 = 4;
const int in2 = 2;

// motor two
const int enB = 5; // pwm port
const int in3 = 6;
const int in4 = 7;  

// motor three
const int enC = 10; // pwm port
const int in5 = 8;
const int in6 = 9;

int timer;

void setup() {
  // put your setup code here, to run once:

pinMode(blockerPin, OUTPUT);
blocker.attach(11);

Serial.begin(9600);
pinMode(gatePin, INPUT);     
digitalWrite(gatePin, HIGH); // turn on the pullup

 // set all the motor control pins to outputs
 pinMode(enA, OUTPUT);
 pinMode(in1, OUTPUT);
 pinMode(in2, OUTPUT);

 pinMode(enB, OUTPUT);
 pinMode(in3, OUTPUT);
 pinMode(in4, OUTPUT);


 pinMode(enC, OUTPUT);
 pinMode(in5, OUTPUT);
 pinMode(in6, OUTPUT);

 pinMode(bulkFeederPin, OUTPUT);


}

void loop() {
  // put your main code here, to run repeatedly:



if(Serial.available()>0){

  oldGateStatus = gateStatus;     //used for checking old gateStatus with the new one
  gateStatus = digitalRead(gatePin);
  pyInput = Serial.read();
    if(oldGateStatus == HIGH && gateStatus == LOW){ // compares if the lightgate switched from no bolt to bolt
      SecondGateStatus = HIGH;
      //Serial.println();

    }  
    // return the gate status when the light gate is broken, or was broken since the gate was closed
    if((pyInput == 'l' && gateStatus == LOW)||(pyInput == 'l' && SecondGateStatus == HIGH)){ 
      data = 1;
      SecondGateStatus = LOW;
      Serial.println(data);

    }
    else if(pyInput == 'l' && gateStatus == HIGH){ // return the gate status when the light gate is unbroken
      data = 2;
      Serial.println(data);
    }
    
    else if(pyInput == 'm'){ // forward motor 1
      data = 3;
      digitalWrite(in1, HIGH);
      digitalWrite(in2, LOW);
      analogWrite(enA, (pwm_m1));
      
      Serial.println(data);
    }
    else if(pyInput == 'n'){ // stop motor 1
      data = 4;
      digitalWrite(in1, LOW);
      digitalWrite(in2, LOW);
      
      Serial.println(data);
    }
    else if(pyInput == 'o'){ // reverse motor 1
      data = 5;     
      digitalWrite(in1, LOW);
      digitalWrite(in2, HIGH); 
      analogWrite(enA, pwm_m1);
      
      Serial.println(data);
    }
    
    else if(pyInput == 'r'){ // forward motor 2
      data = 6;
      digitalWrite(in3, HIGH);
      digitalWrite(in4, LOW);
      analogWrite(enB, pwm_m2);
      
      Serial.println(data);
    }
    else if(pyInput == 's'){ // stop motor 2
      data = 7;
      digitalWrite(in3, LOW);
      digitalWrite(in4, LOW);
      
      Serial.println(data);
    }
    else if(pyInput == 't'){ // reverse motor 2
      data = 8;     
      digitalWrite(in3, LOW);
      digitalWrite(in4, HIGH); 
      analogWrite(enB, pwm_m2);
      
      Serial.println(data);
    }

    else if(pyInput == 'u'){ // forward motor 3
      data = 9;
      digitalWrite(in5, HIGH);
      digitalWrite(in6, LOW);
      analogWrite(enC, pwm_m3);
      
      Serial.println(data);
    }
    else if(pyInput == 'v'){ // stop motor 3
      data = 10;
      digitalWrite(in5, LOW);
      digitalWrite(in6, LOW);
      
      Serial.println(data);
    }
    else if(pyInput == 'w'){ // reverse motor 3
      data = 11;     
      digitalWrite(in5, LOW);
      digitalWrite(in6, HIGH); 
      analogWrite(enC, pwm_m3);
      
      Serial.println(data);
      
    }
    else if(pyInput == 'q'){ // reverse motor 3
      data = 12;     
      digitalWrite(in1, LOW);
      digitalWrite(in2, LOW); 
      //analogWrite(enC, 0);
      digitalWrite(in3, LOW);
      digitalWrite(in4, LOW); 
      //analogWrite(enC, 0);
      digitalWrite(in5, LOW);
      digitalWrite(in6, LOW); 
      //analogWrite(enC, 0);
      
      Serial.println(data);
    }

    else if(pyInput == 'a'){ // start all
      data = 13;     
      digitalWrite(in1, HIGH);
      digitalWrite(in2, LOW); 
      analogWrite(enA, pwm_m1);
      digitalWrite(in3, HIGH);
      digitalWrite(in4, LOW); 
      analogWrite(enB, pwm_m2);
      digitalWrite(in5, HIGH);
      digitalWrite(in6, LOW); 
      analogWrite(enC, pwm_m3);
      
      Serial.println(data);
    }


else if(pyInput == 'x'){ // start bulkFeeder
      data = 14;     
      digitalWrite(bulkFeederPin, HIGH);
         
      Serial.println(data);
    }

else if(pyInput == 'y'){ // stop bulkFeeder
      data = 15;     
      digitalWrite(bulkFeederPin, LOW);
         
      Serial.println(data);
    }

else if(pyInput == 'e'){ // open blocker
      data = 16;     
      blocker.write(blockerOpen);
         
      Serial.println(data);
    }

else if(pyInput == 'f'){ // close blocker
      data = 17;     
      SecondGateStatus = 0;           // set signal to check for lightgate
      blocker.write(blockerClosed);
         
      Serial.println(data);
    }

}

}
