#include <Servo.h>

// Motor Driver
const int enA = 10; // PWM
const int in1 = 9; // IN1
const int in2 = 8; // IN2

// Servo
const int servoPin1  = 12;
const int servoPin2  = 13;

// Ultrasonic
const int trigPin1 = 2;
const int echoPin1 = 3;

const int trigPin2 = 4;
const int echoPin2 = 5;

const int trigPin3 = 6;
const int echoPin3 = 7;

const int trigPin4 = A0;
const int echoPin4 = A1;

Servo servo1;
Servo servo2;

int currentCommand = -1;

void setup() {
  // Motor Driver Setup
  pinMode(enA, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  analogWrite(enA, 0); 

  // Servo Setup
  servo1.attach(servoPin1);
  servo2.attach(servoPin2);

  // Ultrasonic sensor setup
  pinMode(trigPin1, OUTPUT);
  pinMode(echoPin1, INPUT);
  pinMode(trigPin2, OUTPUT);
  pinMode(echoPin2, INPUT);
  pinMode(trigPin3, OUTPUT);
  pinMode(echoPin3, INPUT);
  pinMode(trigPin4, OUTPUT);
  pinMode(echoPin4, INPUT);

  // Starts the serial communication
  Serial.begin(9600); 
  
}

void loop() { 
  if(currentCommand == -1){
    receiveCommand();
    currentCommand = -1;
  }

  else if(currentCommand == 0){
    float distance = readUltrasonicSensor(trigPin1, echoPin1);
    Serial.println(distance);
    currentCommand = -1;
  }

  else if(currentCommand == 1){
    float distance = readUltrasonicSensor(trigPin2, echoPin2);
    Serial.println(distance);
    currentCommand = -1;
  }

  else if(currentCommand == 2){
    float distance = readUltrasonicSensor(trigPin3, echoPin3);
    Serial.println(distance);
    currentCommand = -1;
  }

  else if(currentCommand == 3){
    float distance = readUltrasonicSensor(trigPin4, echoPin4);
    Serial.println(distance);
    currentCommand = -1;
  }

  else if(currentCommand == 4){
    startMotor();
    currentCommand = -1;
  }

  else if(currentCommand == 5){
    stopMotor();
    currentCommand = -1;
  }

  else if(currentCommand == 6){
    moveDispensingServo(100); 
    currentCommand = -1;
  }

  else if(currentCommand == 7){
    moveDispensingServo(0);
    currentCommand = -1;
  }

  else if(currentCommand == 8){
    moveReturningServo(100);
    currentCommand = -1;
  }
  
  else if(currentCommand == 9){
    moveReturningServo(0);
    currentCommand = -1;
  }
}

void receiveCommand(){
  /* 
   * Get and return command from Raspberry Pi
   */
  if(Serial.available()){
    int sent = Serial.readStringUntil('\n').toInt();
    Serial.println("ok");
    currentCommand = sent;
  }
}

void startMotor() {
  /*
  * Start DC Motor at full speed
  */
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  analogWrite(enA, 255); 
}

void stopMotor() {
  /*
  * Stop DC Motor
  */
  analogWrite(enA, 0);
}

void moveDispensingServo(int angle) {
  /*
  * Move servo to specific angle
  */
  servo1.write(angle);
}

void moveReturningServo(int angle) {
  /*
  * Move servo to specific angle
  */
  servo2.write(angle);
}

float readUltrasonicSensor(int trigPin, int echoPin) {
  /*
  * Get distance from specific ultrasonic sensor
  */
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  float duration = pulseIn(echoPin, HIGH);

  float distance = duration * 0.034 / 2;

  return distance;
}