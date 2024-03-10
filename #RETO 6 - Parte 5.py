#RETO 6 - Parte 5
#Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.

def introducir():
    capital_inicial : float = float(input("Ingrese el valor del prestamo. Ejemplo 1000000: "))
    interes : float = float(input("Ingrese el valor del interés por mes. Ejemplo 0.03: "))
    tiempo : float = float(input("Ingrese el tiempo del prestamo. Ejemplo 12: "))
    desarrollo(capital_inicial,interes,tiempo)
    return

def desarrollo(capital_inicial,interes,tiempo):
    capital_final = capital_inicial*(1+interes)**tiempo
    print(f"El capital final del prestamo será de {capital_final}")
    return

def continuar():
    opcion : int = int(input("¿Desea continuar? Marque 1 (sí) o 2 (no): "))
    return opcion

if __name__ == "__main__":
    print("Programa para determinar el capital final de un prestamo con interés compuesto")

    while True:
        introducir()
        opcion = continuar()
        if opcion == 2:
            break
        elif opcion != 1 and 2:
            print("Sintax error")
            break

# ! /\|=\/