int boton1 = 12;

void setup() {
Serial.begin(9600);
pinMode(boton1, INPUT);
}
 
void loop() {
int buttonState = digitalRead(boton1);
if (buttonState == 1){
  Serial.println("DER");
}
else
  Serial.println("IZQ");
}
