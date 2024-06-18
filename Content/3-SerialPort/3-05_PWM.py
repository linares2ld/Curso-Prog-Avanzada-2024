import tkinter as tk
import serial
import time

class Comunicacion():
    def __init__(self):
        self.datos = ""
        self.pa = False
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

        self.Leer()
        self.root.mainloop()

    def Cerrar(self):
        self.root.destroy()
        self.ard.close()

    def Up(self):
        self.ard.write("u".encode())

    def Down(self):
        self.ard.write("d".encode())

    def Leer(self):
        self.ard.flushInput()
        dato = self.ard.readline()
        try:
            dato = int(dato.decode().strip())
            v = 5 * dato / 1023
        except ValueError:
            v = self.datos # si el dato no se actualiza a tiempo, se muestra el valor anterior
        self.datos = v
        self.L_v.config(text = str(self.datos))
        self.root.update()
        self.root.after(100,self.Leer)

interfaz = Comunicacion()
interfaz.Interfaz()