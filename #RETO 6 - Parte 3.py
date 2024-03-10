#RETO 6 - Parte 3
#Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

def introducir():
    gallinas : int = int(input("Ingrese el número de gallinas. Ejemplo 24: "))
    gallos : int = int(input("Ingrese el número de gallos. Ejemplo 23: "))
    pollitos : int = int(input("Ingrese el número de pollitos. Ejemplo 20: "))
    carne(gallinas,gallos,pollitos)
    return

def carne(gallinas,gallos,pollitos):
    kilos_gallinas : int = gallinas*6
    kilos_gallos : int = gallos*7
    kilos_pollitos : int = pollitos*1
    kilos_totales : int = kilos_gallinas+kilos_gallos+kilos_pollitos
    print(f"La cantidad de carne de las aves es de {kilos_totales} kilos")
    return

def continuar():
    opcion : int = int(input("¿Desea continuar? Marque 1 (sí) o 2 (no): "))
    return opcion

if __name__ == "__main__":
    print("Programa para determinar la cantidad de carne de las aves en kilos")

    while True:
        introducir()
        opcion = continuar()
        if opcion == 2:
            break
        elif opcion != 1 and 2:
            print("Sintax error")
            break

# ! /\|=\/