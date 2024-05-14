class Promedio():
    def __init__(self): # Método constructor -> Sirve para iniciar atributos
        self.cantidad = 0
        self.valores = [] # Los atributos son "caracteristicas" que tienen los objetos de la clase
        self.promedio = 0 # Funcionan como variables globales dentro de la clase y sus clases hija

    def ingresar_datos(self):
        self.cantidad = int(input("Cantidad de datos de la lista: "))

        for i in range(self.cantidad):
            aux = float(input(f'Dato {i+1}: '))
            #print(f'Dato {i+1}: {aux} ')
            self.valores.append(aux)
        
    def calcular_promedio(self):
        suma = 0

        for i in range(self.cantidad):
            suma += self.valores[i]

        self.promedio = suma / self.cantidad
        print(f'\nPromedio: {self.promedio}')

class Mediana():
    def __init__(self):
        self.cantidad = 0
        self.valores = []
        self.promedio = 0

    def ingresar_datos(self):
        self.cantidad = int(input("Cantidad de datos de la lista: "))

        for i in range(self.cantidad):
            aux = float(input(f'Dato {i+1}: '))
            #print(f'Dato {i+1}: {aux} ')
            self.valores.append(aux)
    
    def calcular_mediana(self):
        self.valores.sort()
        print(f'\nValores ordenados: {self.valores}')
        
        aux1 = self.cantidad % 2
        
        if aux1 == 1:
            aux2 = int(self.cantidad / 2)
            mediana = self.valores[aux2]
            print(f'Mediana: {mediana}')

        else:
            aux2 = int(self.cantidad / 2)
            aux3 = aux2 - 1
            mediana1 = self.valores[aux3]
            mediana2 = self.valores[aux2]
            print(f'{mediana1}, {mediana2}')

class Moda():
    def __init__(self):
        self.cantidad = 0
        self.valores = []
        self.promedio = 0

    def ingresar_datos(self):
        self.cantidad = int(input("Cantidad de datos de la lista: "))

        for i in range(self.cantidad):
            aux = float(input(f'Dato {i+1}: '))
            #print(f'Dato {i+1}: {aux} ')
            self.valores.append(aux)   

    def calcular_moda(self):

        # >> MATRIZ DE CEROS
        esp = len(self.valores)
        aux = []
        for i in range(esp):
            aux.append(0)
        # << MATRIZ DE CEROS

        # >> CONTADOR
        self.valores = sorted(self.valores)

        for i in range(self.cantidad):
            valor_actual = self.valores[i]

            for j in range(i,self.cantidad):
                if(valor_actual == self.valores[j]):
                    aux[j] += 1
        # << CONTADOR
        
        aux3 = 0
        aux2 = aux[0]

        for i in range(1,self.cantidad):
            if(aux[i]>aux2):
                aux2 = aux[i]
                aux3 = i
        
        print(f'\nModa: {self.valores[aux3]}')

class CalculadoraEstadistica(Promedio,Mediana,Moda):

    def menu(self):
            
        while (True):
            
            print("Ingresa la opción deseada")
            print("""
            1.- Promedio
            2.- Mediana
            3.- Moda
                    """)

            opcion = int(input("Selecciona una operación: "))

            if(opcion == 1):
                self.ingresar_datos()
                self.calcular_promedio()
            elif(opcion == 2):
                self.ingresar_datos()
                self.calcular_mediana()
            elif(opcion == 3):
                self.ingresar_datos()
                self.calcular_moda()
            else:
                print("Opción no válida")

            # Reiniciando los valores de los atributos
            self.cantidad = 0
            self.valores = []
            self.promedio = 0

            opcion = input("\nIngresa N si deseas terminar o cualquier otro botón para continuar: ")
            if(opcion == "N" or opcion == "n"):
                break

calculadora_estadistica = CalculadoraEstadistica()
calculadora_estadistica.menu()