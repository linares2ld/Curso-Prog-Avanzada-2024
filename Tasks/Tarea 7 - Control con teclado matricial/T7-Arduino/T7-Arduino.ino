int I0 = 9;
int I1 = 8;
int I2 = 7;
int I3 = 6;

int O0 = 5;
int O1 = 4;
int O2 = 3;
int O3 = 2;

int boton = 0;

void setup() {
  pinMode(I0,INPUT);
  pinMode(I1,INPUT);
  pinMode(I2,INPUT);
  pinMode(I3,INPUT);

  pinMode(O0,OUTPUT);
  pinMode(O1,OUTPUT);
  pinMode(O2,OUTPUT);
  pinMode(O3,OUTPUT);
  
  Serial.begin(9600);
}

void loop() {
  // CASO 1
  digitalWrite(O1,LOW);
  digitalWrite(O2,LOW);
  digitalWrite(O3,LOW);
  digitalWrite(O0,HIGH);

  if(digitalRead(I0) == 1){
    boton = 1;
  }
  if(digitalRead(I1) == 1){
    boton = 5;
  }
  if(digitalRead(I2) == 1){
    boton = 9;
  }
  if(digitalRead(I3) == 1){
    boton = 13;
  }

  // CASO 2
  digitalWrite(O0,LOW);
  digitalWrite(O2,LOW);
  digitalWrite(O3,LOW);
  digitalWrite(O1,HIGH);

  if(digitalRead(I0) == 1){
    boton = 2;
  }
  if(digitalRead(I1) == 1){
    boton = 6;
  }
  if(digitalRead(I2) == 1){
    boton = 10;
  }
  if(digitalRead(I3) == 1){
    boton = 14;
  }

  // CASO 3
  digitalWrite(O0,LOW);
  digitalWrite(O1,LOW);
  digitalWrite(O3,LOW);
  digitalWrite(O2,HIGH);

  if(digitalRead(I0) == 1){
    boton = 3;
  }
  if(digitalRead(I1) == 1){
    boton = 7;
  }
  if(digitalRead(I2) == 1){
    boton = 11;
  }
  if(digitalRead(I3) == 1){
    boton = 15;
  }

  // CASO 4
  digitalWrite(O0,LOW);
  digitalWrite(O1,LOW);
  digitalWrite(O2,LOW);
  digitalWrite(O3,HIGH);

  if(digitalRead(I0) == 1){
    boton = 4;
  }
  if(digitalRead(I1) == 1){
    boton = 8;
  }
  if(digitalRead(I2) == 1){
    boton = 12;
  }
  if(digitalRead(I3) == 1){
    boton = 16;
  }

  Serial.println(boton);
  boton = 0;
  delay(100);
}
