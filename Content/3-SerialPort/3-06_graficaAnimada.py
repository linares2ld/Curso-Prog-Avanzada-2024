import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation 
import serial
import time

class Comunicacion():
    def __init__(self):
        self.datos = ""
        self.pa = False
        self.x = []
        self.y = []
        self.ard = serial.Serial("COM8",9600)
        time.sleep(2)
    
    def Interfaz(self):
        self.root = tk.Tk()
        self.root.geometry("300x500")

        self.L_v = tk.Label(self.root,text="0v")
        self.L_v.place(x = 100, y = 100)

        self.B_up = tk.Button(self.root, 
                                  text = "Up",
                                  command = self.Up)
        self.B_up.place(x = 100, y = 200)

        self.B_down = tk.Button(self.root, 
                                  text = "Down",
                                  command = self.Down)
        self.B_down.place(x = 0, y = 200)

        self.B_cerrar = tk.Button(self.root, 
                                  text = "Cerrar",
                                  command = self.Cerrar)
        self.B_cerrar.place(x = 100, y = 300)

        fig = plt.figure()

        # Configura la animación para actualizar la gráfica cada 10 milisegundos llamando al método Leer
        animacion = FuncAnimation(fig,
                                  self.Leer,
                                  interval = 10)
        plt.show()
        self.root.mainloop()

    def Cerrar(self):
        self.root.destroy()
        self.ard.close()

    def Up(self):
        self.ard.write("u".encode())

    def Down(self):
        self.ard.write("d".encode())

    def Leer(self, i):
        self.ard.reset_input_buffer()
        dato = self.ard.readline()
        try:
            dato = int(dato.decode().strip())
            v = 5 * dato / 1023
        except ValueError:
            v = self.datos
        self.datos = v
        self.x.append(i)
        self.y.append(v)
        plt.plot(self.x,self.y)
        self.L_v.config(text = str(self.datos))
        self.root.update()

interfaz = Comunicacion()
interfaz.Interfaz()