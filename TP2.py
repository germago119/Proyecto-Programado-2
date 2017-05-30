#           _____________________________
#__________/BIBLIOTECAS
from tkinter import *
from tkinter import messagebox
from threading import Thread
import os
import winsound
import sys

sys.setrecursionlimit(10000000)

#-------------------------------------------------------


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
        self.left_frames = ["W1L.png", "W2L.png", "W3L.png", "W4L.png"]
        self.right_frames = ["W1R.png", "W2R.png", "W3R.png", "W4R.png"]
        master.title("Azrael")
        master.minsize(1300, 800)
        master.resizable(width=NO, height=NO)

        self.pos = -1  # Variable de posicion
        self.x_azrael = 400  # posicion inicial en x del robot para left() y right()

        #Canvas donde estara el Robot
        self.fondo = Canvas(master, width=1300, height= 800, bg="#000000")
        self.fondo.place(x=0, y=0)
#           ____________________________
#__________/Cargar una imagen de fondo
        #self.imagenFondo = self.cargarImagen("Front.png")
        #self.LabelFondo = Label(master, image=self.imagenFondo, bg="#FFFFFF")
        #self.LabelFondo.place(x=0, y=0)
#           ______________________________
# __________/Se crea el robot
        self.frame1 = self.cargarImagen("Front.png")
        self.azrael = Label(self.fondo, bg='white')
        self.azrael.config(image=self.frame1)
        self.azrael.image = self.frame1
        self.azrael.place(x=400, y=50)

        self.label_title = Label(master, text="Diseño del control:", fg="#ffffff", bg="#000000", font=("Eczar", 22, "bold"))
        self.label_title.place(x=90, y=650)

        #  AQUI VA UNA IMAGEN DEL CONTROL CON LOS BOTONES

        self.b1 = Button(self.master, text="Prueba right", command=self.right)
        self.b1.place(x=700, y=10)
        self.b2 = Button(self.master, text="Prueba Left", command=self.left)
        self.b2.place(x=600, y=10)

        self.master.mainloop()
#           ______________________________
# __________/Función que ejecuta que se mueva hacia la derecha


    def right(self):
        self.azrael.place(x=self.x_azrael, y=50)
        self.pos += 1
        self.x_azrael += 7
        if self.x_azrael == 399 or self.x_azrael in range (750, 757):
            self.pos = -1
            self.azrael.config(image=self.frame1)
            self.azrael.image = self.frame1
            return
        if self.x_azrael > 1220:
            self.pos = -1
            self.x_azrael = 0
        if self.pos == len(self.right_frames):
            self.pos = 0
        frame3 = self.cargarImagen(self.right_frames[self.pos])
        self.azrael.config(image=frame3)
        self.master.after(5, self.right)
        self.master.mainloop()

    def left(self):
        self.azrael.place(x=self.x_azrael, y=50)
        self.pos += 1
        self.x_azrael -= 7
        if self.x_azrael == 401 or self.x_azrael in range (-1, 6):
            self.pos = -1
            self.azrael.config(image=self.frame1)
            self.azrael.image = self.frame1
            return
        if self.x_azrael < -450:
            self.pos = -1
            self.x_azrael = 800
        if self.pos == len(self.left_frames):
            self.pos = 0
        frame3 = self.cargarImagen(self.left_frames[self.pos])
        self.azrael.config(image=frame3)
        self.master.after(5, self.left)
        self.master.mainloop()



root = Tk()
ventana_principal = GUI(root)
root.mainloop()
