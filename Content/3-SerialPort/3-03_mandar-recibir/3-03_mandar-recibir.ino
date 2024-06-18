int LED = 13;
int pot = 0;

void setup() {
  pinMode(LED,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0){ // Verifica si hay datos disponibles para leer del puerto serial
    char dato = Serial.read();
    if(dato == 'p'){
      digitalWrite(LED,HIGH);
    }
    if(dato == 'a'){
      digitalWrite(LED,LOW);
    }
  }
  else{
    pot = analogRead(0);
    Serial.println(pot);
    delay(100);
  }
}
