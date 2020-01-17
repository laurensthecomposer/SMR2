

int data = 0;
int gatePin =4;
char pyInput;

bool gateStatus; 

// connect motor controller pins to Arduino digital pins
// motor one
int enA = 3; // pwm port 
int in1 = 4;
int in2 = 2;



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


  
  data = 3;
    
  digitalWrite(in5, HIGH);
  digitalWrite(in6, LOW);
  for(int i = 150; i <= 255 && i >= 0; i+=5){
    
  
    analogWrite(enC, i);
    Serial.println(i);
    delay(3000);
  }
}
