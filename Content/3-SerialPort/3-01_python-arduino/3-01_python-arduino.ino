int LED=13;

void setup() {
  pinMode(LED,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  char datos=Serial.read(); // Lee un byte de datos del puerto serial 
  if(datos=='p'){
    digitalWrite(LED,HIGH);
  }
  if(datos=='a'){
    digitalWrite(LED,LOW);
  }
}
