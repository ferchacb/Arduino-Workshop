//Practica encender y apagar un led con un boton pulsador
const int led=13;
const int boton=7;
int val=0; //almacena el estado del pulsador

void setup(){
  pinMode(led,OUTPUT); //se establece el pin como una señal de salida
  pinMode(boton,INPUT); //se establece el pin como una señal de entrada
}

void loop(){
  val = digitalRead(boton); //hace una lectura del estado del boton
  if(val==HIGH){
    digitalWrite(led,HIGH);
  }else{
    digitalWrite(led,LOW);
  }
}
qq
