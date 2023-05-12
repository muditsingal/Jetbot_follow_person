int motor1pin1 = 2;
int motor1pin2 = 4;
int motor1pwm = 3;

int motor2pin1 = 6;
int motor2pin2 = 7;
int motor2pwm = 5;

void setup() {
  pinMode(motor1pin1, OUTPUT);
  pinMode(motor1pin2, OUTPUT);
  pinMode(motor2pin1, OUTPUT);
  pinMode(motor2pin2, OUTPUT);
  pinMode(motor1pwm, OUTPUT); 
  pinMode(motor2pwm, OUTPUT);
}

void loop() {
    digitalWrite(motor1pin1, HIGH);
    digitalWrite(motor1pin2, LOW);
    analogWrite(motor1pwm,200);
  
    digitalWrite(motor2pin1, HIGH);
    digitalWrite(motor2pin2, LOW);
    analogWrite(motor2pwm,200);

    delay(2000);

    digitalWrite(motor1pin1, LOW);
    digitalWrite(motor1pin2, HIGH);
    analogWrite(motor1pwm,200);
  
    digitalWrite(motor2pin1, LOW);
    digitalWrite(motor2pin2, HIGH);
    analogWrite(motor2pwm,200);

    delay(2000);
  
}
