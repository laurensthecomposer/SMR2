

int data = 0;
int gatePin =4;
char pyInput;

bool gateStatus; 

// connect motor controller pins to Arduino digital pins
// motor one
int enA = 10;
int in1 = 9;
int in2 = 8;

void setup() {
  // put your setup code here, to run once:

Serial.begin(9600);
pinMode(gatePin, INPUT);     
digitalWrite(gatePin, HIGH); // turn on the pullup

 // set all the motor control pins to outputs
 pinMode(enA, OUTPUT);
 pinMode(in1, OUTPUT);
 pinMode(in2, OUTPUT);



}

void loop() {
  // put your main code here, to run repeatedly:



if(Serial.available()>0){


  gateStatus = digitalRead(gatePin);
  pyInput = Serial.read();
  

    // send gate status
    if(pyInput == 'l' && gateStatus == LOW){ 

      data = 1;
      //digitalWrite(ledPin, LOW);
      Serial.println(data);

    }


    else if(pyInput == 'l' && gateStatus == HIGH){

      data = 2;
      //digitalWrite(ledPin, HIGH);
      Serial.println(data);

    }
      
     else if(pyInput == 'f'){ // start motor forward

      data = 3;
      digitalWrite(in1, HIGH);
      digitalWrite(in2, LOW);
      analogWrite(enA, 200);
      Serial.println(data);
      
      //delay(3000);

      
    }


    else if(pyInput == 's'){ // stop motor

      data = 4;
      digitalWrite(in1, LOW);
      digitalWrite(in2, LOW);
      
      Serial.println(data);
      
      //delay(3000);

      
    }


    else if(pyInput == 'r'){ // start motor backwards

      data = 5;     
      digitalWrite(in1, LOW);
      digitalWrite(in2, HIGH); 
      analogWrite(enA, 200);
      Serial.println(data);
      
      //delay(3000);

      
    }

    }

}
