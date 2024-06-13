import tkinter as tk
from tkinter import ttk

class Ventana:
    def __init__(self):
        self.valores = ["Arroz","Cheve","Tacos de sal"]
    
    def main(self):
        self.root = tk.Tk()
        self.root.title("Ventana")
        self.root.geometry("500x500")

        self.l_valorleido = tk.Label(self.root,
                                     text="")
        self.l_valorleido.place(x=200,y=130)
        
        self.c_lista = ttk.Combobox(self.root,              #Crea un combobox que es la lista desplegable
                                    values = self.valores)
        self.c_lista.place(x=200,y=230)
        self.c_lista.bind("<<ComboboxSelected>>", # Asocia un evento para cuando se seleccione un elemento 
                         self.leerSeleccion)      # de la lista se llame al método leerSeleccion

        self.b_agregar = tk.Button(self.root,
                                   text="Agregar",
                                   command=self.Agregar)
        self.b_agregar.place(x=210,y=400)

        self.b_eliminar = tk.Button(self.root,
                                   text="Eliminar",
                                   command=self.Eliminar)
        self.b_eliminar.place(x=290,y=400)

        self.root.mainloop()

    def leerSeleccion(self,event):
        vleido = self.c_lista.get()
        self.l_valorleido.config(text=vleido)
    
    def Agregar(self):
        vnuevo = self.c_lista.get()
        self.valores.append(vnuevo)
        self.c_lista.config(values=self.valores)

    def Eliminar(self):
        n=self.c_lista.current()
        if n != -1: # n valdrá -1 cuando no haya ningún objeto seleccionado
            self.valores.pop(n)
            self.c_lista.config(values=self.valores)

ventana = Ventana()
ventana.main()