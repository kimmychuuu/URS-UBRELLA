#include <Servo.h>

// Motor Driver
#define enA 10 // PWM
#define in1 9  // IN1
#define in2 8  // IN2

// Servo
#define servo1 12
#define servo2 13

// Ultrasonic
#define trigPin1 2
#define echoPin1 3

#define trigPin2 4
#define echoPin2 5

#define trigPin3 6
#define echoPin3 7

#define trigPin4 A0
#define echoPin4 A1

Servo servo1;
Servo servo2;

// Variables to control the motor and servos
bool motorRunning = false;
bool servo1Moving = false;
bool servo2Moving = false;
unsigned long servo1StartTime = 0;
unsigned long motorStartTime = 0;
int dispense = 0;

int currentCommand = 1;

void setup() {
  // Motor Driver Setup
  pinMode(enA, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  analogWrite(enA, 0); 

  // Servo Setup
  servo1.attach(servo1);
  servo2.attach(servo2);

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
    int distance = readUltrasonicSensor(trigPin1, echoPin1);
    Serial.println(distance);
    currentCommand = -1;
  }

  else if(currentCommand == 1){
    int distance = readUltrasonicSensor(trigPin2, echoPin2);
    Serial.println(distance);
    currentCommand = -1;
  }

  else if(currentCommand == 2){
    int distance = readUltrasonicSensor(trigPin3, echoPin3);
    Serial.println(distance);
    currentCommand = -1;
  }

  else if(currentCommand == 3){
    int distance = readUltrasonicSensor(trigPin4, echoPin4);
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

int readUltrasonicSensor(int trigPin, int echoPin) {
  /*
  * Get distance from specific ultrasonic sensor
  */
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  long duration = pulseIn(echoPin, HIGH);

  int distance = duration * 0.034 / 2;

  return distance;
}
