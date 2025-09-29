from random import *

numero = randint(0 , 100)

while True:
    adivina = int(input("Dime un numero del 0 al 100"))
    if numero > adivina:
        print("El número es más alto, sigue intentándolo pringado")
    elif numero < adivina:
        print("El numero es más bajo, sigue intentándolo pringado")
    else:
        print("HAS ACERTADO")
        
