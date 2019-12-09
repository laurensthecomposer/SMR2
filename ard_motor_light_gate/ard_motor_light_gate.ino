

int data = 0;
int ledPin = 13;
int relayPin = 5;
int gatePin =4;
char pyInput;

bool gateStatus; 
bool motorStatus;

void setup() {
  // put your setup code here, to run once:

Serial.begin(9600);
pinMode(ledPin, OUTPUT);
pinMode(relayPin, OUTPUT);
pinMode(gatePin, INPUT);     
digitalWrite(gatePin, HIGH); // turn on the pullu


}

void loop() {
  // put your main code here, to run repeatedly:

gateStatus = digitalRead(gatePin);

if(Serial.available()>0){

  pyInput = Serial.read();
  

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
      
     else if(pyInput == 'r'){

      data = 3;
      digitalWrite(ledPin, HIGH);
      digitalWrite(relayPin, HIGH);
      Serial.println(data);
      
      //delay(3000);

      
    }


    else if(pyInput == 's'){

      data = 4;
      digitalWrite(ledPin, LOW);
      digitalWrite(relayPin, LOW);
      Serial.println(data);
      
      //delay(3000);

      
    }

    }

}
