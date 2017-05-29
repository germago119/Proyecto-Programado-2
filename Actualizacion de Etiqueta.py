import serial
import time
from tkinter import *
from threading import Thread


ser = serial.Serial('COM3', 9600)

root = Tk()
root.title("Azrael")
root.minsize(600, 600)
root.resizable(width=NO, height=NO)

lbl = Label(text = "Hola Probando el arduino").place(x = 300, y = 300)

def update():
    while 1:
        if ser.readline() == b'IZQ\r\n':
            lbl.config(text ="Mae actualizacion de ventana completa")
            lbl.place(x=300, y = 300)
            root.update()
        else:
            lbl.config(text = "Mae no estoy recibiendo nada jajaj")
            lbl.place(x = 300, y = 300)
            root.update()

p = Thread(target=update, args=())
p.start()

root.mainloop()