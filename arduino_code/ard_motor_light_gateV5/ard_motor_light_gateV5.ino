#include <Servo.h>

Servo blocker;

int data = 0;
int gatePin =12;
int loaderPin = 11;
int blockerPin = A1;

const int pwm_m1 = 100;
const int pwm_m2 = 200;
const int pwm_m3 = 255;

char pyInput;
int blockerVal = 0;

bool gateStatus; 

// connect motor controller pins to Arduino digital pins
// motor one
const int enA = 3; // pwm port 
const int in1 = 4;
const int in2 = 2;

// motor two
const int enB = 5; // pwm port
const int in3 = 7;
const int in4 = 6;  

// motor three
const int enC = 10; // pwm port
const int in5 = 9;
const int in6 = 8;

int timer;

void setup() {
  // put your setup code here, to run once:

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

 pinMode(loaderPin, OUTPUT);
 pinMode(blockerPin, OUTPUT);


}

void loop() {
  // put your main code here, to run repeatedly:



if(Serial.available()>0){


  gateStatus = digitalRead(gatePin);
  pyInput = Serial.read();
  

    if(pyInput == 'l' && gateStatus == LOW){ // return the gate status
      data = 1;
      Serial.println(data);

    }
    else if(pyInput == 'l' && gateStatus == HIGH){ // return the gate status
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


else if(pyInput == 'x'){ // start loader
      data = 14;     
      digitalWrite(loaderPin, HIGH);
         
      Serial.println(data);
    }

else if(pyInput == 'y'){ // stop loader
      data = 15;     
      digitalWrite(loaderPin, LOW);
         
      Serial.println(data);
    }

else if(pyInput == 'e'){ // open blocker
      data = 16;     
      blocker.write(0);
         
      Serial.println(data);
    }

else if(pyInput == 'f'){ // close blocker
      data = 17;     
      blocker.write(180);
         
      Serial.println(data);
    }

}

}
