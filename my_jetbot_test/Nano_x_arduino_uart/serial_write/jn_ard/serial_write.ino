
void setup()
{
  Serial.begin(115200);
  pinMode(LED_BUILTIN, OUTPUT);
}

char data_from_nano;

void loop()
{
  Serial.write("Hello Jetson!\n");
  data_from_nano = Serial.read();
  digitalWrite(LED_BUILTIN, LOW);
  delay(500); 
//  Serial.print(data_from_nano, HEX);
  if(data_from_nano == 'H')
  {
    digitalWrite(LED_BUILTIN, HIGH);
    delay(500);  
  }
  /*
  if (Serial.available())
  { 
    data_from_nano = Serial.read();
    data_from_nano = (data_from_nano, DEC);
    Serial.write("Hello Jetson!");
    Serial.print("I received ");
    Serial.println(data_from_nano, DEC);
  }
  */
}
