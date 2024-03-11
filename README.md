# Reto_6
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

def introducir():
    num1 : float = float(input("Ingrese el primer número. Ejemplo: 50.75: "))
    num2 : float = float(input("Ingrese el segundo número. Ejemplo: 50.75: "))
    num3 : float = float(input("Ingrese el tercer número. Ejemplo: 50.75: "))
    num4 : float = float(input("Ingrese el cuarto número. Ejemplo: 50.75: "))
    num5 : float = float(input("Ingrese el quinto número. Ejemplo: 50.75: "))
    desarrollo(num1,num2,num3,num4,num5)

def desarrollo(num1,num2,num3,num4,num5):
    numeros = [num1,num2,num3,num4,num5]
    numeros.sort()

    promedio = (num1+num2+num3+num4+num5)/5
    print(f"Promedio: {promedio}")

    if len(numeros) % 2 == 0:
        mediana : float  = (numeros[len(numeros)//2-1] + numeros[len(numeros)//2])/2
    else:
        mediana = numeros[len(numeros)//2]
    print(f"Mediana: {mediana}")

    promedio_multiplicativo : float = (num1*num2*num3*num4*num5)/5
    print(f"Promedio multiplicativo: {promedio_multiplicativo}")

    print(f"Números de forma ascendente: {numeros}")

    numeros.sort(reverse=True)
    print(f"Números de forma descendente: {numeros}")

    potencia : float = numeros[0]**numeros[-1]
    print(f"Potencia del mayor número elevado al menor número: {potencia}")

    raiz : float = num1 ** (1/3)
    print(f"La raiz cúbica del número menor: {raiz}")

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

<h2>Bibliografía</h2>
    <div class="bibliografia">
        <table>
            <tr>
                <th>Referencia</th>
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
        </table>
    </div>
