#           _____________________________
#__________/BIBLIOTECAS
from tkinter import *
from pygame import *
from threading import Thread
import os
import winsound
import sys
import time

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
        self.own_frames= ["D1.png", "D2.png", "D3.png", "D4.png", "D5.png", "D6.png", "D7.png", "D8.png", "D9.png", "D10.png", "D11.png", "D12.png", "TDF1.png", "TDF2.png", "TDF3.png"]
        self.presen_frames = ["H1.png", "H2.png", "H3.png", "H4.png", "H5.png", "H6.png", "H7.png", "H8.png", "H9.png", "H10.png", "H11.png", "H12.png", "H13.png", "H14.png"]
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

        self.label_description = Label(master, text="Hola, mi nombre es Azrael. Soy un pequeño juego creado por Kevyn Guadamuz y Roger Valderrama \n"
                                                    "Acercate, toma el control y empieza a jugar conmigo. Descubre lo que puedo hacer con solo presionar un botón. \n"
                                                    "Interactua conmigo y podrás conocer a mi mejor amigo y verás lo que podemos hacer juntos.", fg="#ffffff", bg="#000000", font=("Eczar", 16, "bold"))
        self.label_description.place(x=80, y=675)
        self.label_rights =Label(master, text="Rights Reserve to Kevyn Guadamuz and Roger Valderrama, Tecnológico de Costa Rica.", fg="#ffffff", bg="#000000", font=("Eczar", 11, "bold"))
        self.label_rights.place(x=350, y=765)

        self.b1 = Button(self.master, text="Prueba right", command=self.own)
        self.b1.place(x=700, y=10)
        self.b2 = Button(self.master, text="Prueba Left", command=self.presentation)
        self.b2.place(x=600, y=10)

        self.master.mainloop()
#           ______________________________
# __________/Función que ejecuta que se mueva hacia la derecha


    def right(self):
        flag_right = 1
        while flag_right != 0:
            self.azrael.place(x=self.x_azrael, y=50)
            self.pos += 1
            self.x_azrael += 7
            if self.x_azrael == 399 or self.x_azrael in range (750, 757):
                self.pos = -1
                self.azrael.config(image=self.frame1)
                self.azrael.image = self.frame1
                break
            if self.x_azrael > 1220:
                self.pos = -1
                self.x_azrael = 0
            if self.pos == len(self.right_frames):
                self.pos = 0
            frame2 = self.cargarImagen(self.right_frames[self.pos])
            self.azrael.config(image=frame2)
            self.master.update()

#             _______________________________________________
#____________/Función que hace que se mueva hacia la izquierda

    def left(self):
        flag_left = 1
        while flag_left != 0:
            self.azrael.place(x=self.x_azrael, y=50)
            self.pos += 1
            self.x_azrael -= 7
            if self.x_azrael == 401 or self.x_azrael in range (-1, 6):
                self.pos = -1
                self.azrael.config(image=self.frame1)
                self.azrael.image = self.frame1
                break
            if self.x_azrael < -450:
                self.pos = -1
                self.x_azrael = 800
            if self.pos == len(self.left_frames):
                self.pos = 0
            frame3 = self.cargarImagen(self.left_frames[self.pos])
            self.azrael.config(image=frame3)
            self.master.update()


#             _______________________________________________
#____________/Función naciente de la creatividad del grupo de trabajpo

    def own(self):
        flag_presen = 1
        conta = 0
        #pygame.mixer.init()
        #pygame.mixer.music.load("Marshmellow.mp3")
        #pygame.mixer.music.play()
        while flag_presen != 0:
            if conta == 15:
                time.sleep(1)
                # own_music.stop()
                break
            else:
                if conta <= 11:
                    self.azrael.place(x=0, y=50)
                    frame4 = self.cargarImagen(self.own_frames[conta])
                    self.azrael.config(image=frame4)
                    conta += 1
                    time.sleep(0.1)
                else:
                    self.azrael.place(x=150, y=50)
                    frame4 = self.cargarImagen(self.own_frames[conta])
                    self.azrael.config(image=frame4)
                    conta += 1
                    time.sleep(0.1)
            self.master.update()
        self.azrael.destroy()
        self.frame1 = self.cargarImagen("Front.png")
        self.azrael = Label(self.fondo, bg='white')
        self.azrael.config(image=self.frame1)
        self.azrael.image = self.frame1
        self.azrael.place(x=400, y=50)
        self.master.update()

    #def music_presen(self):
     #   winsound.PlaySound("AUDIO", winsound.SND_ASYNC)


#             _______________________________________________
#____________/Función reproduce la musica


    def play(self):
        global music
        music = True
        play_thr = Thread(target=self.play_aux(), args=())
        play_thr.start()

    def play_aux(self):
        while music:
            winsound.PlaySound("Marshmellow.wav", winsound.SND_FILENAME)

    def pause(self):
        global music
        music = False

#             _______________________________________________
#____________/Función que hace la presentacion

    def presentation(self):
        flag_presen = 1
        conta = 0
        #prese = Thread(target=self.music_presen, arg())
        #prese.start()
        while flag_presen != 0:
            if conta == 14:
                time.sleep(1)
                break
            else:
                self.azrael.place(x=350, y=50)
                frame5 = self.cargarImagen(self.presen_frames[conta])
                self.azrael.config(image=frame5)
                conta += 1
                time.sleep(0.2)
            self.master.update()
        self.azrael.destroy()
        self.frame1 = self.cargarImagen("Front.png")
        self.azrael = Label(self.fondo, bg='white')
        self.azrael.config(image=self.frame1)
        self.azrael.image = self.frame1
        self.azrael.place(x=400, y=50)
        self.master.update()

 # def music_own(self):
 #       winsound.PlaySound("TURN DOWN FOR WHAT", winsound.SND_ASYNC)

root = Tk()
ventana_principal = GUI(root)
root.mainloop()
