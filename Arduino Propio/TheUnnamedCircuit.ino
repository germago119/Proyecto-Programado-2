//  _ ___ _______     ___ ___ ___  ___ _   _ ___ _____ ___ 
// / |_  )__ /   \   / __|_ _| _ \/ __| | | |_ _|_   _/ __| 
// | |/ / |_ \ |) | | (__ | ||   / (__| |_| || |  | | \__ \ 
// |_/___|___/___/   \___|___|_|_\\___|\___/|___| |_| |___/ 
// 
// The Unnamed Circuit
// 
// Made by Kevyn Guadamuz
// License: CC-BY-SA 3.0
// Downloaded from: https://circuits.io/circuits/5056880-the-unnamed-circuit

int boton1 = 13;
int boton2 = 12;
int boton3 = 11;
int boton4 = 10;//evitar usar pines 0 y 1
void setup() {
  //inicializa la comunicacion serial
  Serial.begin(9600); //9600 es la "velocidad", el mismo valor debe ser seleccionado en el monitor serial
  pinMode(boton1, INPUT_PULLUP);
  pinMode(boton2, INPUT_PULLUP);
  pinMode(boton3, INPUT_PULLUP);
  pinMode(boton4, INPUT_PULLUP);
  //declaramos el pin como una entrada digital (HIGH o LOW, 0 o 5V)
}

void loop() {
  int button1State = digitalRead(boton1);
  int button2State = digitalRead(boton2);
  int button3State = digitalRead(boton3);
  int button4State = digitalRead(boton4);
    //lee el estado del pin (0 o 1, 0 o 5v)
  if (button1State == 0)
  {
    Serial.println("DER");
  }
  if (button2State == 0)
  {
    Serial.println("IZQ");
  }
  if (button3State == 0)
  {
    Serial.println("PLAY/PAUSE");
  }
  if (button4State == 0)
  {
    Serial.println("OWN");
  }
delay(10);        // espera para la siguiente lectura
}
