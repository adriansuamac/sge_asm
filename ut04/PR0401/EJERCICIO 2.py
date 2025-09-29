n = int(input("Introduce un número: "))
k = int(input("Número de elementos que quieres que se vean: "))

for i in range(1,k + 1):
    print(n, "*", i, "=", n * i)