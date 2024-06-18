import tkinter as tk
import serial
import time

class Comunicacion():
    def __init__(self):
        self.datos = ""
        self.h_boton = 3
        self.w_boton = 6
        self.pa = False
        self.ard = serial.Serial("COM8",9600)
        time.sleep(2)
    
    def Interfaz(self):
        self.root = tk.Tk()
        self.root.geometry("205x280")

        # GIRO A LA IZQUIERDA
        self.B_der = tk.Button(self.root, 
                                  text = "<--",
                                  width=self.w_boton,
                                  height=self.h_boton,
                                  command = self.Izquierda)
        self.B_der.place(x = 20, y = 80)

        # GIRO A LA DERECHA
        self.B_izq = tk.Button(self.root, 
                                  text = "-->",
                                  width=self.w_boton,
                                  height=self.h_boton,
                                  command = self.Derecha)
        self.B_izq.place(x = 130, y = 80)

        # AUMENTA VELOCIDAD
        self.B_up = tk.Button(self.root, 
                                  text = "+ RPM",
                                  width=self.w_boton,
                                  height=self.h_boton,
                                  command = self.Mas)
        self.B_up.place(x = 75, y = 20)

        # DISMINUYE VELOCIDAD
        self.B_down = tk.Button(self.root, 
                                  text = "- RPM",
                                  width=self.w_boton,
                                  height=self.h_boton,
                                  command = self.Menos)
        self.B_down.place(x = 75, y = 140)

        # CIERRA VENTANA
        self.B_cerrar = tk.Button(self.root, 
                                  text = "Cerrar",
                                  width=self.w_boton,
                                  height=1,
                                  command = self.Cerrar)
        self.B_cerrar.place(x = 75, y = 240)

        self.Leer()
        self.root.mainloop()

    def Cerrar(self):
        self.root.destroy()
        self.ard.close()

    def Mas(self):
        self.ard.write("a".encode())

    def Menos(self):
        self.ard.write("e".encode())

    def Derecha(self):
        self.ard.write("d".encode())

    def Izquierda(self):
        self.ard.write("i".encode())

    def Leer(self):
        self.ard.flushInput()
        dato = self.ard.readline()
        try:
            dato = int(dato.decode().strip())
            v = 5 * dato / 1023
        except ValueError:
            v = self.datos
        self.datos = v
        self.root.update()
        self.root.after(10,self.Leer)

interfaz = Comunicacion()
interfaz.Interfaz()