#RETO 6 - Parte 2
#Desarrolle una función matemática para calcular el perímetro y el área de la figura. Además, cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r, a y b.
import math

def introducir():
    radio : float = float(input("Ingrese el valor del radio en centímetros en números. Ejemplo 57.9: "))
    base : float = float(input("Ingrese el valor de la base en centímetros en números. Ejemplo 25.8: "))
    altura : float = float(input("Ingrese el valor de la altura en centímetros en números. Ejemplo 16.5: "))
    perimetro(radio,base,altura)
    return

def perimetro(radio,base,altura):
    perimetro_cuadrilatero : float = base*2 + altura*2
    perimetro_circunferencia : float = math.pi*2*radio
    perimetro_total : float = perimetro_circunferencia*2 + perimetro_cuadrilatero
    print(f"El perimetro de la figura es de {perimetro_total} cm")
    area(radio,base,altura)
    return 

def area(radio,base,altura):
    area_cuadrilatero : float = base*altura
    area_circunferencia : float = math.pi*radio**2
    area_total : float = area_circunferencia*2 + area_cuadrilatero
    print(f"El área superficial de la figura es de {area_total} cm^2")
    return

def continuar():
    opcion : int = int(input("¿Desea continuar? Marque 1 (sí) o 2 (no): "))
    return opcion

if __name__ == "__main__":
    print("Programa para determinar el perimetro y área de una figura")

    while True:
        introducir()
        opcion = continuar()
        if opcion == 2:
            break
        elif opcion != 1 and 2:
            print("Sintax error")
            break

# ! /\|=\/