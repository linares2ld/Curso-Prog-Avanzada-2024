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
      if(dato == 'u'){
        if(TON < 100){
          TON = TON + 10;
        }
      }
      if(dato == 'd'){
        if(TON > 0){
          TON = TON - 10;
        }
      }
      TOFF = 100 -TON;
    }
    else{
      tomms = TON*T/100;
      toffms = TOFF*T/100;
      digitalWrite(LED,HIGH);
      delay(tomms);
      digitalWrite(LED,LOW);
      delay(toffms);
      pot = analogRead(0);
      Serial.println(pot);
      delay(100);
    }
  
}