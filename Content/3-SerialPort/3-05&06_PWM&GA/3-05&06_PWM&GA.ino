// FUNCIONA PARA: 3-05_PWM.py Y 3-06_graficaAnimada.py

int TON = 0;
int TOFF = 100;
int T = 10;
int tomms = 0;
int toffms = 10;

int LED = 13;
int pot = 0;

void setup() {
  pinMode(LED,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0){
    char dato = Serial.read();
    if(dato == 'u'){ //  Incrementa el tiempo de encendido TON en 10%, hasta un máximo de 100%.
      if(TON < 100){
        TON = TON + 10;
      }
    }
    if(dato == 'd'){ // Decrementa el tiempo de encendido TON en 10%, hasta un mínimo de 0%.
      if(TON > 0){
        TON = TON - 10;
      }
    }
    TOFF = 100 -TON; // Actualiza el tiempo de apagado TOFF en función del nuevo TON
  }
  else{
    tomms = TON*T/100; // Calcula el tiempo de encendido en milisegundos.
    toffms = TOFF*T/100; // Calcula el tiempo de apagado en milisegundos.
    digitalWrite(LED,HIGH);
    delay(tomms);
    digitalWrite(LED,LOW);
    delay(toffms);
    pot = analogRead(0);
    Serial.println(pot);
    delay(100);
  }
}