import tkinter as tk
from PIL import Image,ImageTk

class Ventana():
    def __init__(self):
        self.aux = False

    def crearVentana(self):
        self.root = tk.Tk()
        self.root.geometry("900x500")

        self.ima = Image.open('Images\\OjoAbierto.png') # Abre la imagen
        self.ima = self.ima.resize((30,20)) # Redimensiona la imagen
        self.ima = ImageTk.PhotoImage(self.ima) # Convierte la imagen en algo que tkinter pueda leer

        self.imc = Image.open('Images\\OjoNegado.png')
        self.imc = self.imc.resize((30,20))
        self.imc = ImageTk.PhotoImage(self.imc)

        # Crear un fondo:
        # El primer widget que aparezca se pone primero, este label hace el efecto de imagen de fondo
        im_fondo = Image.open('Images\\PenguinLinux.png')
        im_fondo = im_fondo.resize((900,500),Image.LANCZOS) # Agregar un tipo filtro pasa altas para quitar lo pixeleado
        im_fondo = ImageTk.PhotoImage(im_fondo)
        lfondo = tk.Label(self.root,image=im_fondo).place(x=0,y=0)

        self.econtrasena = tk.Entry(self.root,show="*")
        self.econtrasena.place(x=300,y=220)
        self.ltexto = tk.Label(self.root,text="")
        self.ltexto.place(x=300,y=182)

        self.bleer = tk.Button(self.root,
                               text="Leer",
                               command=self.Leer)
        self.bleer.place(x=470,y=180)

        self.bcerrar = tk.Button(self.root,
                                 text="Cerrar",
                                 command=self.Cerrar)
        self.bcerrar.place(x=850,y=15)

        self.bmo = tk.Button(self.root,
                             image=self.ima, # Coloca una imagen, en lugar de un texto, sobre el botón
                             command= self.Cambio)
        self.bmo.place(x=470,y=220)
        self.root.mainloop()

    def Leer(self):
        texto = self.econtrasena.get()
        self.ltexto.config(text=texto)
    
    def Cerrar(self):
        self.root.destroy()

    def Cambio(self):
        if (self.aux):
            self.econtrasena.config(show="*")
            self.bmo.config(image=self.ima)
            self.aux = False
        else:
            self.econtrasena.config(show="")
            self.bmo.config(image=self.imc)
            self.aux = True

ventana = Ventana()
ventana.crearVentana()