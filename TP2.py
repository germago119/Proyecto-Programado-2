#           _____________________________
#__________/BIBLIOTECAS
from tkinter import *
from tkinter import messagebox
from threading import Thread
import os
import winsound
import sys


#-------------------------------------------------------

pos = -1 #Variable de posicion
rep = -1 #Variable de repeticion
x_azrael = 570 #posicion inicial en x del robot para left() y right()
#--------------------------------------------------------------------

class Robot:
    def __init__(self, nombre):
        self.nombre = nombre
        self.imagen = "Front.png"


class GUI:
    def cargarImagen(self, nombre):
        ruta = os.path.join('Imagenes', nombre)
        imagen = PhotoImage(file=ruta)
        return imagen
    
    def __init__(self, master):
        #Crea la ventana principal
        self.master = master
        self.azrael = Label(master, bg='white')
        self.right_frames = ["W1R.png", "W2R.png", "W3R.png", "W4R.png"]
        master.title("Azrael")
        master.minsize(1300, 800)
#           ______________________________
#__________/Se crea un lienzo para objetos
        contenedor_principal = Canvas(master, width=1300, height=800, bg="#000000")
        contenedor_principal.place(x=0, y=0)

        #Canvas donde estara el Robot
        fondo = Canvas(master, width=1300, height= 800, bg="#ffffff")
        fondo.place(x=0, y=0)
#           ____________________________
#__________/Cargar una imagen de fondo
        imagenFondo = self.cargarImagen("Front.png")
        LabelFondo = Label(contenedor_principal, image=imagenFondo, bg="#FFFFFF")
        LabelFondo.place(x=0, y=0)
#           ______________________________
# __________/Se crea el robot
        frame1 = self.cargarImagen("Front.png")
        self.azrael.config(image=frame1)
        self.azrael.image = frame1
        self.azrael.place(x=450, y=110)
#           ______________________________
# __________/Función que ejecuta que se mueva hacia la derecha
    def right(self, pos = -1, rep = -1, x_place= 570):
        self.pos = pos
        self.rep = rep
        self.place = x_place
        self.right_aux()
        self.master.mainloop()

    def right_aux(self):
        global x_azrael
        global pos
        self.azrael.place(x=x_azrael, y=110)
        pos += 1
        x_azrael += 7
        if x_azrael == 563:
            pos = -1
            frame = self.cargarImagen(self.right_frames[1])
            self.azrael.config(image=frame)
            self.azrael.image = frame
            return
        if x_azrael >= 970:
            pos = -1
            frame5 = self.cargarImagen(self.right_frames[1])
            self.azrael.config(image=frame5)
            self.azrael.image = frame5
            return
        if pos == len(self.right_frames):
            pos = 0
        frame3 = self.cargarImagen(self.right_frames[pos])
        self.azrael.config(image=frame3)
        self.master.after(10, self.right)
        self.master.mainloop()

        b1 = Button(self.master, text = "Prueba", command = self.right).place(750, 10)
        self.master.mainloop()
        


    

root = Tk()
ventana_principal = GUI(root)
root.mainloop()
