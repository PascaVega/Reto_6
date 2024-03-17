# Reto_6
| Nombre                 | Identificación | Grupo | Trabajo          |
|------------------------|----------------|-------|------------------|
| Angélica Pascagaza Vega| 1031652163     |   5   | Trabajo individual |

<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 6 - Parte 1</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Desarrolle una función matemática para calcular el volumen y el área superficial. Además, cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h.</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Se tiene en cuenta el módulo <i>math</i> y la formula del volumen y perímetro de las figuras.</td>
  </tr>
</table>

**Parte 1** 
```python
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
```

<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 4 - Parte 2</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Desarrolle una función matemática para calcular el perímetro y el área de la figura. Además, cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r, a y b.</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Se tiene en cuenta el módulo <i>math</i> y la formula del área y perímetro de las figuras.</td>
  </tr>
</table>

**Parte 2**
```python
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
```

<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 4 - Parte 3</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Se crean pequeñas ecuaciones para la resolución del punto.</td>
  </tr>
</table>

**Parte 3**
```python
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
```

<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 4 - Parte 4</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Se plantean algunas ecuaciones y condiciones con desigualdades para determinar si se le dan vueltas o no.</td>
  </tr>
</table>

**Parte 4**
```python
#RETO 6 - Parte 4
#Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno.
#Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.

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
```

<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 4 - Parte 5</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Se parte de la formula del interés compuesto, se determina que se desea hallar el capital final y desde ahí se plantea todo el código.</td>
  </tr>
</table>

**Parte 5** 
```python
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
```

<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 4 - Parte 6</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Se plantea la siguiente función exponencial para resolver la situación:
      <p></p></P>$$C_t = c*2^d$$</p>
    </td>
  </tr>
</table>

**Parte 6** 
```python
#RETO 6 - Parte 6
#El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día.
#Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.

def introducir():
    dias : float = float(input("Ingrese el número de días transcurridos. Ejemplo 5: "))
    contagiados : float = float(input("Ingrese el número de contagiados iniciales. Ejemplo 24: "))
    desarrollo(dias,contagiados)
    return

def desarrollo(dias,contagiados):
    contagiados_finales = contagiados*2**dias
    print(f"El numero de contagiados después de {dias} dia(s) es de {contagiados_finales}")
    return

def continuar():
    opcion : int = int(input("¿Desea continuar? Marque 1 (sí) o 2 (no): "))
    return opcion

if __name__ == "__main__":
    print("Programa para determinar el número de contagiados de COVID-19")

    while True:
        introducir()
        opcion = continuar()
        if opcion == 2:
            break
        elif opcion != 1 and 2:
            print("Sintax error")
            break

# ! /\|=\/
```

<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 6 - Parte 7</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
  <td style="color:#141414" align="center">Escriba un programa que pida 5 números reales y calcule las siguientes operaciones:
        <li>El promedio</li>
        <li>La mediana</li>
        <li>El promedio multiplicativo </li>
        <li>Ordenar los números de forma ascendente</li>
        <li>Ordenar los números de forma descendente</li>
        <li>La potencia del mayor número elevado al menor número</li>
        <li>La raíz cúbica del menor número</li>
   </td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Para este punto, primero se ordenan los números de forma ascendente en una lista, a partir de ahí se van ejecutando las operaciones correspondientes.</td>
  </tr>
</table>

**Parte 7** 
```python
#Taller 1 - Punto 7
#Escriba un programa que pida 5 números reales y calcule las siguientes operaciones: 
#Promedio, mediana, promedio multiplicativo, ordenar los números de forma ascendente, ordenar los números de forma descendente, potencia del mayor número elevado al menor número, raíz cúbica del menor número.
from funciones import ordenar_numeros

def introducir():
    num1 : float = float(input("Ingrese el primer número. Ejemplo: 50.75: "))
    num2 : float = float(input("Ingrese el segundo número. Ejemplo: 50.75: "))
    num3 : float = float(input("Ingrese el tercer número. Ejemplo: 50.75: "))
    num4 : float = float(input("Ingrese el cuarto número. Ejemplo: 50.75: "))
    num5 : float = float(input("Ingrese el quinto número. Ejemplo: 50.75: "))
    numeros = ordenar_numeros(num1,num2,num3,num4,num5)
    desarrollo(num1,num2,num3,num4,num5,numeros)

def promedio(num1,num2,num3,num4,num5):
    promedio = (num1+num2+num3+num4+num5)/5
    print(f"Promedio: {promedio}")
    return

def mediana(numeros):
    if len(numeros) % 2 == 0:
        mediana : float  = (numeros[len(numeros)//2-1] + numeros[len(numeros)//2])/2
    else:
        mediana = numeros[len(numeros)//2]
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
```

**Ordenar los números** 
```python
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
```


<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 6 - Parte 8</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
  <td style="color:#141414" align="center">Para el punto anterior incluir las funciones en un archivo independiente e importarlas para su uso.</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Se reutilizo completamente el código anterior y se modificó de tal forma que la mayoría de las funciones se encuentran en un archivo diferente al principal.</td>
  </tr>
</table>

**Parte 8** 
```python
#Reto 6 - Punto 8
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
```

**Ordenar los números** 
```python
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
    if len(numeros) % 2 == 0:
        mediana : float  = (numeros[len(numeros)//2-1] + numeros[len(numeros)//2])/2
    else:
        mediana = numeros[len(numeros)//2]
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
```


<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 6 - Parte 9</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
   <td style="color:#141414" align="center">Consultar qué es y cómo funciona pip en python.</td>
  </tr>
  <tr bgcolor="#e4e4ed">
   <td style="color:#141414" align="center">
        <li>PIP --> Python Package Index</li>
        <li>Es el sistema de gestión de paquetes de Python.</li>
        <li>Es una herramienta que facilita la <i>instalación</i>, <i>actualización</i> y <i>gestión de paquetes</i> y <i>dependencias</i> de <ins>Python</ins>.</li>
        <li>Permite a los usuarios instalar <b>paquetes</b> de Python desde el <i>Python Package Index (PyPI)</i> y otros repositorios de paquetes.</li>
   </td>
  </tr>
  <tr bgcolor="#e4e4ed">
   <td style="color:#141414" align="center"><b>Instalación de PIP:</b>
        <li>El PIP generalmente se instala automáticamente cuando se instala Python en el sistema. Sin embargo, si no se encuentra instalado, se puede instalar manualmente descargando el archivo de instalación desde <i>PyPI</i> e instalándolo.</li>
   </td>
  </tr>
    <tr bgcolor="#e4e4ed">
   <td style="color:#141414" align="center"><b>Uso básico:</b>
        <li>Para <ins>instalar un paquete</ins>, se puede usar el comando pip install <i><nombre_del_paquete></i>. Esto descargará e instalará el paquete especificado desde <i>PyPI</i>.</li>
        <li>Para <ins>instalar una versión específica</ins> de un paquete, se puede especificar la versión con <i>pip install <nombre_del_paquete>==<versión></i>.</li>
        <li>Para <ins>actualizar</ins> un paquete a la última versión disponible, se puede usar <i>pip install --upgrade <nombre_del_paquete></i>.</li>
        <li>Para <ins>desinstalar</ins> un paquete, se puede utilizar <i>pip uninstall <nombre_del_paquete></i>.</li>
   </td>
  </tr>
  <tr bgcolor="#e4e4ed">
   <td style="color:#141414" align="center"><b>Requerimientos de instalación:</b>
        <li>PIP puede leer archivos de requisitos (como <i>requirements.txt</i>) que enumeran todos los paquetes necesarios para una aplicación.</li>
        <li>Se pueden instalar todos los paquetes enumerados en un archivo de requisitos con el comando <i>pip install -r requirements.txt.</i></li>
   </td>
  </tr>  
    <tr bgcolor="#e4e4ed">
   <td style="color:#141414" align="center"><b>Entornos virtuales:</b>
        <li>PIP es comúnmente utilizado en conjunción con <ins>entornos virtuales</ins> de Python. Estos entornos virtuales permiten aislar las dependencias de cada proyecto, lo que evita conflictos entre versiones de paquetes.</li>
        <li>Se puede crear un entorno virtual utilizando <i>virtualenv</i> o el módulo <i>venv</i> de Python.</li>
   </td>
  </tr> 
  </tr>  
    <tr bgcolor="#e4e4ed">
   <td style="color:#141414" align="center"><b>Otros repositorios:</b>
        <li>PyPI es el repositorio predeterminado para los paquetes de Python, pero PIP también puede trabajar con otros repositorios de paquetes.</li>
        <li>Se puede especificar el repositorio utilizando la opción <i>--index-url</i> o configurando opciones en un archivo de configuración.</li>
   </td>
  </tr>    
</table>

<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 6 - Parte 10</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Hacer un listado de módulos populares para python que se puedan instalar com pip y consultar cómo instalarlos.</td>
  </tr>
  <tr bgcolor="#e4e4ed">
   <td style="color:#141414" align="center"><b>numpy</b>
        <li>Biblioteca fundamental para computación numérica en Python.</li>
        <li><i>pip install numpy</i></li>
   </td>
  </tr>
    <tr bgcolor="#e4e4ed">
   <td style="color:#141414" align="center"><b>pandas</b>
        <li>Biblioteca para manipulación y análisis de datos en Python.</li>
        <li><i>pip install pandas</i></li>
   </td>
  </tr>
    </tr>
    <tr bgcolor="#e4e4ed">
   <td style="color:#141414" align="center"><b>matplotlib</b>
        <li>Biblioteca para crear visualizaciones estáticas, interactivas y animadas en Python.</li>
        <li><i>pip install matplotlib</i></li>
   </td>
  </tr>
    <tr bgcolor="#e4e4ed">
   <td style="color:#141414" align="center"><b>scikit-learn</b>
        <li>Biblioteca de aprendizaje automático para Python que proporciona algoritmos de clasificación, regresión, agrupación, entre otros.</li>
        <li><i>pip install scikit-learn</i></li>
   </td>
  </tr>
    <tr bgcolor="#e4e4ed">
   <td style="color:#141414" align="center"><b>tensorflow</b>
        <li>Biblioteca de aprendizaje automático de código abierto desarrollada por Google para construir y entrenar modelos de redes neuronales.</li>
        <li><i>pip install tensorflow</i></li>
   </td>
  </tr>
    </tr>
    <tr bgcolor="#e4e4ed">
   <td style="color:#141414" align="center"><b>keras</b>
        <li>API de alto nivel para construir y entrenar modelos de aprendizaje profundo en Python.</li>
        <li><i>pip install keras</i></li>
   </td>
  </tr>
      <tr bgcolor="#e4e4ed">
   <td style="color:#141414" align="center"><b>requests</b>
        <li>Biblioteca HTTP para Python que permite enviar solicitudes HTTP/1.1 con Python.</li>
        <li><i>pip install requests</i></li>
   </td>
  </tr>
    <tr bgcolor="#e4e4ed">
   <td style="color:#141414" align="center"><b>beautifulsoup4</b>
        <li>Biblioteca para extraer datos de archivos HTML y XML.</li>
        <li><i>pip install beautifulsoup4</i></li>
   </td>
  </tr>
    <tr bgcolor="#e4e4ed">
   <td style="color:#141414" align="center"><b>django</b>
        <li>Framework web de Python de alto nivel que fomenta el desarrollo rápido y el diseño limpio y pragmático.</li>
        <li><i>pip install django</i></li>
   </td>
  </tr>
    </tr>
    <tr bgcolor="#e4e4ed">
   <td style="color:#141414" align="center"><b>flask</b>
        <li>Framework web ligero de Python para construir aplicaciones web rápidas y escalables.</li>
        <li><i>pip install flask</i></li>
   </td>
  </tr>
</table>


<h2>Bibliografía</h2>
    <div class="bibliografia">
        <table>
            <tr>
                <th>Referencias</th>
            </tr>
            <tr>
                <td>Varsity Tutors. (s.f.). Volumen de una esfera. Recuperado el 10 de marzo de 2024, de https://www.varsitytutors.com/hotmath/hotmath_help/spanish/topics/volume-of-a-sphere<a href="https://www.varsitytutors.com/hotmath/hotmath_help/spanish/topics/volume-of-a-sphere"></a></td>
            </tr>
            <tr>
                <td>Varsity Tutors. (s.f.). Volumen de un cono. Recuperado el 10 de marzo de 2024, de https://www.varsitytutors.com/hotmath/hotmath_help/spanish/topics/volume-of-a-cone<a href="https://www.varsitytutors.com/hotmath/hotmath_help/spanish/topics/volume-of-a-cone"></a></td>
            </tr>
            <tr>
                <td>Varsity Tutors. (s.f.). Área de superficie de una esfera. Recuperado el 10 de marzo de 2024, de https://www.varsitytutors.com/hotmath/hotmath_help/spanish/topics/surface-area-of-a-sphere<a href="https://www.varsitytutors.com/hotmath/hotmath_help/spanish/topics/surface-area-of-a-sphere"></a></td>
            </tr>
            <tr>
                <td>Varsity Tutors. (s.f.). Área de superficie de un cono. Recuperado el 10 de marzo de 2024, de https://www.varsitytutors.com/hotmath/hotmath_help/spanish/topics/surface-area-of-a-cone<a href="https://www.varsitytutors.com/hotmath/hotmath_help/spanish/topics/surface-area-of-a-cone"></a></td>
            </tr>
            <tr>
                <td>Gerencie.com. (s.f.). Cómo calcular el interés compuesto. Recuperado el 10 de marzo de 2024, de https://www.gerencie.com/como-calcular-el-interes-compuesto.html<a href="https://www.gerencie.com/como-calcular-el-interes-compuesto.html"></a></td>
            </tr>
            <tr>
                <td>Python Packaging User Guide. (2024). Installing Packages. Recuperado el 17 de marzo de 2024, de https://packaging.python.org/en/latest/tutorials/installing-packages/<a href="https://packaging.python.org/en/latest/tutorials/installing-packages/"></a></td>
            </tr>
            <tr>
                <td>IMMUNE Technology Institute. (2022). Librerías de Python, ¿qué son y cuáles son las mejores? Recuperado el 17 de marzo de 2024, de https://immune.institute/blog/librerias-python-que-son/<a href="https://immune.institute/blog/librerias-python-que-son/"></a></td>
            </tr>
            <tr>
                <td>Michigan Technological University. (s.f.). Installing, uninstalling, or upgrading Python modules using Pip (Linux - RHEL7). Recuperado el 17 de marzo de 2024, de https://servicedesk.mtu.edu/TDClient/1801/Portal/KB/ArticleDet?ID=66715<a href="https://servicedesk.mtu.edu/TDClient/1801/Portal/KB/ArticleDet?ID=66715"></a></td>
            </tr>
            <tr>
                <td>El Libro De Python. (s.f.). Módulos en Python. Recuperado el 17 de marzo de 2024, de https://ellibrodepython.com/modulos-python<a href="https://ellibrodepython.com/modulos-python"></a></td>
            </tr>
        </table>
    </div>
