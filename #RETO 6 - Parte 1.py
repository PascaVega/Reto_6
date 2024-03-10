#RETO 6 - Parte 1
#Desarrolle una función matemática para calcular el volumen y el área superficial. Además, cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h.
import math

def introducir():
    radio1 : float = float(input("Ingrese el valor del radio 1 (radio esférico) en centímetros en números. Ejemplo 24: "))
    radio2 : float = float(input("Ingrese el valor del radio 2 (radio del cono) en centímetros en números. Ejemplo 24: "))
    altura : float = float(input("Ingrese el valor de la altura (altura del cono) en centímetros en números. Ejemplo 24: "))
    volumen(radio1,radio2,altura)
    return

def volumen(radio1,radio2,altura):
    volumen_esfera : float = math.pi*4/3*radio1**3
    volumen_cono : float = math.pi*radio2**2*altura/3
    volumen_total : float = volumen_esfera + volumen_cono
    print(f"El volumen de la figura es de {volumen_total} cm^3")
    area(radio1,radio2,altura)
    return 

def area(radio1,radio2,altura):
    area_esfera : float = math.pi*4*radio1**2
    area_cono : float = math.pi*radio2*(radio2*2+altura**2)**(1/2)+math.pi*radio2*2
    area_total : float = area_esfera + area_cono
    print(f"El área superficial de la figura es de {area_total} cm^3")
    return

def continuar():
    opcion : int = int(input("¿Desea continuar? Marque 1 (sí) o 2 (no): "))
    return opcion

if __name__ == "__main__":
    print("Programa para determinar el volumen y área supeficial de una figura")

    while True:
        introducir()
        opcion = continuar()
        if opcion == 2:
            break
        elif opcion != 1 and 2:
            print("Sintax error")
            break

# ! /\|=\/