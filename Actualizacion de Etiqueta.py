import serial
import time
from tkinter import *

ser = serial.Serial('COM3', 9600)

root = Tk()
root.title("Azrael")
root.minsize(600, 600)
root.resizable(width=NO, height=NO)

lbl = Label(text = "Hola Probando el arduino").place(x = 300, y = 300)


while 1:
    if ser.readline() == b'IZQ\r\n':
        lbl=Label(text ="Mae actualizacion de ventana completa").place(x=300, y = 300)
        root.update()
    else:
        lbl =  Label(text = "Mae no estoy recibiendo nada jajaj").place(x = 300, y = 300)
        root.update()
