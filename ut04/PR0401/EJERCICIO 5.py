numero = float(input("Introduce un numero: " ))
mayor = numero
menor = numero


for i in range(2,6):
    num = float(input("Introduce los numeros: "))

    if num > mayor:
        mayor = num
    if num < menor:
        menor = num
    
print("El numero mayor es {mayor} y el numero menor es {menor}")