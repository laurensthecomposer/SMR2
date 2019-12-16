

int data = 0;
int gatePin =4;
char pyInput;

bool gateStatus; 

// connect motor controller pins to Arduino digital pins
// motor one
int enA = 10; // pwm port
int in1 = 9;
int in2 = 8;

// motor two
int enB = 5; // pwm port
int in3 = 7;
int in4 = 6;

// motor three
int enC = 3; // pwm port
int in5 = 2;
int in6 = 4;

int timer;

void setup() {
  // put your setup code here, to run once:

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
      analogWrite(enA, 200);
      
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
      analogWrite(enA, 200);
      
      Serial.println(data);
    }
    
    else if(pyInput == 'r'){ // forward motor 2
      data = 3;
      digitalWrite(in3, HIGH);
      digitalWrite(in4, LOW);
      analogWrite(enB, 120);
      
      Serial.println(data);
    }
    else if(pyInput == 's'){ // stop motor 2
      data = 4;
      digitalWrite(in3, LOW);
      digitalWrite(in4, LOW);
      
      Serial.println(data);
    }
    else if(pyInput == 't'){ // reverse motor 2
      data = 5;     
      digitalWrite(in3, LOW);
      digitalWrite(in4, HIGH); 
      analogWrite(enB, 120);
      
      Serial.println(data);
    }

    else if(pyInput == 'u'){ // forward motor 3
      data = 3;
      digitalWrite(in3, HIGH);
      digitalWrite(in4, LOW);
      analogWrite(enB, 255);
      
      Serial.println(data);
    }
    else if(pyInput == 'v'){ // stop motor 3
      data = 4;
      digitalWrite(in3, LOW);
      digitalWrite(in4, LOW);
      
      Serial.println(data);
    }
    else if(pyInput == 'w'){ // reverse motor 3
      data = 5;     
      digitalWrite(in3, LOW);
      digitalWrite(in4, HIGH); 
      analogWrite(enB, 255);
      
      Serial.println(data);
    }
}

}
