

int data = 0;
int gatePin =4;
char pyInput;

bool gateStatus; 

// connect motor controller pins to Arduino digital pins
// motor one
int enA = 10;
int in1 = 9;
int in2 = 8;

int enB = 5;
int in3 = 7;
int in4 = 6;
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
    else if(pyInput == 'f'){
      data = 3;
      digitalWrite(in1, HIGH);
      digitalWrite(in2, LOW);
      analogWrite(enA, 50);
      
      Serial.println(data);
    }
    else if(pyInput == 's'){
      data = 4;
      digitalWrite(in1, LOW);
      digitalWrite(in2, LOW);
      
      Serial.println(data);
    }
    else if(pyInput == 'r'){
      data = 5;     
      digitalWrite(in1, LOW);
      digitalWrite(in2, HIGH); 
      analogWrite(enA, 200);
      
      Serial.println(data);
    }
     else if(pyInput == 'F'){
      data = 3;
      digitalWrite(in1, HIGH);
      digitalWrite(in2, LOW);
      analogWrite(enA, 200);
      
      Serial.println(data);
    }
    else if(pyInput == 'S'){
      data = 4;
      digitalWrite(in1, LOW);
      digitalWrite(in2, LOW);
      
      Serial.println(data);
    }
    else if(pyInput == 'R'){
      data = 5;     
      digitalWrite(in1, LOW);
      digitalWrite(in2, HIGH); 
      analogWrite(enA, 200);
      
      Serial.println(data);
    }
}

}
