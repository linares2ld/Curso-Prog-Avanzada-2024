
# Script entregable:

# ---------- Operaciones de preprocesamiento de texto para extrar los valores necesarios ----------

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
                            
    # Extra los el coefiente y el grado de cada monomio en una matriz
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

# ---------- Proceso de derivar y escribir el resultado en formato de ecuación ----------

class Derive_polynomial(Preprocessing_operations):
    def __init__(self,polynomial):
        super().__init__(polynomial)
        self.polynomial = polynomial

    def derive(self):
        coeffs,grades = self.extractor_coeff_grades()
        list_aux = [[],[],[]]
        for coeff,grade in zip(coeffs,grades):
            aux1 = coeff*grade
            aux2 = grade-1
            list_aux[0].append(aux1)
            list_aux[1].append(aux2)
        menor_cero = lambda x:x<0
        list_aux[2] =[menor_cero(x) for x in coeffs]
        return list_aux
    
    def Derivative(self):
        coeffs,grades,signs = self.derive()
        index_size = len(coeffs)
        derivative = []
        if coeffs[index_size - 1] == 0 :
            index_size = index_size - 1
        for coeff,grade,sign,i in zip(coeffs,grades,signs,range(index_size)):
            aux = str(coeff)     
            if (sign == False and i == 0):
                if grade > 0 :
                    if grade == 1 :
                        aux = aux + "*x"
                    else:
                        aux = aux + "*x**" + str(grade)
                    derivative.append(aux)
                    continue
                else:
                    aux = str(coeff)
                    derivative.append(aux)
                    continue
            if sign == False :
                aux = " +" + str(coeff)
            else:
                aux = " " + str(coeff)
            if grade > 0 :
                if grade == 1 :
                    aux = aux + "*x"
                else:
                    aux = aux + "*x**" + str(grade)
            derivative.append(aux)
        result = ""
        for monomial in derivative:
            result = result + monomial

        return result
    
    def Write_derivative(self):
        result = self.Derivative()
        print(f'Derivada: {result}')

# ---------- PRUEBA ----------

# --> línea de ejemplo
# Cambie el polinomio de ejemplo por otro calcular su derivada
derivada1 = Derive_polynomial("4*x**6 -5*x**4 +x**3 -x -4") 

# --> Descomente y comente la línea de ejemplo si quiere introducir los polinomios por medio de la consola
#polinomio = input("Polinomio:")
#derivada1 = Derive_polynomial(polinomio)

derivada1.Write_derivative()