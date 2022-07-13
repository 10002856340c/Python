from ast import literal_eval
from msilib.schema import _Validation_records
from random import *
from random import randint
from asyncore import loop
from multiprocessing.spawn import old_main_modules
from random import random
from traceback import print_tb
from typing import Match


# OPERADORES DE COMPARACION

# verificar = "blanco" == "Blanco"
# print(verificar)------> false

# verificar2 = 100 != 99
# print(verificar2)------>True

# verificar3 = 5 < 9
# print(verificar3)------>True

# ------------------------------------------------------------------------------------------------------------------------

# EJERCICIO 1

# num1 = 36
# num2 = 17

# mi_bool = num1 >= num2

# print(mi_bool)

# ------------------------------------------------------------------------------------------------------------------------

# EJERCICIO 2

# import math

# num1 = math.sqrt(25)
# num2 = 5

# mi_bool = num1 == num2

# print(mi_bool)

# ------------------------------------------------------------------------------------------------------------------------

# OPERADORES LOGICOS COMPARACION
# and =  " y " ---> es decir se tienen que cumplir las dos funciones
# or = "o" ---->se puede cumpliar alguna de las dos funciones
# not = "no" ------> no se tiene que cumplir la funcion

# EJEMPLO1

# verificar = (50 == 50) and ("perro" == "gato")
# print(verificar)-------> en este ejemplo seria FALSE por que no se estan cumpliendo las dos condciones , si o si se tiene que cumplir las dos condiciones


# verificar2 = (50 == 40) or ("gato" == "gato")
# print(verificar2)------------> en este caso es TRUE por que aunque la primera condicion sea falsa la segunda condicion es verdadera , se cumple por lo menos una condicion


# EJEMPLO 2

# texto = "hola como estas"
# verificar = ("hola" in texto) or ("perro" in texto)-----> asignamos el operador "or" es decir es TRUE por que se cumple algunas de las dos condiciones
# print(verificar)


# EJEMPLO 3

# num1 = 36
# num2 = 72/2
# num3 = 48

# mi_bool = (num1 > num2) or (num1 < num3) and (num1 > num2) or (num1 < num3)

# print(mi_bool)


# EJEMPLO 4

# texto = " Cuando algo es lo suficientemente importante , lo haces incluso si las probabilidades de que salga bien no te acompañan "

# palabra1 = "éxito"
# palabra2 = "tecnología"

# mi_bool = not(palabra1 and palabra2) in texto
# print(mi_bool)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------

# CONTROL DE FLUJO


# existen controles de flujo como los siguientes
# if () -------->"si pasa esta condicion" --------> ejecutame este codigo
# else : --------> "y si no pasa esa condicion" --------> entonces ejecutame este codigo
# elif () --------> Se pueden verificar varias condiciones al incluir una o más verificaciones elif después de su declaración if inicial. Ten en cuenta que solo se ejecutará una condición


# EJEMPLO1

# mascota = "perro"

# if (mascota == "gato"):
# print("tienes un gato")

# else:
# print("no se que animal tienes")

# edad = int(input("Ingresa tu edad :"))
# calificaciones = int(input("¿ Cuanto sacaste en el examen ? :"))


# if(edad < 18):
# print("Eres menor de edad")

# else:
# print("eres mayor de edad")

# if(calificaciones >= 30):
# print("Aprobaste")
# else:
# print("No aprobaste")


# EJEMPLO 2:


# num1 = int(input("Ingresa un numero :"))
# num2 = int(input("Ingresa otro numero :"))

# if(num1 > num2):
# print(f"{num1} es mayor que {num2}")

# elif(num2 > num1):
# print(f"{num2} es mayor que {num1}")

# else:
# print(f"{num1} y {num2} son iguales")


# EJEMPLO 3

# edad = 16
# tiene_licencia = False

# if edad >= 18 and tiene_licencia:
# print("Puedes conducir")
# elif edad < 18:
# print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
# else:
# print("No puedes conducir. Necesitas contar con una licencia")


# EJEMPLO 4

# habla_ingles = True
# sabe_python = False

# if(habla_ingles == habla_ingles) and (sabe_python):
# print("Cumple con los requisitos para potularte")

# elif (not habla_ingles) and (not sabe_python):
# print("Necesitas tener conocimientos en ingles y en python")

# elif(not habla_ingles) and (sabe_python):
# print("necesitas conocimientos en ingles")

# else:
# print("para postularte necesitas saber programar en python")

# ----------------------------------------------------------------------------------------------------------------------------------------------------------

# LOOP FOR:-------->"por cada"


# EJEMPLO 1

# lista = ["a", "b", "c", "d"]

# for letra in lista: ------->"por cada letra en las lista"
# print("letra :" + letra)


# EJEMPLO 2

# lista = ["a", "b", "c", "d"]

# for letra in lista:
# numero_letra = lista.index(letra)+1
# print(f"la letra{numero_letra} : {letra}")


# EJEMPLO 3

# startswith() --------->El método comienza con () devuelve True si una cadena comienza con el prefijo (cadena) especificado. Si no, devuelve Falso.

# lista = ["pablo", "laura", "fede", "luisa", "julia"]

# for nombres in lista:
# if nombres.startswith("l"):  ----------> startswith() nos Sirvio para decirle al pograma que nos busque las palabras que empiezen con "L"  dentro de la lista
# print(nombres)


# EJEMPLO 4

# numeros = [1, 2, 3, 4, 5, 6]
# valor = 0

# for numero in numeros:
# valor = valor+numero
# print(valor)

# EJEMPLO 5

# dicc = {"clave1": "a", "clave2": "b", "clave3": "c"}

# for a, b in dicc.items(): items()--------> imprimir el diccionario completo con sus significados
# print(a, b)


# EJEMPLO 6

# alumnos_clase = ["Maria", "Jose", "Carlos","Martina", "Isabel", "Tomas", "Daniela"]

# for nombre in alumnos_clase:
# print("Hola " + nombre)


# EJEMPLO 7
# lista_numeros = [1, 5, 8, 7, 6, 8, 2, 5, 2,
# 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]
# suma_numeros = 0

# for valor in lista_numeros:
# suma_numeros = suma_numeros + valor
# print(suma_numeros)

# ---------------------------------------------------------------------------------------------------------------------------->

# LOOP WHILE ----------->"mientras"

# break ------> corta una funcion o un ciclo
# continue ------> da la opción de omitir la parte de un bucle en la que se activa una condición externa, pero continuar para completar el resto del bucle. Es decir, la iteración actual del bucle se interrumpirá, pero el programa volverá a la parte superior del bucle.
# pass ------>deja seguir o pasar el  codigo haci ya haya una funcion ya establecida

# 1 EJEMPLO

# monedas = 5

# while monedas > 0:
# print(f"tengo {monedas} monedas")
# break


# 2 EJEMPLO

# respuesta = "si"

# while respuesta == "si":
# respuesta = input("quieres seguir si o no ?")

# else:
# input("gracias")

# 3 EJEMPLO

"""numeros = 10

while numeros >= 0:
    print(numeros)
    numeros -= 1"""

# 4 EJEMPLO

"""numeros = 50

while numeros >= 0:
    if numeros % 5 == 0:
        print(numeros)
        numeros -= 1
    else:

        numeros -= 1"""

# 5 EJEMPLO


"""lista_numeros = [4, 5, 8, 7, 6, 9, 8, 2, 4,
                 5, 7, 1, 9, 5, 6, -1, -5, 6, -6, -4, -3]

for numero in lista_numeros:
    if numero >= 0:
        print(numero)
    else:
        break"""


# ---------------------------------------------------------------------------------------------------------------------------->

# RANGE

# 1 EJEMPLO

"""for numero in range(1, 101):
    print(numero)"""

# 2 EJEMPLO

"""mi_lista = list(range(2500, 2586))
print(mi_lista)"""

# 3 EJEMPLO

"""mi_lista = list(range(3, 301, 3))

print(mi_lista)"""

# 4 EJEMPLO


"""suma_cuadrados = 0
for numero in range(1, 16):
    suma_cuadrados += numero**2
print(suma_cuadrados)"""

# ------------------------------------------------------------------------------------------------------------------------------------->

# ZIP-------------->para hacer una combinacion de listas


# Ejemplo 1
"""nombres = ["Cristian", "Camilo", "Fabian"]
edades = [19, 18, 20]
paises = ["Colombia", "Mexico", "Argentina"]
combinacion = (list(zip(nombres, edades, paises)))

for nombre, edad, pais in combinacion:
    print(f"{nombre} tiene {edad} años y vive en {pais}")"""


# Ejemplo 2

"""capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

combinacion = list(zip(capitales, paises))

for capital, pais in combinacion:
    print(f"La capital de {pais} es {capital}")"""


# Ejemplo 3

"""marcas = ["nike", "adidas", "reebook", "puma"]
productos = ["zapatos", "sudaderas", "gorras", "chaquetas"]

mi_zip = list(zip(marcas, productos))"""


# Ejemplo 4

"""español = ["uno", "dos", "tres", "cuatro", "cinco"]
portugues = ["um", "dois", "três ", "quatro", "cinco"]
ingles = ["one", "two", "three", "four", "five"]
numeros = list(zip(español, portugues, ingles))"""

"""print(numeros)"""

# ------------------------------------------------------------------------------------------------------------------------------------->

# MAX Y MIN ------------------> "MAX" sirve para hayar el mayor y el min para hayar el menor de una listas, etc.

# primer ejemplo
"""numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(min(numeros))
print(max(numeros))"""

# 2 ejemplo

"""nombres = ["carlos", "cristian", "daniela"]

print(min(nombres))"""

# 3 Ejemplo

"""nombre = "Carlos"
# terner en cuenta que el min y el max funcionan alfabeticamente , es decir en este caso el min seria "a"y el max seria "s", pero si el str tiene alguna mayuscula lo va a leer como si fuera el primero
print(min(nombre.lower()))"""  # --------> lower()para pasar a minusculas

# ejemplo 4

"""dicc = {'num1': 5, 'num2': 10}

print(max(dicc.values()))#------> para escribir el significado de los diccionarios"""


# ejemplo 5

"""lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]

valor_maximo=max(lista_numeros)"""


# ejemplo 6
"""lista_numeros = [44542247, 21310, 2134747, 44556475,
                 121676, 6654067, 353254, 123134, 552512, 611665]

rango = max(lista_numeros)-min(lista_numeros)

print(rango)"""

# ejemplo 7

"""diccionario_edades = {"Carlos": 55, "María": 42, "Mabel": 78, "José": 44, "Lucas": 24, "Rocío": 35, "Sebastián": 19, "Catalina": 2, "Darío": 49}

edad_minima = (min(diccionario_edades.values()))
ultimo_nombre = (max(diccionario_edades))
print(edad_minima)
print(ultimo_nombre.lower())"""

# ------------------------------------------------------------------------------------------------------------------------------------->
# se deber importar desde la libreria de "random"
# RANDINT ------->su funcion es escojer un numero  al azar que este dentro del rango establecido
# UNIFORM------->su funcion es escojer un numero al azar  pero en tipo float es decir de forma decimal que este dentro del rango establecido
# RANDOM ------->random() retorna un punto flotante, un número pseudo-aleatorio dentro del rango [0, 1). Esto es, desde el 0 (Incluido) hasta el 1 pero sin incluirlo (excluido), el cual se puede escalar hasta el rango deseado.
# CHOICE ---------> La función choice(secuencia) elige un valor al azar en un conjunto de elementos. Cualquier tipo de datos  rable (tupla, lista, cadena, range) puede utilizarse como conjunto de elementos.
# SHUFFLE ----------> La función shuffle() 'mezcla' o cambia aleatoriamente el orden de los elementos de una lista antes de realizar la selección de alguno de ellos


# RANDINT
"""aleatorio = randint(1, 50)
print(aleatorio)"""

# UNIFORM
"""aleatorio = uniform(1, 5)
print(aleatorio)"""

# RANDOM
"""print(random())"""

# CHOICE
"""nombres = ["Cristian", "Camilo", "Fabian", "brayan"]
print(choice(nombres))"""

# SHUFFLE----> solo se puede utilizar en int y float , y no str
"""numeros = list(range(5, 50, 5))
shuffle(numeros)

print(numeros)"""

# ------------------------------------------------------------------------------------------------------------------------------------->


# Compresion de listas


# en este ejemplo quedaria de la siguiente manera

"""lista = []
palabra = "python"

for letra in palabra:
    lista.append(letra)

print(lista)"""


# pero con la compresion de lista querdaria mas efeiciente a la hora de querer ahorrar codigo

"""lista = [letra for letra in "python"]

print(lista)"""

# 2 ejemplo
"""lista = [numero for numero in range(0, 30, 5)]
print(lista)"""

# 3 Ejemplo tambien se pueden agregar condicionales if

"""lista = [numero for numero in range(1, 50, 5) if numero >= 10]
print(lista)"""

# Ejemplo tambien se pueden agregar condicionales if y else
"""lista = [numero if numero >= 10 else "no" for numero in range(1, 50, 5)]
print(lista)"""


# Ejemplo pasar a pies a metros

"""pies = [10, 20, 30, 40, 50]
metros = [numero*0.3048 for numero in pies]
print(metros)"""

# Ejemplo hallar la potencia de cada numero de la lista
"""valores = [1, 2, 3, 4, 5, 6, 9.5]

valores_cuadrado = [numero**2 for numero in valores]
print(valores_cuadrado)"""

# Ejemplo hallar los numeros pares de la lista
"""valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [numero for numero in valores if numero % 2 == 0]
print(valores_pares)"""


# Ejemplo hallar de grados fahrenheit a celcius
"""temperatura_fahrenheit = [32, 212, 275]
grados_celcius = [(numero-32) * (5/9) for numero in temperatura_fahrenheit]
print(grados_celcius)"""


"""cliente = {'nombre': 'cristian', 'edad': 19, 'ocupacion': 'programador'}

pelicula = {'titulo': 'matrix', 'ficha_tecnica': {
    'protagonista': 'cristian galeano', 'director': 'harol galeano'}}

elementos = [cliente, pelicula, "libro"]"""

# ------------------------------------------------------------------------------------------------------------------------------------->
# PROYECTO 4 ADIVINA EL NUMERO

intentos = 0
numeromin = 1
numeromax = 100

print("hola cual es tu nombre :")
usuario = input()
numero = (randint(numeromin, numeromax))

print(f"hola  {usuario} a continuacion vas adivinar el numero que estoy pensando del  {str(numeromin)} al {str(numeromax)}")


while intentos < 8:
    print("ingresa el numero :")
    ingreso = int(input())
    intentos = intentos + 1
    if ingreso < numero:
        print("!el numero es mayor!")

    elif ingreso > numero:
        print("! el numero es menor !")

    elif ingreso == numero:
        print("Felicitaciones incontraste el numero")
        print(f"y tus intentos fueron {intentos}")
        break

    if ingreso > numeromax:
        print("te saliste del rango del 1 - 100")

    elif ingreso < numeromin:
        print("no se acepta numeros negativos ")
else:
    print(f"se te acabaron los intentos , el numero pensado era {numero}")
    print("GAME OVER")
