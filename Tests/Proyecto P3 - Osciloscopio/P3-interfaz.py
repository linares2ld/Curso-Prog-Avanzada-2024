import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation 
import serial
import time

class Comunicacion():
    def __init__(self):
        self.texto = 0.5
        self.datos = "0"
        self.x = []
        self.y = []
        self.ard = serial.Serial("COM8", 9600)
        time.sleep(2)
        self.paused = False  # Variable para controlar el estado de la animación
    
    def Interfaz(self):
        self.root = tk.Tk()
        self.root.geometry("900x400")

        self.entrada = tk.Entry(self.root)
        self.entrada.place(x=700,y=250)

        self.bleer = tk.Button(self.root,text="Leer",command=self.leerEntrada)
        self.bleer.place(x=700,y=300)

        self.ltexto = tk.Label(self.root,text="")
        self.ltexto.place(x=700,y=350)

        self.L_v = tk.Label(self.root, text="0v")
        self.L_v.place(x=100, y=100)

        self.B_up = tk.Button(self.root, 
                              text="Up",
                              command=self.Up)
        self.B_up.place(x=700, y=50)

        self.B_down = tk.Button(self.root, 
                                text="Down",
                                command=self.Down)
        self.B_down.place(x=700, y=100)

        self.B_pause = tk.Button(self.root, 
                                 text="Pause",
                                 command=self.Pause)
        self.B_pause.place(x=700, y=150)

        self.B_cerrar = tk.Button(self.root, 
                                  text="Cerrar",
                                  command=self.Cerrar)
        self.B_cerrar.place(x=700, y=200)

        # >>>>>>>> GRÁFICA

        fig = plt.figure(figsize=(6,4))
        self.ax = fig.add_subplot(1, 1, 1)
            # 1er número: cantidad de filas
            # 2do número: cantidad de columnas
            # 3er número: posición del subplot
        self.ax.set_ylim(0, 0.5) # Establece los límites del eje Y de la gráfica

        self.canvas = FigureCanvasTkAgg(fig, master=self.root) #Crea un lienzo de tkinter para integrar la figura de Matplotlib
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.place(x=0, y=0)

        self.colorGrafica = 'blue' # Variable para el color por defecto de la gráfica
        self.line, = self.ax.plot([], [], color=self.colorGrafica) # Crea la línea de la gráfica

        #  Crea una animación que llama al método self.Leer cada 10 milisegundos para actualizar el gráfico dinámicamente
        self.animacion = FuncAnimation(fig,
                                       self.Leer,
                                       interval=10)
        plt.show()

        # <<<<<<<< GRÁFICA

        self.root.mainloop()

    def Cerrar(self):
        self.root.destroy()
        self.ard.close()

    def Pause(self):
        self.paused = not self.paused
        if self.paused: # Detiene y activa la animación de la gráfica
            self.animacion.event_source.stop()
        else:
            self.animacion.event_source.start()

    def Up(self):
        self.ard.write("u".encode())

    def Down(self):
        self.ard.write("d".encode())

    def Leer(self, i):
        if not self.paused:
            self.ard.reset_input_buffer()
            dato = self.ard.readline() # Lee la información del puerto serial
            try:
                dato = int(dato.decode().strip()) # Decodifica el dato del puerto serial
                v = 5 * dato / 1023

            except ValueError:
                v = self.datos
            self.datos = v
            self.ltexto.config(text=v)

            # >>>>>>>> ACTUALIZA LA GRÁFICA

            self.x.append(i) # Actualiza los ejes X y Y de la gráfica
            self.y.append(v)

            # Cuando las listas alcanzan una longitud de 50, se empieza a borrar el primer dato de la lista
            # para agregar el último, esto da la apariencia de que la gráfica para para adelante
            if len(self.y) > 50 :
                self.x.pop(0)
                self.y.pop(0)

            self.line.set_data(self.x, self.y)  # Actualiza los datos en la línea del gráfico
            self.ax.relim()
            self.ax.autoscale_view()
            self.L_v.config(text=str(self.datos))

            # Actualizar el color de la línea
            if float(self.datos) > float(self.texto)*0.9:
                self.colorGrafica = 'red'
                
                print(f'{self.datos} - {self.texto}')
            else:
                self.colorGrafica = 'blue'

            self.line.set_color(self.colorGrafica)

            # <<<<<<<< ACTUALIZA LA GRÁFICA

            self.root.update()

    def leerEntrada(self):
        self.texto = self.entrada.get()
        print(self.texto)
        if float(self.datos) > float(self.texto)*0.9:
            self.colorGrafica = 'red'
            
            print(f'{self.datos} - {self.texto}')
        else:
            self.colorGrafica = 'blue'

interfaz = Comunicacion()
interfaz.Interfaz()