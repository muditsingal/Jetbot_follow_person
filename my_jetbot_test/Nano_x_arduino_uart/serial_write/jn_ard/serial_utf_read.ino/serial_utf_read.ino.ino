void setup()
{
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

char data_from_nano;
wchar_t buffer[32];
int i = 0;
int read_char;
String read_line;

void loop()
{
  Serial.write("Hello Jetson!\n");
//  buffer[i] = Serial.read();
//  read_char = Serial.read();
  read_line = Serial.readString();
  Serial.print(read_line.length());
  Serial.println(read_line);
  

//  digitalWrite(LED_BUILTIN, LOW);
//  delay(1200); 
//  if(char(read_char) == 'H')
//  {
//    digitalWrite(LED_BUILTIN, HIGH);
//    delay(500);
//  }
}
