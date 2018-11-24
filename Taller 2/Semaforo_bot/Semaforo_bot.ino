// Definimos las variables
const int LED_VERDE=6;
const int LED_ROJO=4;
const int LED_AMARILLO=5;
unsigned int opcion;

void setup() {
  Serial.begin(9600); // Se inicializa con una velocidad de 9600
  pinMode(LED_VERDE,OUTPUT);
  pinMode(LED_ROJO,OUTPUT);
  pinMode(LED_AMARILLO,OUTPUT);
}

void loop() {
  while(Serial.available()>0){ // Si la conexion es permitida entra
    opcion = Serial.read(); //Lectura del serial
    
    if(opcion=='G')digitalWrite(LED_VERDE,HIGH);
    if(opcion=='g')digitalWrite(LED_VERDE,LOW);
    if(opcion=='Y')digitalWrite(LED_AMARILLO,HIGH);
    if(opcion=='y')digitalWrite(LED_AMARILLO,LOW);
    if(opcion=='R')digitalWrite(LED_ROJO,HIGH);
    if(opcion=='r')digitalWrite(LED_ROJO,LOW);
    if(opcion=='A'){
      digitalWrite(LED_VERDE,HIGH);
      digitalWrite(LED_AMARILLO,HIGH);
      digitalWrite(LED_ROJO,HIGH);
    }
    if(opcion=='a'){
      digitalWrite(LED_VERDE,LOW);
      digitalWrite(LED_AMARILLO,LOW);
      digitalWrite(LED_ROJO,LOW);
    }
  }
}
