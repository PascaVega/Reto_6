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

# ! /\|=\/