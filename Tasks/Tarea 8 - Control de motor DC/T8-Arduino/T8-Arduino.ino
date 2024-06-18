int TON = 0;
int TOFF = 100;
int T = 10;
int tomms = 0;
int toffms = 10;

bool derecha = true;
bool mas_rpm = true;
bool bloqueo = true;

int LED_derecha = 11;
int LED_izquierda = 10;
int pot = 0;

void setup() {
  pinMode(LED_derecha,OUTPUT);
  pinMode(LED_izquierda,OUTPUT);
  Serial.begin(9600);
}

void loop() {
    if (Serial.available() > 0){
      char dato = Serial.read();

      if(dato == 'a'){
        mas_rpm = true;
        bloqueo = false;
      }
      if(dato == 'e'){
        mas_rpm = false;
        bloqueo = false;
      }
      if(dato == 'd'){
        derecha = true;
        bloqueo = true;
      }
      if(dato == 'i'){
        derecha = false;
        bloqueo = true;
      }


      if(mas_rpm == true && bloqueo == false){
        if(TON < 100){
          TON = TON + 10;
        }
      }
      if(mas_rpm == false && bloqueo == false){
        if(TON > 0){
          TON = TON - 10;
        }
      }
      TOFF = 100 -TON;
    }
    else{
      if (derecha == true){

        digitalWrite(LED_izquierda,LOW);

        tomms = TON*T/100;
        toffms = TOFF*T/100;
        digitalWrite(LED_derecha,HIGH);
        delay(tomms);
        digitalWrite(LED_derecha,LOW);
        delay(toffms);
        pot = analogRead(0);
        Serial.println(pot);
        delay(10);
      }
      if (derecha == false){

        digitalWrite(LED_derecha,LOW);

        tomms = TON*T/100;
        toffms = TOFF*T/100;
        digitalWrite(LED_izquierda,HIGH);
        delay(tomms);
        digitalWrite(LED_izquierda,LOW);
        delay(toffms);
        pot = analogRead(0);
        Serial.println(pot);
        delay(10);
      }
    }
}