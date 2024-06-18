int pot=0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  pot=analogRead(0);
  Serial.println(pot); // Envia el valor de pot al puerto serial
  delay(500);
}
