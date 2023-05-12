int motor1pin1 = 2;
int motor1pin2 = 4;
int motor1pwm = 3;

int motor2pin1 = 6;
int motor2pin2 = 7;
int motor2pwm = 5;

void setup() {
  Serial.begin(115200);
//  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(motor1pin1, OUTPUT);
  pinMode(motor1pin2, OUTPUT);
  pinMode(motor2pin1, OUTPUT);
  pinMode(motor2pin2, OUTPUT);
  pinMode(motor1pwm, OUTPUT); 
  pinMode(motor2pwm, OUTPUT);
}

String rx_data;
char cmd;
int left_wh_speed = 0;
int right_wh_speed = 0;
char data_read[3];

void loop() {
  if(Serial.available())
  {
    Serial.readBytes(data_read,3);
//    cmd = Serial.read();
    cmd = data_read[0];
//    left_wh_speed = Serial.read();
    left_wh_speed = data_read[1];
//    right_wh_speed = Serial.read();
    right_wh_speed = data_read[2];
//    Serial.println(cmd);
//    Serial.println(left_wh_speed);
//    Serial.println(right_wh_speed);

    
    left_wh_speed = left_wh_speed -63;
    right_wh_speed = right_wh_speed -63;

    if(left_wh_speed <= 0)
    {
      digitalWrite(motor1pin1, LOW);
      digitalWrite(motor1pin2, HIGH);
      analogWrite(motor1pwm,(left_wh_speed+63)*4);
    }
    else
    {
      digitalWrite(motor1pin1, HIGH);
      digitalWrite(motor1pin2, LOW);
      analogWrite(motor1pwm,left_wh_speed*4);
    }
  
  
    if(right_wh_speed <= 0)
    {
      digitalWrite(motor2pin1, LOW);
      digitalWrite(motor2pin2, HIGH);
      analogWrite(motor2pwm,(right_wh_speed+63)*4);
    }
    else
    {
      digitalWrite(motor2pin1, HIGH);
      digitalWrite(motor2pin2, LOW);
      analogWrite(motor2pwm,right_wh_speed*4);
    }
    
//    if(left_wh_speed == 121)
//    {
//      digitalWrite(LED_BUILTIN, HIGH);
//      delay(500);  
//    }
//    digitalWrite(LED_BUILTIN, LOW);
//    delay(500); 
//    
  }
}
  
