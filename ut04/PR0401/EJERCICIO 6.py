cantidad = float(input("Introduce la cantidad: "))
unidad1 = input("Introduce la unidad 1 (mm, cm, m, km): ").lower()
unidad2 = input("Introduce la unidad 2 (mm, cm, m, km): ").lower()

if unidad1 == "mm":
    metros = cantidad / 1000
elif unidad1 == "cm":
    metros = cantidad / 100
elif unidad1 == "m":
    metros = cantidad
elif unidad1 == "km":
    metros = cantidad * 1000
else:
    print("Unidad de origen no válida")
    exit()

if unidad2 == "mm":
    resultado = metros * 1000
elif unidad2 == "cm":
    resultado = metros * 100
elif unidad2 == "m":
    resultado = metros
elif unidad2 == "km":
    resultado = metros / 1000
else:
    print("Unidad de destino no válida")
    exit()

print(f"{cantidad} {unidad1} equivalen a {resultado} {unidad2}")
