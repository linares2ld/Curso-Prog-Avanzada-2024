import tkinter as tk
import calcopgui.basicop as cg # Módulo propio para manejar las operaciones de la calculadora

class Calculadora(cg.BasicOp):  # Como la clase Calculadora hereda a la clase BasicOP que se encuentra en el
    def __init__(self):         # módulo, puede usar todos sus métodos sin tener que escribir el cg
        self.a = ""
        self.b = ""
        self.operacion = 0
        self.decimal = True
        self.botones = []
        self.etiquetas = ["7","8","9","*","AC",
                          "4","5","6","/","DEL",
                          "1","2","3","+","ANS",
                          "0",".","=","-","SCI"]
        self.metodos = [self.siete,self.ocho,self.nueve,self.mult,self.AC,
                        self.cuatro,self.cinco,self.seis,self.div,self.DEL,
                        self.uno,self.dos,self.tres,self.suma,self.ANS,
                        self.cero,self.punto,self.igual,self.rest,self.SCI]
    def interfaz(self):
        self.root = tk.Tk()
        self.root.geometry("310x330")
        
        # Crea la lista de botones asignando automaticamente su etiqueta y método correspondiente

        for i in range(20):
            self.botones.append(tk.Button(self.root,
                                          text=self.etiquetas[i],
                                          width=5,
                                          height=2,
                                          command=self.metodos[i]))
        
        # Este doble for anidado sirve para colocar los botones en la interfaz
           
        c=0 # Índice de la lista self.botones
        for i  in range(4):
            for j in range(5):
                self.botones[c].place(x=30+j*50,y=100+i*50)
                c += 1

        self.botones[14].config(state=tk.DISABLED) # Desactiva los botones sin funcionalidad
        self.botones[19].config(state=tk.DISABLED)

        # Pantalla de la calculadora

        self.display = tk.Label(self.root,text="0")
        self.display.place(x=30,y=50)
        self.root.mainloop()

calculadora = Calculadora()
calculadora.interfaz()