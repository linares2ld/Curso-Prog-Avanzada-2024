import threading as th
import time

def Contador(n,t,h):
    for i in range(n):
        print("Cuenta número ",i +1," del hilo número ", h)
        time.sleep(t)

H1 = th.Thread(target=Contador, args=(10,0.3,1))
H2 = th.Thread(target=Contador, args=(7,0.5,2))

H1.start() # Corre el hilo 1 en paralelo al principal como un hilo secundario
H2.run() # Corre el hilo 2 como el principal