//Motor Driver
#define enA 9 //PWM 
#define in1 6 //IN1
#define in2 7 //IN2

//Servo
#define s1 9
#define s2 10

//Ultrasonic
#define echoPin 5
#define trigPin 6
long duration;
int distance;

#include <Servo.h>

Servo lockDispense;
Servo lockReturn;


void setup() {
  pinMode(enA, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  // Set initial rotation direction
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  analogWrite(enA, 100); // Send PWM signal to L298N Enable pin (0-255)

  lockDispense.attach(s1);
  lockReturn.attach(s2);  

  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input
  Serial.begin(9600); // Starts the serial communication
   
}


void loop() {
  char srx, received;

  while(Serial.available()>0){
    srx = Serial.read();
    if(srx == 'd' || srx == 'r'){
      received = srx;
    }else{
      received = 'x';
    }
    Serial.println(received);
  }

  if(received=='d'){
  //dispenseUmbrella();
    delay(1000);
    dispenseLock();
    delay(1000);
    dispenseUnlock();
    delay(1000);
    returnLock();
    delay(1000);
    returnUnlock();
    delay(1000);
  }
  
  if(received=='r'){
    checkUltrasonic();
  }
  received='x';    
}

void dispenseUmbrella(){
  //calibrate duration for dispensing
  for(int i=0; i<1000; i++){
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
    delay(20);
  }
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  delay(20);
}

//Servo Value 0-180

void dispenseLock(){
  lockDispense.write(180);
  delay(15);
}

void dispenseUnlock(){
  lockDispense.write(0);
  delay(15);
}

void returnLock(){
  lockReturn.write(180);
  delay(15);
}

void returnUnlock(){
  lockReturn.write(0);
  delay(15);
}

void checkUltrasonic(){
    // Clears the trigPin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  // Calculating the distance
  distance = duration * 0.034 / 2;
  // Prints the distance on the Serial Monitor
  Serial.print("Distance (cm): ");
  Serial.println(distance);
}