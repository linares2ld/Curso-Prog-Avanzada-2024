import serial
import time

ard = serial.Serial("COM8",9600) # Abre una conexión serial en el puerto COM8 a una velocidad de 9600 baudios
time.sleep(2) # Pausa la ejecución del programa por 2 segundos para asegurarse
              # de que la conexión serial esté completamente establecida

while(True): # Bucle principal
    print("Ingresa la opción deseada: \n")
    print("\t p) Encender LED \n\t a) Apagar LED \n\t s) Salir")

    opcion = input()
    if(opcion == "s" or opcion == "S"):
        break
    ard.write(opcion.encode()) # Envía la opción ingresada al dispositivo a través de la conexión serial

ard.close() # Cierra la conexión serial