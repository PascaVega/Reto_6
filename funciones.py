#Funciones

def ordenar_numeros(num1,num2,num3,num4,num5):
    # Encontrar el primer número más pequeño y asignarlo a la primera posición
    if num1 < num2 and num1 < num3 and num1 < num4 and num1 < num5:
        numeros = [num1, 0, 0, 0, 0]
    elif num2 < num1 and num2 < num3 and num2 < num4 and num2 < num5:
        numeros = [num2, 0, 0, 0, 0]
    elif num3 < num1 and num3 < num2 and num3 < num4 and num3 < num5:
        numeros = [num3, 0, 0, 0, 0]
    elif num4 < num1 and num4 < num2 and num4 < num3 and num4 < num5:
        numeros = [num4, 0, 0, 0, 0]
    else:
        numeros = [num5, 0, 0, 0, 0]

    # Encontrar el segundo número más pequeño y asignarlo a la segunda posición
    if (num1 <= num2 and num1 <= num3 and num1 <= num4 and num1 <= num5) or numeros[0] == num1:
        if num2 <= num3 and num2 <= num4 and num2 <= num5:
            numeros[1] = num2
        elif num3 <= num2 and num3 <= num4 and num3 <= num5:
            numeros[1] = num3
        elif num4 <= num2 and num4 <= num3 and num4 <= num5:
            numeros[1] = num4
        else:
            numeros[1] = num5
    elif num2 <= num1 and num2 <= num3 and num2 <= num4 and num2 <= num5:
        if num1 <= num3 and num1 <= num4 and num1 <= num5:
            numeros[1] = num1
        elif num3 <= num1 and num3 <= num4 and num3 <= num5:
            numeros[1] = num3
        elif num4 <= num1 and num4 <= num3 and num4 <= num5:
            numeros[1] = num4
        else:
            numeros[1] = num5
    elif num3 <= num1 and num3 <= num2 and num3 <= num4 and num3 <= num5:
        if num1 <= num2 and num1 <= num4 and num1 <= num5:
            numeros[1] = num1
        elif num2 <= num1 and num2 <= num4 and num2 <= num5:
            numeros[1] = num2
        elif num4 <= num1 and num4 <= num2 and num4 <= num5:
            numeros[1] = num4
        else:
            numeros[1] = num5
    elif num4 <= num1 and num4 <= num2 and num4 <= num3 and num4 <= num5:
        if num1 <= num2 and num1 <= num3 and num1 <= num5:
            numeros[1] = num1
        elif num2 <= num1 and num2 <= num3 and num2 <= num5:
            numeros[1] = num2
        elif num3 <= num1 and num3 <= num2 and num3 <= num5:
            numeros[1] = num3
        else:
            numeros[1] = num5
    else:
        if num1 <= num2 and num1 <= num3 and num1 <= num4:
            numeros[1] = num1
        elif num2 <= num1 and num2 <= num3 and num2 <= num4:
            numeros[1] = num2
        elif num3 <= num1 and num3 <= num2 and num3 <= num4:
            numeros[1] = num3
        else:
            numeros[1] = num4

# Encontrar el tercer número más pequeño y asignarlo a la tercera posición
    for i in range(2, 5):
        if numeros[i] == 0:
            smallest_remaining = min([num for num in [num1, num2, num3, num4, num5] if num not in numeros])
            numeros[i] = smallest_remaining

    return numeros

def promedio(num1,num2,num3,num4,num5):
    promedio = (num1+num2+num3+num4+num5)/5
    print(f"Promedio: {promedio}")
    return

def mediana(numeros):
    mediana = numeros[2]
    print(f"Mediana: {mediana}")
    return

def promedio_multiplicativo(num1,num2,num3,num4,num5):
    promedio_multiplicativo : float = (num1*num2*num3*num4*num5)/5
    print(f"Promedio multiplicativo: {promedio_multiplicativo}")
    return

def ascendente(numeros):
    print(f"Números de forma ascendente: {numeros}")
    return

def descendente(numeros):
    numeros.sort(reverse=True)
    print(f"Números de forma descendente: {numeros}")
    return

def potencia(numeros):
    potencia : float = (numeros[0])**numeros[-1]
    print(f"Potencia del mayor número elevado al menor número: {potencia}")
    return

def raiz(numeros):
    numero_menor = numeros[4]
    raiz : float = numero_menor ** (1/3)
    print(f"La raiz cúbica del número menor: {raiz}")
    return

# ! /\|=\/
