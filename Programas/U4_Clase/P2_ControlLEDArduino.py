
import serial as ser

arduino = ser.Serial(port="COM4", baudrate=9600, timeout=1)

while True:
    estado_led = input("Ingresa el estado del led: 1 = ON, 0 = OFF")
    arduino.write(estado_led.encode())
    print("Estado Actualizado")
