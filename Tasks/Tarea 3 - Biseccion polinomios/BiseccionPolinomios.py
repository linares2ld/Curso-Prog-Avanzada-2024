# LIBRERIAS QUE OCUPA

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# >>>>>>>> EXTRAE LOS COEFIENCIENTES Y GRADOS DE UNA ECUACIÓN POLINOMIAL

class Preprocessing_operations:
    def __init__(self,polynomial):
        self.polynomial = polynomial

    # Separa el polinomio en monomios y los monomios en térmios: 
    # - coeficiente con signo
    # - variable
    # - grado del monomio
    def split_terms(self):
        self.polynomial = self.polynomial.split(" ")
        aux_list = []
        for i in range(len(self.polynomial)):
            aux = self.polynomial[i].split("*")
            aux_list.append(aux)

        return aux_list
    
    # Mide la cantidad de términos separados del monomio
    def monomials_size(self,split_polynomial):
        aux_list = []
        for i in range(len(split_polynomial)):
            aux = len(split_polynomial[i])     
            aux_list.append(aux)

        return aux_list
    
    # Reorganiza el polinomio partido en términos para que tenga el formato necesario:
    def reorganize(self,split_polynomial,polynomial_size):
        for  terms,size in zip(split_polynomial,polynomial_size):
            if size == 3:
                aux = terms[0][0]
                if aux == '-':
                    terms.insert(0,-1)
                else :
                    terms.insert(0,1)
            if size == 1:
                aux = terms[0][0]
                if len(terms[0]) == 1:
                    if terms[0] == "x":
                        terms.insert(0,1)
                else:
                    is_x = terms[0][1].isalpha()
                    if is_x == True:
                        if aux == '+':
                            terms.insert(0,1)
                        else :
                            terms.insert(0,-1)
                            
    # Extrae los el coefiente y el grado de cada monomio en una matriz
    # lista1 = coeficientes
    # lista2 = grado
    def extractor_coeff_grades(self):
        split_polynomial = self.split_terms()
        polynomial_size = self.monomials_size(split_polynomial)
        self.reorganize(split_polynomial,polynomial_size)
        polynomial_size = self.monomials_size(split_polynomial)
        list_aux = [[],[]]
        for terms,size in zip(split_polynomial,polynomial_size):
            if size == 4:
                aux1 = terms[0]
                aux2 = terms[3]
                list_aux[0].append(int(aux1))
                list_aux[1].append(int(aux2))
            if size == 2:
                aux1 = terms[0]
                list_aux[0].append(int(aux1))
                list_aux[1].append(1)
            if size == 1:
                aux1 = terms[0]
                list_aux[0].append(int(aux1))
                list_aux[1].append(0)

        return list_aux
    
# <<<<<<<< EXTRAE LOS COEFIENCIENTES Y GRADOS DE UNA ECUACIÓN POLINOMIAL


# >>>>>>>> EVALUA EN X ECUACIONES POLINOMIALES

class Evaluate_polynomial(Preprocessing_operations):
    def __init__(self,polynomial):
        super().__init__(polynomial)
        self.polynomial = polynomial

    def evaluate(self, x):
        coeffs,grades = self.extractor_coeff_grades()
        x = float(x)
        aux = 0
        result = 0
        for coeff,grade in zip(coeffs,grades):
            aux = x**grade
            aux = coeff*aux
            result += aux
        return result
    
    def WLaTex(self):
        LaTexPol = self.polynomial

        LaTexPol = LaTexPol.replace("**","^")
        LaTexPol = LaTexPol.replace("*","")
        LaTexPol = "$y = " + LaTexPol +"$"

        return LaTexPol
    
# <<<<<<<< EVALUA EN X ECUACIONES POLINOMIALES


# >>>>>>>> GRAFICA ECUACIONES POLINOMIALES

class Chart_polynomial(Evaluate_polynomial):
    def __init__(self,polynomial):
        super().__init__(polynomial)
        self.polynomial = polynomial

    def graph(self,a,b,size=0.01,label=False):
        x = np.arange(a,b,size)
        n = len(x)
        y = np.zeros(n)
        for i in range(n):
            chart = Chart_polynomial(self.polynomial)
            y[i] = chart.evaluate(x[i])
        plt.plot(x,y,label=label)
        plt.legend()
        plt.show()

# <<<<<<<< GRAFICA ECUACIONES POLINOMIALES


# >>>>>>>> MÉTODO DE BISECCIÓN DE POLINOMIOS

class Biseccion(Evaluate_polynomial):
    def __init__(self,polynomial,i,error):
        super().__init__(polynomial)

        # Atributos para crear la clase
        self.polynomial = polynomial
        self.i = i
        self.error = error

        # Punto = xr
        self.xr = 0

        # Funciones evaludas en los puntos a y xr
        self.fa = 0
        self.fxr = 0

        self.ep = 0
    
    def calcularXr(self):
        self.xr = (self.a + self.b)/2
        
    def calcularBiseccion(self):
        self.i = int(input("Número de iteraciones: "))
        self.error = float(input("Error permitido: "))
        self.a = float(input("a: "))
        self.b = float(input("b: "))
        i = 0
        e = 1
        while(i<self.i and e>self.error):

            self.calcularXr()
            fa = Evaluate_polynomial(self.polynomial)
            self.fa = fa.evaluate(self.a)

            fxr = Evaluate_polynomial(self.polynomial)
            self.fxr = fxr.evaluate(self.xr)


            fafxr = self.fa * self.fxr
            if(fafxr > 0):
                self.a = self.xr
            elif(fafxr < 0):
                self.b = self.xr
            elif(fafxr == 0):
                break

            i += 1
            self.ep = abs(self.fxr)*100
        
        return self.xr, self.ep

class BiseccionPolinomio(Biseccion,Chart_polynomial):
    def __init__(self,i=1000,error=0.01,polynomial="x"):
        Biseccion.__init__(self,polynomial,i,error)
        Chart_polynomial.__init__(self,polynomial)

        self.polynomial = polynomial
        self.i = i
        self.error = error

    def EscribirPolinomio(self):
        self.polynomial = input("polinomio: ")

    def GraficarPolinomio(self,a=-1,b=1):
        
        repetir = True
        while repetir == True:
            a = float(input("Extremo izquierdo: "))
            b = float(input("Extremos derecho: "))
            print("")

            chart = Chart_polynomial(self.polynomial)
            sns.set_theme(style="whitegrid", palette='Spectral',font_scale=1)
            plt.axhline(0, color='gray',linewidth=1.5)
            plt.axvline(0, color='gray',linewidth=1.5)
            plt.title("Gráfica")
            plt.xlabel("Eje X")
            plt.ylabel("Eje Y")

            etiqueta = Evaluate_polynomial(self.polynomial)
            etiqueta = etiqueta.WLaTex()
            chart.graph(a,b,label=etiqueta)

        
            aux = input("¿Desea graficar en otro intervalo? (y/n): ")
            print("")
            aux = aux.lower()

            if aux == "y":
                repetir = True
            elif aux == "n":
                repetir = False

# <<<<<<<< MÉTODO DE BISECCIÓN DE POLINOMIOS

RaizPolinomio = BiseccionPolinomio()
RaizPolinomio.EscribirPolinomio()
RaizPolinomio.GraficarPolinomio()
raiz,error = RaizPolinomio.calcularBiseccion()
print(f"X de la raíz: {raiz}\nError: {error}")
        