import tkinter as tk
from PIL import Image, ImageTk

class Ventana:
    def __init__(self):
        self.aux = False
        self.usuario = "usuario"
        self.password = "Wee7R_MIcj"

    def ventanaLog(self):
        self.log = tk.Tk()
        self.log.title("Login")
        self.log.geometry("200x200")

        self.blog = tk.Button(self.log,text="Registrarse",
                              command=self.Registrar,
                              width=9,
                              height=1,
                              bg="#1A5276",
                              fg="#F1F4EB")
        self.blog.place(x=65,y=80)

        self.bentrar = tk.Button(self.log,text="Acceder",
                                 command=self.Acceder,
                                 width=9,
                                 height=1,
                                 bg="#196F3D",
                                 fg="#F1F4EB")
        self.bentrar.place(x=65,y=120)

        self.bcerrar = tk.Button(self.log,
                                 text="Cerrar",
                                 command=self.Cerrar,
                                 width=5,
                                 height=1,
                                 bg="#E51D1D",
                                 fg="#F3E7E7")
        self.bcerrar.place(x=145,y=10)

        self.log.mainloop()

    def ventanaRA(self,titulo,registro):
        self.log.destroy()          # Ya que las tres ventanas se manejan como objetos Tk() (ventana principal)
        self.RA = tk.Tk()           # es necesario destruir la ventana actual antes de abrir la siguiente.
        self.RA.title(titulo)
        self.RA.geometry("400x250")

        self.lusuario = tk.Label(self.RA,text="Usuario: ")
        self.lusuario.place(x=95,y=78)

        self.eusuario = tk.Entry(self.RA)
        self.eusuario.place(x=150, y=80)

        self.lpassword = tk.Label(self.RA,text="Contraseña: ")
        self.lpassword.place(x=76,y=128)

        self.epassword = tk.Entry(self.RA, show="*")
        self.epassword.place(x=150, y=130)

        self.ltexto = tk.Label(self.RA,
                               text="",
                               fg="#DE0D0D")
        self.ltexto.place(x=125,y=40)

        self.bmo = tk.Button(self.RA,text="Mostrar",
                             command=self.Cambio,
                             bg="#FDFEFE")
        self.bmo.place(x=280,y=127)   

        self.bcerrarRA = tk.Button(self.RA,
                                 text="Cerrar",
                                 command=self.CerrarRA,
                                 width=5,
                                 height=1,
                                 bg="#E51D1D",
                                 fg="#F3E7E7")
        self.bcerrarRA.place(x=345,y=10)

        self.bvolver = tk.Button(self.RA,
                                 text="Volver",
                                 command=self.Volver,
                                 width=5,
                                 height=1,
                                 bg="#AEB6BF",
                                 fg="#17202A")
        self.bvolver.place(x=345,y=45)

        if registro:
            self.bguardar = tk.Button(self.RA,text="Guardar",
                                      command=self.Guardar,
                                      width=12,
                                      height=2,
                                      bg="#7FB3D5",
                                      fg="#171717")
            self.bguardar.place(x=165,y=170)
        else:
            self.bacceder = tk.Button(self.RA,
                                      text="Entrar",
                                      command=self.Entrar,
                                      width=12,
                                      height=2,
                                      bg="#7DCEA0",
                                      fg="#171717")
            self.bacceder.place(x=165,y=170)

        self.RA.mainloop

    def ventanaHome(self):
        self.home = tk.Tk()
        self.home.title("Home")
        self.home.geometry("600x400")

        im_fondo = Image.open('Images\\PenguinLinux.png') # Imagen de fondo
        im_fondo = im_fondo.resize((400,200),Image.LANCZOS) # Filtro para quitar lo pixeleadp
        im_fondo = ImageTk.PhotoImage(im_fondo)
        lfondo = tk.Label(self.home,image=im_fondo).place(x=100,y=100)

        self.bcerrarHOME = tk.Button(self.home,
                                 text="Cerrar sesión",
                                 command=self.CerrarHOME,
                                 width=10,
                                 height=1,
                                 bg="#F17D02",
                                 fg="#F3E7E7")
        self.bcerrarHOME.place(x=10,y=10)

        self.log.mainloop()

    # >>>>>>>>>>>>> FUNCIONES DE LAS VENTANAS 

    # Ventana Login

    def Registrar(self):
        mostrar1.ventanaRA("Registro",True)

    def Acceder(self):
        mostrar1.ventanaRA("Acceder",False)

    def Cerrar(self):
        self.log.destroy()

    # Ventana RA (Registro/Acceder)

    def Cambio(self):
        if self.aux == True:
            self.epassword.config(show="*")
            self.bmo.config(text="Mostrar")
            self.aux = False
        else:
            self.epassword.config(show="")
            self.bmo.config(text="Ocultar")
            self.aux = True

    def CerrarRA(self):
        self.RA.destroy()

    def Volver(self):
        self.RA.destroy()
        mostrar1.ventanaLog()

    def Guardar(self):
        self.usuario = self.eusuario.get()
        self.password = self.epassword.get()
        self.RA.destroy()
        mostrar1.ventanaLog()

    def Entrar(self):
        x_usuario = self.eusuario.get()
        x_password = self.epassword.get()

        if (x_usuario == self.usuario and x_password == self.password):
            self.RA.destroy()
            mostrar1.ventanaHome()
        else:
            self.ltexto.config(text="Contraseña o usuario incorrecto")

    # Ventana Home

    def CerrarHOME(self):
        self.home.destroy()
        mostrar1.ventanaLog()

    # <<<<<<<<<<<<< FUNCIONES DE LAS VENTANAS

mostrar1 = Ventana()
mostrar1.ventanaLog()
