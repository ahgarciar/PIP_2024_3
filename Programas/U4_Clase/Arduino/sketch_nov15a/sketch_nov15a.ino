//temas vistos:
//instrucciones para escritura en puertos/pines digitales
//instrucciones para escritura/lectura en puertos/pines analogicos
//delay
//comunicacion serial - MODULO UART 
//instrucciones mis

void setup() {  
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("Hola");
  delay(1000);
}
