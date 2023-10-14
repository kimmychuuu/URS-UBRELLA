#include <Servo.h>

// Motor Driver
#define enA 10 // PWM
#define in1 9  // IN1
#define in2 8  // IN2

// Servo
#define s1 12
#define s2 13

// Ultrasonic
#define trigPin1 2
#define echoPin1 3
long duration1;
int distance1;
int dispense = 0;

#define trigPin2 4
#define echoPin2 5
long duration2;
int distance2;

#define trigPin3 6
#define echoPin3 7
long duration3;
int distance3;

#define trigPin4 A0
#define echoPin4 A1
long duration4;
int distance4;

Servo servo1;
Servo servo2;

// Variables to control the motor and servos
bool motorRunning = false;
bool servo1Moving = false;
bool servo2Moving = false;
unsigned long servo1StartTime = 0;
unsigned long motorStartTime = 0;

enum SystemState {
  IDLE,   // Default state
  RUNNING_R, // System is executing 'r' command
  RUNNING_D  // System is executing 'd' command
};

SystemState currentState = IDLE;

void setup() {
  // Motor Driver Setup
  pinMode(enA, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  analogWrite(enA, 0); // Set PWM to 0 initially

  // Servo Setup
  servo1.attach(s1);
  servo2.attach(s2);

  // Ultrasonic sensor setup
  pinMode(trigPin1, OUTPUT);
  pinMode(echoPin1, INPUT);
  pinMode(trigPin2, OUTPUT);
  pinMode(echoPin2, INPUT);
  pinMode(trigPin3, OUTPUT);
  pinMode(echoPin3, INPUT);
  pinMode(trigPin4, OUTPUT);
  pinMode(echoPin4, INPUT);

  Serial.begin(9600); // Starts the serial communication
  
}

void loop() {
  char srx;
	
  
  if (Serial.available() > 0) {
    srx = Serial.read();
    if (srx == 'd') {
      // Handle 'd' input
	dispense = 1;
      startMotor();


    } else if (srx == 'r') {
      // Handle 'r' input
     

      moveServo1(100);
      delay(10000);
      moveServo1(0);


    }
  }
  distance1 = readUltrasonicSensor(trigPin1, echoPin1);
  distance2 = readUltrasonicSensor(trigPin2, echoPin2);
  distance3 = readUltrasonicSensor(trigPin3, echoPin3);
  distance4 = readUltrasonicSensor(trigPin4, echoPin4);

  Serial.print("Distance 1: ");
  Serial.print(distance1);
  Serial.print(" cm\t");

  Serial.print("Distance 2: ");
  Serial.print(distance2);
  Serial.println(" cm");
  Serial.print("Distance 3: ");
  Serial.print(distance3);
  Serial.print(" cm\t");

  Serial.print("Distance 4: ");
  Serial.print(distance4);
  Serial.println(" cm");
  
  if (distance1 < 30) {
    startMotor();
  }

  if (distance2 < 30) {
    stopMotor();
  }
  
  if (distance3 < 30 && dispense == 1) {
    moveServo2(100);
    dispense=0;
    delay(3000);
  } else {
    moveServo2(0);
  }

  if (distance4 < 30) {
    stopMotor();
  }
  delay(1000);
  // Other code for your project goes here...
}

void startMotor() {
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  analogWrite(enA, 255); // Start the DC motor at full speed
}

void stopMotor() {
  analogWrite(enA, 0); // Stop the DC motor
}

void moveServo1(int angle) {
  servo1.write(angle);
}

void moveServo2(int angle) {
  servo2.write(angle);
}

int readUltrasonicSensor(int trigPin, int echoPin) {
  // Send a pulse to the trigger pin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Read the duration of the pulse on the echo pin
  duration1 = pulseIn(echoPin, HIGH);

  // Calculate the distance based on the speed of sound
  int distance = duration1 * 0.034 / 2; // Divide by 2 for one-way distance

  return distance;
}