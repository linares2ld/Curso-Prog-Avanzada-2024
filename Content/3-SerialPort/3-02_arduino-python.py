import serial
import time

ard = serial.Serial("COM8",9600)
time.sleep(2)

while (True):
    ard.flushInput() # Limpia el buffer de entrada del puerto serial
    dato = ard.readline() # Lee una línea de datos del dispositivo a través de la conexión serial
        # dato = objeto de bytes
    try:
        dato = int(dato.decode().strip()) 
            # decode() = objeto de bytes --> cadena de texto (UTF8 a ASCII)
            # strip() = elimina los caracteres de espacio en blanco al principio y el final de la cadena
        v = 20.0 * dato / 1023
    except ValueError:
        print("sincronizando...")
    print("V =",v)
    time.sleep(0.5)

    if v == 0:
        break

ard.close()