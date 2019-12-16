

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


  
  data = 3;
    
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
  for(int i = 80; i <= 255 && i >= 0; i+=5){
    
  
    analogWrite(enB, i);
    Serial.println(i);
    delay(3000);
  }
}
