class BasicOp():
    def __init__(self):
        pass

    def cero(self):
        self.b += "0"
        self.display.config(text=self.b)

    def uno(self):
        self.b += "1"
        self.display.config(text=self.b)

    def dos(self):
        self.b += "2"
        self.display.config(text=self.b)

    def tres(self):
        self.b += "3"
        self.display.config(text=self.b)

    def cuatro(self):
        self.b += "4"
        self.display.config(text=self.b)

    def cinco(self):
        self.b += "5"
        self.display.config(text=self.b)

    def seis(self):
        self.b += "6"
        self.display.config(text=self.b)

    def siete(self):
        self.b += "7"
        self.display.config(text=self.b)

    def ocho(self):
        self.b += "8"
        self.display.config(text=self.b)

    def nueve(self):
        self.b += "9"
        self.display.config(text=self.b)

    def div(self):
        self.operacion = 1
        self.a = self.b
        self.b = ""
        self.decimal = True
        self.display.config(text="0")

    def mult(self):
        self.operacion = 2
        self.a = self.b
        self.b = ""
        self.decimal = True
        self.display.config(text="0")

    def suma(self):
        self.operacion = 3
        self.a = self.b
        self.b = ""
        self.decimal = True
        self.display.config(text="0")

    def rest(self):
        self.operacion = 4
        self.a = self.b
        self.b = ""
        self.decimal = True
        self.display.config(text="0")

    def AC(self):
        self.a = ""
        self.b = ""
        self.operacion = 0
        self.decimal = True
        self.display.config(text="0")

    def DEL(self):
        cantidad = len(self.b)
        if self.b[cantidad-1] == ".":
            self.decimal = True
        self.b = self.b[0:cantidad-1]
        self.display.config(text=self.b)

    def ANS(self):
        pass

    def SCI(self):
        pass

    def punto(self):
        if(self.decimal):
            self.b += "."
            self.decimal = False
            texto = self.b + "0"
            self.display.config(text=texto)

    def igual(self):
        if (self.operacion == 1):
            try:
                r = str(float(self.a) / float(self.b))
            except ZeroDivisionError:
                r = "Math Error"

        elif (self.operacion == 2):
            r = str(float(self.a) * float(self.b))

        elif (self.operacion == 3):
            r = str(float(self.a) + float(self.b))

        elif (self.operacion == 4):
            r = str(float(self.a) - float(self.b))
        
        self.display.config(text=r)
        self.a = ""
        self.b = ""
        self.operacion = 0
        self.decimal = True
