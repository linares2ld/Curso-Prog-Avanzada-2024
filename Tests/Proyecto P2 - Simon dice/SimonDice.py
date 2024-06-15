import tkinter as tk
from tkinter import messagebox as mb
import time
import numpy as np

class SimonDice():
    def __init__(self):
        self.numero_combinaciones = 6
        self.contador = 0 # Contador/índice -> sirve para poder comparar los lugares de las dos listas del juego
        self.listareferencia = []   # Lista con la secuencia que se debe se seguir
        self.listajuego = []        # Lista con los valores elegidos por el jugador
        self.botones = []
        self.bcolores =["#0000FF","#FF0000","#00FF00","#FFFF00"]
        self.metodos = [self.B1,self.B2,self.B3,self.B4]
    def interfaz(self):
        self.root = tk.Tk()
        self.root.geometry("300x250")
        
        # Creación de los botones del juego
        for i in range(4):
            self.botones.append(tk.Button(self.root,
                                          width=11,
                                          height=5,
                                          bg=self.bcolores[i],
                                          command=self.metodos[i],
                                          state=tk.DISABLED))   # Inicializa los botones desactivados

        # Posicionamiento de los botones
        c=0
        for i  in range(2):
            for j in range(2):
                self.botones[c].place(x=30+j*100,y=30+i*100)
                c += 1

        self.binicio = tk.Button(self.root,
                                 text="Inicio",
                                 width=5,
                                 height=1,
                                 command=self.inicio)
        self.binicio.place(x=240,y=100)
        self.root.mainloop()

    def B1(self):
        self.estatusJuego(1)

    def B2(self):
        self.estatusJuego(2)

    def B3(self):
        self.estatusJuego(3)

    def B4(self):
        self.estatusJuego(4)

    def estatusJuego(self,valor):
        self.listajuego.append(valor)

        # Compara los lugares correspondientes en la lista de referencia y la lista del juego
        # Si el jugador se llega a equivocar, se cumple la condición y se acaba el juego con 
        # el jugador perdiendo

        if self.listareferencia[self.contador] != self.listajuego[self.contador]:
            mb.showerror(title="Mensaje del juego",message="Perdiste")
            for i in range(4):  # Desactiva los botones ya que se acabó el juego
                self.botones[i].config(state=tk.DISABLED)

        # Si el jugador no se equivoca se suma uno en el contador para que en la siguiente 
        # jugada se evalue la siguiente posición

        self.contador += 1

        # Si el contador alcanza el número de combinaciones, quiere decir que el jugador no
        # cometió ningún error, y gana

        if self.contador == self.numero_combinaciones:
            mb.showinfo(title="Mensaje del juego",message="Ganaste")
            for i in range(4): 
                self.botones[i].config(state=tk.DISABLED)

    def inicio(self):

        # Reinicio de los valores del juego
        self.contador = 0
        self.listareferencia = []
        self.listajuego = []

        # Creación de una secuencia al azar para el nuevo juego
        self.listareferencia = np.random.randint(1,5,self.numero_combinaciones)
        #print(self.listareferencia) # Descomentar para ver el patrón que se debe de seguir, en la consola

        # >>>>>>>> ANIMACIÓN DEL BRILLO DE LOS BOTONES

        for i in self.listareferencia:
            if i == 1:
                self.botones[0].config(bg="#FFFFFF")
            elif i == 2:
                self.botones[1].config(bg="#FFFFFF")
            elif i == 3:
                self.botones[2].config(bg="#FFFFFF")
            else:
                self.botones[3].config(bg="#FFFFFF")

            self.root.update()
            time.sleep(0.4)     # Tiempo de espera entre los cambios de color

            if i == 1:
                self.botones[0].config(bg="#0000FF")
            elif i == 2:
                self.botones[1].config(bg="#FF0000")
            elif i == 3:
                self.botones[2].config(bg="#00FF00")
            else:
                self.botones[3].config(bg="#FFFF00")

            self.root.update()
            time.sleep(0.4)

        # <<<<<<<< ANIMACIÓN DEL BRILLO DE LOS BOTONES

        for i in range(4):  # Reactiva los botones para que se pueda iniciar el juego
                self.botones[i].config(state=tk.NORMAL)

calculadora = SimonDice()
calculadora.interfaz()
