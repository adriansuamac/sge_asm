
n = int(input("Introduce un número: "))

if n <= 1:
    print("{n} NO es un número primo")
else:
    esPrimo = True  
    
    for i in range(2, int(n*0.5) + 1):
        if n % i == 0:
            esPrimo = False
            
    
    if esPrimo:
        print(f"{n} SÍ es un número primo")
    else:
        print(f"{n} NO es un número primo")
