
import serial as ser

arduino = ser.Serial(port="COM4", baudrate=9600, timeout=1)

while True:
    if arduino.inWaiting(): #equivalente a Serial.available()
        cadena = arduino.readline()
        cadena = cadena.decode().strip()
        if cadena != "":
            print(cadena)

