import tkinter as tk
import serial
import time

class Comunicacion():
    def __init__(self):
        self.datos = ""
        self.pa = False
        self.ard = serial.Serial("COM4",9600)
        time.sleep(2)
    
    def Interfaz(self):
        self.root = tk.Tk()
        self.root.geometry("300x500")

        self.L_v = tk.Label(self.root,text="0v")
        self.L_v.place(x = 100, y = 100)

        self.B_cerrar = tk.Button(self.root, 
                                  text = "Cerrar",
                                  command = self.Cerrar)
        self.B_cerrar.place(x = 100, y = 300)

        self.Leer()
        self.root.mainloop()

    def Cerrar(self):
        self.root.destroy()
        self.ard.close()

    def Leer(self):
        self.ard.reset_input_buffer() # Limpia el buffer de entrada del puerto serial (recomendado sobre flushInput())
        dato = self.ard.readline()

        try:
            dato = int(dato.decode().strip())
        except ValueError:
            dato = 0
        
        if dato != 0:
            if dato == 1:
                self.datos = "1"
            elif dato == 2:
                self.datos = "2"
            elif dato == 3:
                self.datos = "3"
            elif dato == 4:
                self.datos = "A"
            elif dato == 5:
                self.datos = "4"
            elif dato == 6:
                self.datos = "5"
            elif dato == 7:
                self.datos = "6"
            elif dato == 8:
                self.datos = "B"
            elif dato == 9:
                self.datos = "7"
            elif dato == 10:
                self.datos = "8"
            elif dato == 11:
                self.datos = "9"
            elif dato == 12:
                self.datos = "C"
            elif dato == 13:
                self.datos = "*"
            elif dato == 14:
                self.datos = "0"
            elif dato == 15:
                self.datos = "#"
            elif dato == 16:
                self.datos = "D"

            self.L_v.config(text = self.datos)
            self.root.update()

        self.root.after(100,self.Leer)

interfaz = Comunicacion()
interfaz.Interfaz()