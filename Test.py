#           _____________________________
# __________/BIBLIOTECAS
from tkinter import *
import os
import sys
import serial
import time
import threading
import queue
import pygame



# -------------------------------------------------------
"""....Se define este Thread propio para lograr ejecutar la interfaz y la lectura del arduino al mismo tiempo...."""
class myThread(threading.Thread):

    def __init__(self, myserial, queque):

        threading.Thread.__init__(self)
        self.queque = queque
        self.ser = myserial

    def run(self):
        while 1:
            if self.ser.readline() != None:
                #  Convierte las señales recibidas del Arduino en mensajes para ejecutar las funciones en Python
                if self.ser.readline() == b'I\r\n':
                    self.queque.put("IZQ")
                if self.ser.readline() == b'D\r\n':
                    self.queque.put("DER")
                if self.ser.readline() == b'P\r\n':
                    self.queque.put("PRESENTATION")
                if self.ser.readline() == b'O\r\n':
                    self.queque.put("OWN")
                if self.ser.readline() == b'L\r\n':
                    self.queque.put("PLAY/PAUSE")



# --------------------------------------------------------------------
"""
 _____________________________________________________
|                    CLASE ROBOT                      |
|_____________________________________________________|
"""

class Robot:
    def __init__(self):
        self.miVentana = None
        self.ser = serial.Serial('COM3', 9600)#Inicializa la comunicacion con el Arduino(EL PUERTO)
        self.botones = ""

"""
 _____________________________________________________
|                    CLASE GUI                        |
|_____________________________________________________|
"""

class GUI:
    def cargarImagen(self, nombre):#Función para cargar las imágenes
        ruta = os.path.join('Imagenes', nombre)
        imagen = PhotoImage(file=ruta)
        return imagen

    def __init__(self, master, myserial):
        # Crea la ventana principal
        self.master = master
        self.queque = queue.Queue()

        # Frames para las animaciones, nombre de cada imagen.
        self.left_frames = ["W1L.png", "W2L.png", "W3L.png", "W4L.png"]
        self.right_frames = ["W1R.png", "W2R.png", "W3R.png", "W4R.png"]
        self.own_frames = ["D1.png", "D2.png", "D3.png", "D4.png", "D5.png", "D6.png", "D7.png", "D8.png", "D9.png", "D10.png", "D11.png", "D12.png", "TDF1.png", "TDF2.png", "TDF3.png"]
        self.presen_frames = ["H1.png", "H2.png", "H3.png", "H4.png", "H5.png", "H6.png", "H7.png", "H8.png", "H9.png",
                              "H1.png", "H2.png", "H3.png", "H4.png", "H5.png", "H6.png",
                              "H7.png", "H8.png", "H9.png", "H1.png", "H2.png", "H3.png", "H4.png", "H5.png", "H6.png",
                              "H7.png", "H8.png", "H9.png", "H1.png", "H2.png", "H3.png", "H4.png", "H5.png", "H6.png",
                              "H7.png", "H8.png", "H9.png",
                              "H1.png", "H2.png", "H3.png", "H4.png", "H5.png", "H6.png", "H7.png", "H8.png", "H9.png",
                              "H10.png", "H11.png", "H12.png", "H13.png", "H14.png"]
        self.play_frames = ["PS.png"]
        master.title("Azrael")
        master.minsize(1300, 800)
        master.resizable(width=NO, height=NO)

        self.pos = -1  # Variable de posicion
        self.x_azrael = 400  # Posicion inicial en x del robot para left() y right()

        # Canvas donde estara el Robot
        self.fondo = Canvas(master, width=1300, height=800, bg="#000000")
        self.fondo.place(x=0, y=0)

        #            ______________________________
        # __________/Se crea el robot
        self.frame1 = self.cargarImagen("Front.png")
        self.azrael = Label(self.fondo, bg='white')
        self.azrael.config(image=self.frame1)
        self.azrael.image = self.frame1
        self.azrael.place(x=400, y=50)

        # Texto de la ventana que se encuentra en la parte inferior
        self.label_description = Label(master, text="Hola, mi nombre es Azrael. Soy un pequeño juego creado por Kevyn Guadamuz y Roger Valderrama \n"
                                            "Acercate, toma el control y empieza a jugar conmigo. Descubre lo que puedo hacer con solo presionar un botón. \n"
                                            "Interactua conmigo y podrás conocer a mi mejor amigo y verás lo que podemos hacer juntos.", fg="#ffffff", bg="#000000", font=("Eczar", 16, "bold"))
        self.label_description.place(x=80, y=655)
        self.label_rights = Label(master, text="Rights Reserve to Kevyn Guadamuz and Roger Valderrama, Tecnológico de Costa Rica.", fg="#ffffff", bg="#000000", font=("Eczar", 11, "bold"))
        self.label_rights.place(x=350, y=770)

        self.music = False


        myThread(myserial, self.queque).start()
        self.updateMe()
        self.master.mainloop()


    def updateMe(self):
        """....Esta función es la que verifica el mensaje que se recibe de Arduino, y dependiendo del mensaje llama a la función solicitada....."""
        try:
            msg = self.queque.get(0)
            print("Estoy aqui " + msg)
            if msg == "IZQ":
                self.left()
                print("IZQ")
                self.master.after(100, self.updateMe)
            if msg == "DER":
                self.right()
                print("DER")
                self.master.after(100, self.updateMe)
            if msg == "PRESENTATION":
                self.presentation()
                print("PRESENTATION")
                self.master.after(100, self.updateMe)
            if msg == "OWN":
                self.own()
                print("OWN")
                self.master.after(100, self.updateMe)
            if msg == "PLAY/PAUSE":
                self.play()
                self.music = True
                print("PLAY/PAUSE")
                self.master.after(100, self.updateMe)
        except queue.Empty:
            pass
        self.master.after(100, self.updateMe)
#           ______________________________
# __________/Función que ejecuta la animación que se mueva hacia la derecha

    def right(self):
        flag_right = 1
        while flag_right != 0:
            self.azrael.place(x=self.x_azrael, y=50)
            self.pos += 1
            self.x_azrael += 7
            if self.x_azrael == 399 or self.x_azrael in range(750, 757):
                self.pos = -1
                self.azrael.config(image=self.frame1)
                self.azrael.image = self.frame1
                break
            if self.x_azrael > 1220:
                self.pos = -1
                self.x_azrael = 0
            if self.pos == len(self.right_frames):
                self.pos = 0
            frame3 = self.cargarImagen(self.right_frames[self.pos])
            self.azrael.config(image=frame3)
            self.master.update()

#           ______________________________
# __________/Función que ejecuta la animación que se se mueva hacia la izquierda

    def left(self):
        flag_left = 1
        while flag_left != 0:
            self.azrael.place(x=self.x_azrael, y=50)
            self.pos += 1
            self.x_azrael -= 7
            if self.x_azrael == 401 or self.x_azrael in range(-1, 6): #Caso base: si esta en x, y posición se detiene
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
#____________/Función naciente de la creatividad del grupo de trabajo

    def own(self):
        flag_presen = 1
        conta = 0
        pygame.mixer.init()#Inicia el audio de la animación
        pygame.mixer.music.load("What.ogg")
        pygame.mixer.music.play()
        while flag_presen != 0:
            if conta == 15:
                time.sleep(1)
                break
            else:
                if conta <= 11: #Cambia de posicion de nuevo el frame
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
        self.azrael.destroy()#Vuelve la imagen a la imagen principal
        self.frame1 = self.cargarImagen("Front.png")
        self.azrael = Label(self.fondo, bg='white')
        self.azrael.config(image=self.frame1)
        self.azrael.image = self.frame1
        self.azrael.place(x=400, y=50)
        self.master.update()

#             _______________________________________________
#____________/Función reproduce y pausa la musica


    def play(self):
        self.azrael.place(x=130, y=50)
        frame6 = self.cargarImagen(self.play_frames[0])
        self.azrael.config(image=frame6)
        pygame.mixer.init()
        pygame.mixer.music.load("Marshmello.ogg")
        pygame.mixer.music.play()
        self.master.mainloop()

    def pause(self):
        pygame.mixer.init()
        pygame.mixer.music.stop()
        self.azrael.destroy()
        self.frame1 = self.cargarImagen("Front.png")
        self.azrael = Label(self.fondo, bg='white')
        self.azrael.config(image=self.frame1)
        self.azrael.image = self.frame1
        self.azrael.place(x=400, y=50)
        self.master.update()

    #             _______________________________________________
#____________/Función que hace la presentacion

    def presentation(self):
        flag_presen = 1
        conta = 0
        pygame.mixer.init()
        pygame.mixer.music.load("Hello.ogg")
        pygame.mixer.music.play()
        while flag_presen != 0:
            if conta == 50:
                time.sleep(3)
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

ser = serial.Serial('COM3', 9600, timeout=0, write_timeout=0)
root = Tk()
ventana_principal = GUI(root, ser)
root.mainloop()
