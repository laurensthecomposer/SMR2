#include <Servo.h>

Servo blocker;

int data = 0;
int gatePin =12;
int loaderPin = 11;
int blockerPin = A1;
char pyInput;
int pwm = 200;
int blockerVal = 0;

bool gateStatus; 

// connect motor controller pins to Arduino digital pins
// motor one
int enA = 3; // pwm port 
int in1 = 4;
int in2 = 2;

int pmwM1_diff = 100; 

// motor two
int enB = 5; // pwm port
int in3 = 7;
int in4 = 6;

// motor three
int enC = 10; // pwm port
int in5 = 9;
int in6 = 8;

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
  

    if(pyInput == 'l' && gateStatus == LOW){
      data = 1;
      Serial.println(data);

    }
    else if(pyInput == 'l' && gateStatus == HIGH){
      data = 2;
      Serial.println(data);
    }
    
    else if(pyInput == 'm'){ // forward motor 1
      data = 3;
      digitalWrite(in1, HIGH);
      digitalWrite(in2, LOW);
      analogWrite(enA, (pwm-pmwM1_diff));
      
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
      analogWrite(enA, pwm);
      
      Serial.println(data);
    }
    
    else if(pyInput == 'r'){ // forward motor 2
      data = 6;
      digitalWrite(in3, HIGH);
      digitalWrite(in4, LOW);
      analogWrite(enB, pwm);
      
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
      analogWrite(enB, pwm);
      
      Serial.println(data);
    }

    else if(pyInput == 'u'){ // forward motor 3
      data = 9;
      digitalWrite(in5, HIGH);
      digitalWrite(in6, LOW);
      analogWrite(enC, pwm-75);
      
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
      analogWrite(enC, pwm);
      
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
      analogWrite(enA, (pwm-pmwM1_diff));
      digitalWrite(in3, HIGH);
      digitalWrite(in4, LOW); 
      analogWrite(enB, pwm);
      digitalWrite(in5, HIGH);
      digitalWrite(in6, LOW); 
      analogWrite(enC, pwm);
      
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
