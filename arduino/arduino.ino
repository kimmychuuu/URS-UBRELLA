#include <Servo.h>


// Motor Driver
#define enA A5 // PWM
#define in1 9  // IN1
#define in2 10  // IN2

//buzzer
#define buzzer 7

// Servo
#define servoPin1 12
#define servoPin2 13

// Ultrasonic
#define trigPin1 2
#define echoPin1 3

#define trigPin2 4
#define echoPin2 5

#define trigPin3 A0
#define echoPin3 A1

#define trigPin4 A2
#define echoPin4 A3

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

  //buzzer
  pinMode(buzzer, OUTPUT);

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
    moveReturningServo(0); 
    currentCommand = -1;
  }

  else if(currentCommand == 7){
    moveReturningServo2(90);
    currentCommand = -1;
  }

  else if(currentCommand == 8){
    moveDispensingServo(0);
    currentCommand = -1;
  }
  
  else if(currentCommand == 9){
    moveDispensingServo2(90);
    currentCommand = -1;
  }
  else if(currentCommand ==10){
    tone();
    currentCommand =-1;
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
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  analogWrite(enA, 130); 
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
  servo1.write(35);
}

void moveDispensingServo2(int angle) {
  /*
  * Move servo to specific angle
  */
  servo1.write(90);
}

void moveReturningServo(int angle) {
  /*
  * Move servo to specific angle
  */
  servo2.write(0);
}

void moveReturningServo2(int angle) {
  /*
  * Move servo to specific angle
  */
  servo2.write(180);
}


void tone (){
  /*
   * buzzer sounds
   */
   tone(buzzer,3000);
   delay(1000);
   noTone(buzzer);
   delay(1000);
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

  long duration = pulseIn(echoPin, HIGH);

  float distance = duration * 0.034 / 2;

  return distance;

}