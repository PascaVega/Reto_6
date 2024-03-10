#RETO 6 - Parte 4
#Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno.
#Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.
import math

def introducir():
    panes : int = int(input("Ingrese el número de panes. Ejemplo 24: "))
    bolsas_leche : int = int(input("Ingrese el número de bolsas de leche. Ejemplo 23: "))
    huevos : int = int(input("Ingrese el número de huevos. Ejemplo 20: "))
    dinero : int = int(input("Ingrese el total de dinero qeu te dio tu mamá. Ejemplo: 10000. "))
    desarrollo(panes,bolsas_leche,huevos,dinero)
    return

def desarrollo(panes,bolsas_leche,huevos,dinero):
    total_panes : int = panes*300
    total_bolsas_leche : int = bolsas_leche*3300
    total_huevos : int = huevos*350
    cuenta : int = total_panes+total_bolsas_leche+total_huevos
    total : int = dinero-cuenta
    if total<0:
        total : int = abs(total)
        print(f"Se queda debiendo un valor de {total}, teniendo en cuenta de que la cuenta fue de {cuenta}")
        return
    elif total>0:
        print(f"La cuenta fue de {cuenta},por lo cual las vueltas son de {total}")
        return
    else:
        print(f"La cuenta de {total} fue pagada en su totalidad y no sobró dinero")
        return

def continuar():
    opcion : int = int(input("¿Desea continuar? Marque 1 (sí) o 2 (no): "))
    return opcion

if __name__ == "__main__":
    print("Programa para conocer las vueltas de las compras de panes, bolsas de leche y huevos")

    while True:
        introducir()
        opcion = continuar()
        if opcion == 2:
            break
        elif opcion != 1 and 2:
            print("Sintax error")
            break

# ! /\|=\/