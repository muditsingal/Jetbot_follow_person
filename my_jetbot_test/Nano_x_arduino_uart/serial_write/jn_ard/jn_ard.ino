void setup() {
  Serial.begin(115200);
  while (!Serial) {
  }

}

void loop() {
  char buffer[16];
  // if we get a command, turn the LED on or off:
  if (Serial.available() > 0) {
    Serial.write("2456 Jetson mo!\n");
    int size = Serial.readBytesUntil('\n', buffer, 12);
    digitalWrite(LED_BUILTIN, LOW);
    Serial.println(buffer[0]);
    delay(1500);
    if (buffer[0] == 'H') {
      digitalWrite(LED_BUILTIN, HIGH);
      delay(1500);
    }
//    if (buffer[0] == 'N') {
//      digitalWrite(LED_BUILTIN, LOW);
//    }
  }
}
