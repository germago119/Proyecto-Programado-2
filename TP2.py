#           _____________________________
#__________/BIBLIOTECAS
from tkinter import *
from tkinter import messagebox
from threading import Thread
import os
# import winsound


class Robot:
    def __init__(self, nombre):
        self.nombre = nombre
        self.imagen = "Cry1.png"


class GUI:
    def cargarImagen(self, nombre):
        ruta = os.path.join('Imagenes', nombre)
        imagen = PhotoImage(file=ruta)
        return imagen
    
    def __init__(self, master):
        #Crea la ventana principal
        self.master = master
        master.title("Azrael")
        master.minsize(750, 600)
#           ______________________________
#__________/Se crea un lienzo para objetos
        contenedor_principal = Canvas(master, width=750, height=600, bg="#000000")
        contenedor_principal.place(x=0, y=0)

        #Canvas donde estara el Robot
        fondo = Canvas(master, width=750, height= 600, bg="#ffffff")
        fondo.place(x=0, y=0)
#           ____________________________
#__________/Cargar una imagen de fondo
        imagenFondo = self.cargarImagen("Cry1.png")
        LabelFondo = Label(contenedor_principal, image=imagenFondo, bg="#FFFFFF")
        LabelFondo.place(x=0, y=0)
#           ______________________________
# __________/Se crea el robot
        frame1 = self.cargarImagen("Cry1.png")
        azrael = Label(fondo, bg='white')
        azrael.config(image=frame1)
        azrael.image = frame1
        azrael.place(x=570, y=110)

    

root = Tk()
ventana_principal = GUI(root)
root.mainloop()
