
while True:
    try:
        introducirNumero = int(input("Dime un número: "))
        elNumero = float(introducirNumero)
        print(f"Numero valido es:  {elNumero}")
        break

    except ValueError:
        print("ERROR: No es un número válido. Inténtalo de nuevo.")
