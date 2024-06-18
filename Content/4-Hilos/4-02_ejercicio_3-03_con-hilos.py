import tkinter as tk
import threading as th
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

        self.B_mandar = tk.Button(self.root, 
                                  text = "I/O",
                                  command = self.Mandar)
        self.B_mandar.place(x = 100, y = 200)

        self.B_cerrar = tk.Button(self.root, 
                                  text = "Cerrar",
                                  command = self.Cerrar)
        self.B_cerrar.place(x = 100, y = 300)

        h_Leer = th.Thread(target=self.Leer) # Maneja el método self.Leer en un hilo secundario
        h_Leer.run()
        self.root.mainloop()

    def Cerrar(self):
        self.root.destroy()
        self.ard.close()

    def Mandar(self):
        if self.pa:
            self.ard.write("a".encode())
            self.pa = False
        else:
            self.ard.write("p".encode())
            self.pa = True

    def Leer(self):
        self.ard.flushInput()
        dato = self.ard.readline()
        try:
            dato = int(dato.decode().strip())
            v = 20.0 * dato / 1023
        except ValueError:
            v = self.datos
        self.datos = v
        self.L_v.config(text = str(self.datos))
        self.root.update()
        self.root.after(100,self.Leer)

def Inicio():
    interfaz.Interfaz()

interfaz = Comunicacion()
h_man = th.Thread(target=Inicio) # Maneja la interfaz en el hilo principal
h_man.start()