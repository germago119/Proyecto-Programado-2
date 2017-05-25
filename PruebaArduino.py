import serial
import time

ser = serial.Serial('COM4', 9600, timeout=1)

def a():
    print("Funciona")

while 1:
    if ser.readline() == b'1 \n':
        a()
    else:
        print (ser.readline())
