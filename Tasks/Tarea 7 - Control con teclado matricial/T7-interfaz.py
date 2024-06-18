import tkinter as tk
import serial
import time

class Comunicacion():
    def __init__(self):
        self.datos = ""
        self.i = 12
        self.cont_h = 0
        self.cont_v = 0
        self.pa = False
        self.botones = []
        self.colorDefecto = 'white'
        self.ard = serial.Serial("COM8",9600)
        time.sleep(2)
    
    def Interfaz(self):

        self.root = tk.Tk()
        self.root.geometry("310x350")

        self.B_cerrar = tk.Button(self.root, 
                                  text = "Cerrar",
                                  command = self.Cerrar)
        self.B_cerrar.place(x = 130, y = 300)

        for i in range(25):
            self.botones.append(tk.Button(self.root, 
                                          bg='white',
                                          width=5,
                                          height=2))
        
        self.botones[12].config(bg='red')
        c=0
        for i  in range(5):
            for j in range(5):
                self.botones[c].place(x=30+j*50,y=30+i*50)
                c += 1

        self.Leer()
        self.root.mainloop()

    def Cerrar(self):
        self.root.destroy()
        self.ard.close()

    def Leer(self):
        self.ard.reset_input_buffer()
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

            self.root.update()
        
        self.root.after(100,self.Leer)

        self.MoverCuadro()

    def MoverCuadro(self):

        # DERECHA
        if self.datos == "6" and self.cont_h != 2:
            aux = self.i + 1
            self.botones[self.i].config(bg=self.colorDefecto)
            self.botones[aux].config(bg='red')
            self.i = aux
            self.cont_h = self.cont_h + 1
            self.datos = "1"

        # IZQUIERDA
        if self.datos == "4" and self.cont_h != -2:
            aux = self.i - 1
            self.botones[self.i].config(bg=self.colorDefecto)
            self.botones[aux].config(bg='red')
            self.i = aux
            self.cont_h = self.cont_h - 1
            self.datos = "1"

        # ABAJO
        if self.datos == "2" and self.cont_v != -2:
            aux = self.i - 5
            self.botones[self.i].config(bg=self.colorDefecto)
            self.botones[aux].config(bg='red')
            self.i = aux
            self.cont_v = self.cont_v - 1
            self.datos = "1"

        # ARRIBA
        if self.datos == "8" and self.cont_v != 2:    
            aux = self.i + 5
            self.botones[self.i].config(bg=self.colorDefecto)
            self.botones[aux].config(bg='red')
            self.i = aux
            self.cont_v = self.cont_v + 1
            self.datos = "1"
        
        # CERRAR 
        if self.datos == "0":
            self.root.destroy()
            self.ard.close()

interfaz = Comunicacion()
interfaz.Interfaz()