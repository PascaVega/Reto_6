#Reto 6 - Punto 7
#Escriba un programa que pida 5 números reales y calcule las siguientes operaciones: 
#Promedio, mediana, promedio multiplicativo, ordenar los números de forma ascendente, ordenar los números de forma descendente, potencia del mayor número elevado al menor número, raíz cúbica del menor número.
from funciones import ordenar_numeros
from funciones import promedio
from funciones import mediana
from funciones import promedio_multiplicativo
from funciones import ascendente
from funciones import descendente
from funciones import potencia
from funciones import raiz

def introducir():
    num1 : float = float(input("Ingrese el primer número. Ejemplo: 50.75: "))
    num2 : float = float(input("Ingrese el segundo número. Ejemplo: 50.75: "))
    num3 : float = float(input("Ingrese el tercer número. Ejemplo: 50.75: "))
    num4 : float = float(input("Ingrese el cuarto número. Ejemplo: 50.75: "))
    num5 : float = float(input("Ingrese el quinto número. Ejemplo: 50.75: "))
    numeros = ordenar_numeros(num1,num2,num3,num4,num5)
    desarrollo(num1,num2,num3,num4,num5,numeros)

def desarrollo(num1,num2,num3,num4,num5,numeros):
    promedio(num1,num2,num3,num4,num5)
    mediana(numeros)
    promedio_multiplicativo(num1,num2,num3,num4,num5)
    ascendente(numeros)
    descendente(numeros)
    potencia(numeros)
    raiz(numeros)
    return
    
def continuar():
    opcion : int = int(input("¿Desea continuar? Marque 1 (sí) o 2 (no): "))
    return opcion

if __name__ == "__main__":
    print("Ingrese cinco número para realizar determinadas operaciones.")

    while True:
        introducir()
        opcion = continuar()
        if opcion == 2:
            break
        elif opcion != 1 and 2:
            print("Sintax error")
            break

# ! /\|=\/