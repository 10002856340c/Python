from operator import index
from os import lstat
import pandas as pd
import numpy as np

# EJERCICIO 1


# print("por favor digite un numero")

# a = int(input("digite un primer numero :"))
# b = int(input("digite el segundo numero : "))

# if(a != b):
# print(f"el numero {a} y el numero {b} son diferentes")
# else:
# print("son iguales")


# EJERCICIO 2


# num1 = int(input("ingresa el primer numero :"))
# num2 = int(input("ingresa el segundo numero :"))

# multiplicacion = num1*num2
# division = num1/num2
# Resta = num1-num2
# suma = num1+num2
# raiz = (num1+num2)**0.5
# potencia = num1**num2
# modulo = num1 % num2

# print(f"la suma del{num1} y el numero {num2} es {suma}")
# print(f"la resta del{num1} y el numero {num2} es {Resta}")
# print(f"la multiplicacion del{num1} y el numero {num2} es {multiplicacion}")
# print(f"la division del{num1} y el numero {num2} es {division}")
# print(f"la potencia entre el numero{num1} y el numero {num2} es {potencia}")
# print(f"la el modulo entre el numero {num1} y el numero {num2} es {modulo}")
# print(f"la raiz entre  {num1} y el numero {num2} es {raiz}")


# EJERCICIO 3

"""numero = int(input("ingrese un numero"))

if numero < 0:
    print("el numero debe ser positivo ")
else:
    if ((numero // 2)*2) == numero:
        print(f"el numero {numero} es par")
    else:
        print(f"el numero {numero} no es par ")"""

# EJERCICIO 4

"""usuario = int(input("ingrese un numero :"))
rango = range(1, usuario)
contador = 0

for i in rango:
    if usuario % i == 0:
        contador = contador+1
if contador > 2:
    print("No es primo")
else:
    print("si es primo")"""

# EJERCICIO 5
# FUNCIONES


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->
# RETO 1 EN EL BOOT

"""def CDT(usuario: str, capital: int, tiempo: int):
    if tiempo > 2:
        valor_intereses = ((capital*0.03*tiempo)/12)
        valor_total = valor_intereses+capital
        return f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valor_total}"
    else:
        valor_aperder = (capital*0.02)
        valor_total = capital-valor_aperder

        return f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valor_total}"


print(CDT("AB1012", 1000000, 3))"""

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->


# RETO1 CRISTIAN

"""def CDT(usuario: str, capital: int, tiempo: int):
    if tiempo > 2:
        valor_intereses = round(((capital*0.03*tiempo)/12))
        return valor_intereses+capital
    else:
        valor_aperder = round(capital*0.02)
        valor_total = capital-valor_aperder
        return valor_total


usuario = input("digite su usuaurio :")
capital = int(input("digite su capital :"))
tiempo = int(input("digite su tiempo estimado en meses  :"))
respuesta = CDT(usuario, capital, tiempo)

print(f"Para el  usuario{usuario} La cantidad de dinero a recibir , segun el monto inicial de  {capital} COP para un tiempo de {tiempo} meses es de : {respuesta} COP")"""


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->


# mayores y menor de una lista con las funciones
# min()---------------------> el minimo de una lista de numeros tipo int
# max()----------------------> el maximo de un numero de una lista de tipo int
"""lista = [1, 2, 3, 4, 5]

print(
    f"el mayor de la lista es : {max(lista)} y el menor de la lista es {min(lista)}")"""

# ----------------------------------------------------------------------------------------------------------------------------                         >


"""def sumar(lista: list):
    return print(f"la suma de los elementos de la lista son {sum(lista)}")


lista = (sumar([1, 2, 3, 4, 5]))"""


# CONVERTIDOR DE LIBRAS A KIILOGRAMOS------------------------------------------------------------------------------------------------------------------------------>

# PRIMERA FORMA DE HACERLO

"""libras = int(input("ingrese su peso en libras "))
conversion = round(libras * 0.453592)

print(f"su peso en kilogramos es {conversion} kilogramos")"""

# SEGUNDA  FORMA DE HACERLO

"""def conversion(pesoL: float):
    pesokg = round((pesoL*0.453592))
    return print(f"su peso en kilogramos es de {pesokg} kilogramos")


pesoL = int(input("Digite su peso en Libras"))
conversion(pesoL)"""
# ------------------------------------------------------------------------------------------------------------------------------>

"""adyacente = int(input("digite el cateto Adyacente :"))
opuesto = int(input("Digite el cateto opuesto :"))
hipotenusa = round(((adyacente**2+opuesto**2))**0.5)
print(
    f"el cateto adyacente del triangulo es de {adyacente} cm y el cateto opuesto es de {opuesto} cm ")
print(f"por lo tanto la hipotenusa del triangulo es de {hipotenusa} cm")"""


"""def hipotenusa(adyacente: int, opuesto: int):
    formula = round(((adyacente**2+opuesto**2))**0.5)
    return print(
        f"el cateto adyacente del triangulo es de {adyacente} cm y el cateto opuesto es de {opuesto} cm , por lo tanto la hipotenusa es de {formula} cm")


adyacente = int(input("ingrese cateto adyacente :"))
opuesto = int(input("ingrese cateto opuesto :"))

hipotenusa(adyacente, opuesto)"""

# ------------------------------------------------------------------------------------------------------------------------------------>

# Ejercicio Menu convertir de millas a kilometros y de kilometros a millas


"""def conversionMl_KM(millas: float):
    formula = round((millas*1.609334), 2)
    return print(f"las millas fueron convertidas a {formula} Km")


def conversionKM_MI(kilometros: float):
    formula = round((kilometros*0.621371), 2)
    return print(f"los kilometros en millas son {formula} millas")


menu = input('**********************Menu opciones*********************** \n'
             'Digite la Opcion a Elegir \n'

             '1 -  Convertir de millas a kilometros\n'
             '2 - Convertir de kilometros a millas\n'
             '0 - Salir')


while menu != 0:
    if menu == "1":
        print('***************Has Ingresado al menu 1**********************\n')
        millas = int(input("ingrese las millas : "))
        conversionMl_KM(millas)
        break
    elif menu == "2":
        print('***************Has Ingresado al menu 2**********************\n')
        kilometros = int(input("ingrese los kilometros : "))
        conversionKM_MI(kilometros)
        break
    else:
        print("Por favor digite un numero valido que este dentro del Menu\n")
        menu = input('**********************Menu opciones*********************** \n'
                     'Digite la Opcion a Elegir \n'

                     '1 -  Convertir de millas a kilometros\n'
                     '2 - Convertir de kilometros a millas\n'
                     '0 - Salir')"""


# ------------------------------------------------------------------------------------------------------------------------------------------>

# Ejercicio de  condiciones en cascadas


"""numero = int(input("Ingresa un numero :"))

if numero < 0:
    numero = numero*(-1)

if numero >= 1 and numero <= 9:
    print("EL numero tiene 1 digito")
else:
    if numero > 9 and numero < 99:
        print("El numero tiene 2 digitos")
    else:
        if numero > 99 and numero < 1000:
            print("el numero es de 3 digitos")
        else:
            numero > 1000 and numero < 10000
            print("el numero tiene 4 digitos")
            if numero > 10000:
                print(f"el numero {numero} tiene mas de 4 digitos ")"""


# ------------------------------------------------------------------------------------------------------------------------------------------>

# BOOLEANOS

"""var = 1
var2 = 2

if var > 0 and var2 < 0:
    print("es verdadero")
else:
    print("no es verdadero")"""

# ------------------------------------------------------------------------------------------------------------------------------------------>

# try and except -----> si queremos que nos muestre enla pantalla lo que quertemos con try y si llega a pasar un erro o algo que no concuerde lo hacemos con un except

"""try:
    temperatura = float(input("ingrese la temperatura"))
except:
    print("esta ingresando letras ")


print(f"el numero ingresado para la temperatura es {temperatura}")"""

# ------------------------------------------------------------------------------------------------------------------------------------------>
# para seleccionar una palabra o el numero de letra que queramos en una lista o en str utilizamos[n:n]
"""fruta = "banana"
print(fruta[0:3])
print(fruta[2:4])"""

# ------------------------------------------------------------------------------------------------------------------------------------------>

# para hallar si una palabra de tipo str aparece en el texto planteado

"""fruta = "banana"
bool = "x" in fruta"""

"""print(bool)"""

# ------------------------------------------------------------------------------------------------------------------------------------------>
# metodo DIR()--->para mirar cuantos tipo de funciones se puede utilizar en dicho valor ya sea float str y int

"""a = "hola"
print(dir(a))"""

# ------------------------------------------------------------------------------------------------------------------------------------------>
# Anidaciones
"""a = " " "hola"
b = " " "como"
c = " " "estas"
d = a+b+c
print(d)"""
# ------------------------------------------------------------------------------------------------------------------------------------------>
# diccionarios RETORNANDO DICCIONARIOS CON FUNCIONES


# ejemplo promedio de notas PROFESORA
"""dicnotas = {'Estudiante': 'Cristian Smith Galeano Sanchez ',
            'nota1': 3.0, 'nota 2': 5.0, 'nota 3': 2.5, 'nota 4': 4.2}


def reporte_notas(dicnotas: dict):
    sumatoria = 0
    sumatoria += dicnotas['nota1']
    sumatoria += dicnotas['nota 2']
    sumatoria += dicnotas['nota 3']
    sumatoria += dicnotas['nota 4']
    promedio = sumatoria/4
    resultadoPromedio = {
        'Estudiante': dicnotas['Estudiante'], 'promedio': promedio}
    return resultadoPromedio


print(reporte_notas(dicnotas))"""


# ejercicio promedio de notas CRISTIAN

"""dicnotas = {'Estudiante': 'Cristian Smith Galeano Sanchez ',
            'nota1': 3.0, 'nota 2': 5.0, 'nota 3': 2.5, 'nota 4': 4.2}


def reporte_notas(dicnotas: dict):
    nota1 = dicnotas['nota1']
    nota2 = dicnotas['nota 2']
    nota3 = dicnotas['nota 3']
    nota4 = dicnotas['nota 4']

    promedio = round(((nota1+nota2+nota3+nota4)/4), 2)
    resultado = {'Estudiante': dicnotas['Estudiante'], 'promedio': promedio}
    return resultado


print(reporte_notas(dicnotas))"""


# ------------------------------------------------------------------------------------------------------------------------------------------>
"""padres = []
hijos = []
rango = range(0, 3)

for i in rango:
    nombrepadre = input("Por favor digite el nombre del padre :")
    nombreMadre = input("Nombre de la madre")
    padres.append([nombrepadre, nombreMadre])
    cantidadhijos = int(input("Cuantos hijos tiene la familia :"))
    rangohijos = range(0, cantidadhijos)

    for j in rangohijos:
        hijos.append([])
        nombreshijos = input("ingrese el nombre de sus hijos :")
        hijos[i].append(nombreshijos)

print(padres)
print(hijos
      )

for i in rango:
    print(f"Nombre del padre {padres[i][0]}")
    print(f"El nombre de la madre {padres[i][1]}")
    for j in range(len(hijos[i])):
        print(f"hijo (a) : {hijos[i][j]}")

print("Acontinuacion encontara rl listado de los padres con sus respectivos hijos :")

for i in rango:
    print(f"el nombre del padre{padres[i][0]}")
    print(f"cantidad  de los hijos{len(hijos[i])}")"""


# ------------------------------------------------------------------------------------------------------------------------------------->

# TUPLAS

# tuplas = ('a', 'b')
# tupla2 = 1, 2, 3, 4, 5, 6


# print(tuplas[0])# ------> ASI SE HACE PARA IMPRIMIR UN ELEMENTO EN ESPECIFICO SEGUN SU POSICION

# print(tupla2[3])# ------> ASI SE HACE PARA IMPRIMIR UN ELEMENTO EN ESPECIFICO SEGUN SU POSICION

# modificada = ('A',)+tuplas[1:]# ------> ASI SE HACE PARA CAMBIAR UN ELEMENTO DE UNA TUPLA  SEGUN LA POSICION EN LA QUE SE ENCUENTRE
# print(modificada)

# ------------------------------------------------------------------------------------------------------------------------------------->
# SETS:

# lista = [1, 2, 3, 4, 5, 6]
# conjunto = {True, 2022, 'hola', 25.36}
# ------------------------------------------------------------------------------------------------------------------------------------->

# dic1 = {'clave1': 'Cristian', 'clave2': {'clave3': 'hola'}}

# print(dic1['clave2'][])
# ------------------------------------------------------------------------------------------------------------------------------------->


salirmenu = True

tareas = {'01': {'descripcion': 'ir a mercar', 'estado': 'pendiete', 'tiempo': 60},
          '02': {'descripcion': 'Estudiar', 'estado': 'pendiete', 'tiempo': 100},
          '03': {'descripcion': 'Hacer ejercicio', 'estado': 'pendiete', 'tiempo': 50}}


def adicionar_tareas(tareas, descripcion, tareanueva):  # ---> Funcion adicionar tareas
    tareas[descripcion] = tareanueva
    return tareas


def consultar_tareas(tareas):  # ---> Funcion consultar tareas
    for descripcion, tarea in tareas.items():

        # --> Esta expresion se hace para quitarle el salto de linea , y no aparezca de forma saltada en la terminal
        print(descripcion, '-', end='')
        for atributo in tarea.values():
            print(atributo, '-', end='')
        print()


def actualizar_tareas(identificador, tareas):
    actualizar = set(tareas)
    if identificador in actualizar:
        return True
    else:
        return False


def adicionar_tareas(tareas, identificador):
    nuevaDescripcion = str(input("Digite la nueva descripcion :"))
    nuevoEstado = str(input("Digite el nuevoEstado :"))
    nuevoTiempo = int(input("Digite el nuevo Tiempo :"))
    tareas[identificador]['descripcion'] = nuevaDescripcion
    tareas[identificador]['estado'] = nuevoEstado
    tareas[identificador]['tiempo'] = nuevoTiempo


def eliminar_tarea(tareas, identificador):
    conjuntoidentificadores = set(tareas.keys())
    if identificador in conjuntoidentificadores:
        tareas.pop(identificador)
    else:
        print("no se ha encontrado la tarea con ese identificador :")


while salirmenu:
    print("***********************Menu de opciones********************\n"
          "1) Adicionar tareas \n"
          "2) Consultar Tarea \n"
          "3) Actualizar Tareas\n"
          "4) Eliminar Tarea \n"
          "5)Salir")
    opcionMenu = int(input("Ingrese la opcion a Elegir :"))

    if opcionMenu == 1:
        print("***********Adicionar tareas****************")
        descripcion = (input("Ingrese la descripcion :"))
        estado = (input("ingres el estado :"))
        tiempo = int(input("ingrese el tiempo :"))
        diccionario = {'descripcion': descripcion,
                       'estado': estado, 'tiempo': tiempo}
        a = adicionar_tareas(tareas, descripcion, diccionario)

    elif opcionMenu == 2:
        print("***********Consultar Tareas****************")
        a = consultar_tareas(tareas)

    elif opcionMenu == 3:
        print("***********Actualizar Tareas*****************")
        identificador = str(
            input("ingrese el identificador de la tarea a actualizar :"))
        if actualizar_tareas(identificador, tareas):
            adicionar_tareas(tareas, identificador)

        else:
            print("No ha sido encontrada la tarea con ese identificador")

    elif opcionMenu == 4:
        print("********** Eliminar Tarea********************")
        identificador = str(
            input("por favor ingrese el identificador a eliminar :"))
        b = eliminar_tarea(tareas, identificador)

    elif opcionMenu == 5:
        print("************Salir menu**********************")
        print("Has salido del sistema")
        break

    else:
        print("no has elejido ninguna opcion")
        salirmenu = False

# ----------------------------------------------------------------------------------------------------------------------------

# Clase 26 / 05 / 2022


# CONVERSION DE CADENAS ----> LISTAS
# split() tiene la funcion de pasar tu texto separado por palabras y NO por letras a una lista

"""cadena = ("hola como estas")

lista= cadena.split()
print(lista)"""


# CONVERSION DE CADENAS---> TUPLAS
"""cadena = "hola como estas "
conversion = tuple(cadena)
print(conversion)"""

# CONVERSION DE CADENAS----> CONJUNTOS(SETS)

"""cadena = "hola como estas"
conversion = set(cadena)
print(conversion)"""

# CONVERSION DE LISTAS ---> CADENAS


"""lista = ["h", "o", "l", "a"]
cadena = "".join(lista)
# No se puede convertir una lista de numeros a cadenas ya que solo se pueden de tipo str
print(cadena)"""

# CONVERSION DE LISTAS ---> TUPLAS
"""lista = ["h", "o", "l", "a"]
tupla = tuple(lista)
print(tupla)"""

# CONVERSION DE LISTAS ---> CONJUNTOS(SETS)
"""lista = ["h", 2, "o", "l"]
sets = set(lista)
print(sets)"""

# CONVERSION DE TUPLAS--->CADENAS
"""tupla = ('h', 'o', 'l', 'a')
print(type(tupla))
cadena = "".join(tupla)
print(cadena)"""

# CONVERSION DE TUPLAS---> LISTA

"""tupla = ('h', 'o', 'l', 'a')
lista = list(tupla)
print(lista)"""

# CONVERSION DE TUPLAS --->CONJUNTOS

"""tupla = ('h', 'o', 'l', 'a')
conjunto = set(tupla)
print(conjunto)"""

# CONVERSION DE CONJUNTOS ---> CADENAS
"""conjunto = {'h', 'o', 'l', 'a'}
cadenas = "".join(conjunto)
print(cadenas)"""


# CONVERSION DE CONJUNTOS ---->TUPLAS
"""conjunto = {'h', 'o', 'l', 'a'}
tupla = tuple(conjunto)
print(tupla)"""

# CONVERSION DE CONJUNTOS ---> LISTAS
"""conjunto = {'h', 'o', 'l', 'a'}
lista = list(conjunto)
print(lista)"""

# CONVERSION DE CADENA ---> DICCIONARIO

"""cadena = "Hola"
rango = range(0, len(cadena))
dicc = dict(zip(rango, cadena))
print(dicc)"""

# CONVERSION DE TUPLAS --->DICCIONARIOS
"""tupla = ('h', 'o', 'l', 'a')
rango = range(0, len(tupla))
dicc = dict(zip(rango, tupla))
print(dicc)"""

# CONVERSION DE CONJUNTOS ---> A DICCIONARIOS

"""conjunto = {'h', 'o', 'l', 'a'}
rango = range(0, len(conjunto))
dicc = dict(zip(rango, conjunto))
print(dicc)"""

# CONVERSION DE DICCIONARIOS --->CONJUNTOS
"""diccionario = {1: 'h', 2: 'o', 3: 'l', 4: 'a'}
sets = set(diccionario.values())
sets2 = set(diccionario.keys())
print(sets)
print(sets2)"""

# CONVERSION DE DICCIONARIOS ---> CADENAS
"""diccionario = {1: 'h', 2: 'o', 3: 'l', 4: 'a'}
cadena = "".join(diccionario.values())
print(cadena)"""

# CONVERSION DE DICCIONARIOS --->TUPLAS
"""diccionario = {1: 'h', 2: 'o', 3: 'l', 4: 'a'}
tupla = tuple(diccionario.values())
print(tupla)"""
# CONVERSION DE DICCIONARIOS A LISTAS
"""diccionario = {1: 'h', 2: 'o', 3: 'l', 4: 'a'}
listas = list(diccionario.values())
print(listas)"""

# INVOCACION DE FUNCIONES


"""def suma(num1, num2):
    return num1+num2


def otra_operacion(suma, num1, num2):
    return suma(num1, num2)


b = otra_operacion(suma, 4, 6)
print(b)"""


"""def crear_funcion(operador):
    if operador == '+':
        def suma(num1, num2):
            return num1+num2
        return suma


def operacion(funcion, num1, num2):
    return funcion(num1, num2)


suma = crear_funcion("+")
a = operacion(suma, 5, 5)
print(a)"""


# clase 27/05/2022

# FUNCIONES LAMBDA


# ejercicio 1
"""suma=lambda num1,num2:num1+num2

a=suma(25,64)
print(a)"""

# ejercicio 2
"""suma=lambda num1,num2,num3:num1+num2+num3

a=suma(10,18,97)
print(f"la suma de los valores es {a}")"""
# ejercicio 3 lambda y *args

"""todaslasvariables = lambda *args: args[2]

a = todaslasvariables(56, 68, 97, 54)

print(a)"""

# ejercicio 4 lambda y **kwargs

"""todaslasvariables = lambda **kwargs: kwargs.items()

a = todaslasvariables(clave1=5, clave2=2, clave3=7)

print(a)"""

# ejercicio 5 lambda , *args , **kwargs

"""todoslosvalores = lambda *args, **kwargs: args[0] and kwargs.items()

a = todoslosvalores(12, 15, 20, clave1="hola", clave2="como estas")

print(a)"""

# map()--->map() La función ejecuta una función específica para cada elemento en un iterable. El elemento se envía a la función como un parámetro.
# filter()--->La función filter() integrada de Python puede usarse para crear un nuevo iterador a partir de un iterable existente (como una lista o un diccionario) que filtrará de forma eficiente los elementos usando una función que proporcionamos
# zip()--->
# reduce()--->reduce() es una función incorporada de Python 2, que toma como argumento un conjunto de valores (una lista, una tupla, o cualquier objeto iterable) y lo "reduce" a un único valor. Cómo se obtiene ese único valor a partir de la colección pasada como argumento dependerá de la función aplicada.


# Ejemplos map

# EJEMPLO 1

"""def cuadrado(elemento):
    return elemento*elemento


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

resultado = list(map(cuadrado, lista))
print(resultado)"""

# EJEMPLO 2

"""numeros = [1, 2, 3, 4, 5, 6]
potencia = [3, 6, 5, 4, 7, 8]

resultado = list(map(pow, numeros, potencia))

print(resultado)"""


# EJEMPLOS DE FILTER

# Ejercicio 1

"""def mayores_asiete(numero):
    if numero > 7:
        return numero
    else:
        return False


def menores_asiete(numero):
    if numero < 7:
        return numero
    else:
        return False


tupla = (1, 2, 5, 8, 9, 4, 7, 6, 3, 1, 4, 5, 9, 7, 8, 5, 48)

mayores = tuple(filter(mayores_asiete, tupla))
menores = tuple(filter(menores_asiete, tupla))

print(mayores)
print(menores)"""


# Ejercicio 3 lambda y filter
"""lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


numeros_pares = list(filter(lambda lista: lista % 2 == 0, lista))
numeros_impares = list(filter(lambda lista: lista % 2 != 0, lista))
print(numeros_pares)
print(numeros_impares)"""

# Ejercicio 4 lambda y map
"""lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros_cubicos=list(map(lambda x:x**2,lista))
print"""

# Ejercicio 5 Reduce y lambda


# ejerecicio  sin la funcion reduce y sin la funcion anonima lambda quedaria de la siguiente manera con un loop for
"""lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
acumulador = 0

for i in lista:
    acumulador += i


print(acumulador)"""

# ejercicio con la funcion reduce y la funcion anonima lambda

"""from functools import reduce
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numero = (reduce(lambda a, b: a+b, lista))

print(numero)"""

# ejercicio de reduce con cadenas o str

"""from functools import reduce
lista = ['cristian', 'oscar', 'Fabian', 'Camilo']
reducir = (reduce(lambda a, b: a+"--"+b, lista))

print(reducir)"""

# EJERCICIOS DE ZIP
"""
nombres = ['cristian', 'Fabian', 'Oscar']
lista = [1, 2, 3]
a = tuple(zip(nombres, lista))
print(a)"""

# significado y funciones All y Any

# all -->La función all() toma un iterable como argumento y retorna True solo si todos los elementos del iterable tienen un valor booleano de True o el iterable está vacío
# any--->La función any devuelve el booleano True si alguno de los elementos del iterable que se cede como argumento es True, y devuelve el booleano False en caso contrario (o si el iterable está vacío)


# print(all([]))--> all sirve para saber si todos los retornos que nos dan son verdaderos es decir nos va a devolver True
# print(any([2]))---> any sirve para saber si todos los retornos que nos dan son falsos es decir nos va retornar false


"""lista = [1, 0, 3]
a = all(lista)

print(a)"""

# funciones isupper ()--> esta funcion devuelve "True"si todos los caracteres de las cadenas estan mayusculas . de lo contrario dvolvera "false"
# funciones isdigit()--->esta funcion devuelve "True" si todos los caracteres de la cadenas son digitos , de lo controraio devolvera "False"
# funciones isalnum()--> esta funcion comprueba si todos los caracteres de la cadena son alfanumericos o no (letra o numero)

# primer ejercicio


"""lista = ["B1CD1023540", "B1CDEF2354"]
condicion = []
for i in lista:
    condicion.append(len(list(filter(lambda i: i.isupper(), list(i)))) >= 2)
    condicion.append(len(list(filter(lambda i: i.isdigit(), list(i)))) >= 3)
    condicion.append(
        len(list(filter(lambda i: not(i.isalnum()), list(i)))) == 0)
    condicion.append(len(i) == len(set(i)))
    condicion.append(len(i) == 10)

print(condicion)"""


# -------------------------------------------------------------------------------------------------------------------------------

# NUMPY
# primero se deben importar las librerias en este caso se debe importar numpy
"""from turtle import shape
import numpy as np"""
# ejercicio matriz 2 x 3
"""a = np.array([(34, 25, 7), (47, 50, 41)])
print(a)"""
# print(a.shape) --> la funcion shape funciona para decirnos que tipo de matriz es , es decir cuantas columanas y filas esta conformada la matriz

# ejercicio matriz 3 x 3
"""b = np.array([(45, 78, 20), (41, 41, 78), (96, 4, 20)])
print(b)
print(type(b))
# print(b.shape)"""

# ejercicio para halallar un digito en especifico de nuestra matriz indicado la columna uy la fila donde esta

"""b = np.array([(45, 78, 20), (41, 41, 78), (96, 4, 20)])
# print(b[1, 1])---> en este caso le indicamos en que fila, columna esta el digito que queremos encontrar"""


# ejercicio para crear matrices con numeros aleatorios

"""b = np.random.random((3, 2))
print(b)"""
# ejercicio para crear matrices con numeros enteros es decir que sean de tipo int , y no de tipo float=decimales
"""n = np.random.randint(5, 20, size=(2, 2))
print(n)"""
# ejercio de matriz de ceros = 0
# la funcion zeros()--> permite hacer una matriz de solo numero 0
"""a = np.zeros((2, 2))
print(a)"""
# ejercicio matriz de unos = 1
# la funcion ones---> sirve para crear matrices solo con el numero 1
"""d = np.ones((2, 2))
print(d)"""

# matriz con una constante
# la funcion full()---> tiene como funcionamiento hacer la matriz con un mismo numero
"""a = np.full((3, 83), 15)
print(a)"""
# matriz identidad
"""a = np.eye(2)
print(a)"""


# submatriz de una matriz
# practicamente en estos ejercicios de matriz es sacar una submatriz de la matriz original, indicadando en que n filas  y n columnas estan

"""b = np.array([(1, 2, 3), (5, 6, 7), (9, 10, 11)])
a = b[0:3, 1:3]
print(a)
c = b[1:3, 1:3]
print(c)
h = b[0:2, 0:2]
print(h)
s = b[1:3, 0:2]
print(s)"""

# EJEMPLO PARA INVETIR UNA LISTA O MATRICEZ    DECIR PARA CAMBIAR SU ORDEN
# .fliplr()--> La función Numpy fliplr () es utilizado para voltear la matriz en la dirección de izquierda a derecha. Se conserva la forma de la matriz.
"""lista = np.array([(1, 2, 3), (2, 3, 4), (5, 6, 7)])
print(f"Esta es la lista normal :\n {lista}")

listaInvertida = (np.fliplr(lista))
print(f"Esta es la matriz invertida : \n {listaInvertida}")"""


# EJEMPLO DE INDEXACION DE MATRICEZ, ES DECIR IMPRIMIR UNA SUBMATRIZ INDICANDOLE LAS COLUMNAS

# np.arange()-->Devuelve valores uniformemente espaciados dentro de un intervalo dado. en este caso le indicamos el intervaalo de las columnas de la matriz

"""lista = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)])
columnas = np.array([(0, 2, 0, 1)])
a = lista[np.arange(4), columnas]
print(a)"""

# EJEMPLO , PARA SUMARLE UN NUMERO A LOS DIGITOS QUE UNO QUIERA SUMARLE , INDICANDO PREVIAMENTE SU N FILAS Y N COLUMNAS
"""lista = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)])
columnas = np.array([(0, 2, 0, 1)])
lista[np.arange(4), columnas] += 10
print(lista)"""

# EJEMPLO DE INDEXACION DE MATRICES BOOLENAS, en estecaso le ponemos una "condicion"que imprima true si hay numeros mayores a 5 , y false si no los hay
"""lista = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 15, 20)])
boolena = (lista > 5)
print(boolena)"""
# EJEMPLO PARA DECIRLE QUE NOS IMPRIMA SOLO LOS NUMEROS QUE SON MAYORES EN ESTE CASO DE 6
"""lista = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 15, 20)])
booleana = (lista > 6)
print(lista[booleana])"""

# EJEMPLO PARA CONOCER EL TIPO DE DATOS EN BYTES (INT,FLOAT)
# .dtype()---> dtype  describe cómo se deben interpretar los bytes en el bloque de memoria de tamaño fijo correspondiente a un elemento de la matriz. Describe los siguientes aspectos de los datos: Tipo de datos (entero,flotante,objeto Python ,etc.)
# si se hace de este modo seria un int(32)

"""lista = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print(lista.dtype)"""

# EJEMPLO PARA ASIGNAR FORZOZAMENTE A UN TIPO DE DATOS
"""lista = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)], dtype=np.int64)
print(lista.dtype)"""

# EJEMPLO SUMA DE MATRICEZ
"""a = np.array([(10, 5), (6, 7)])
b = np.array([(8, 6), (5, 9)])

print(a+b)"""

# EJEMPLO RESTA DE MATRICEZ
"""a = np.array([(10, 5), (6, 7)])
b = np.array([(8, 6), (5, 9)])
print(a-b)"""
# EJEMPLO DE MULTIPLICACION DE ELEMENTOS DE UNA  MATRIZ
"""a = np.array([(10, 5), (6, 7)])
b = np.array([(8, 6), (5, 9)])
print(a*b)"""
# EJEMPLO DE DIVISION DE ELEMENTOS DE UNA MATRIZ, CON REDONDEO
"""a = np.array([(10, 5), (6, 7)])
b = np.array([(8, 6), (5, 9)])
print(a/b)
print(np.round((a/b), 2))"""

# EJEMPLO DE RAIZ CUADRADA DE UNA MATRTIZ
"""a = np.array([(10, 5), (6, 7)])
b = np.array([(8, 6), (5, 9)])

print('raiz cuadrada')

print(np.sqrt(a))
print(np.round(np.sqrt(b)), 1)"""
# MULTIPLICACION DE MATRICEZ
"""print("multiplicacion de matricez")
a = np.array([(10, 5), (6, 7)])
b = np.array([(8, 6), (5, 9)])
print(np.dot(a, b))"""
# EJEMPLO DE BROADCASTING, ES DECIR SUMAR , RESTAR O MULTIPLICAR LOS INDICES DE NUESTRA MATRIZ
"""matriz = np.array([(12, 10, 11), (41, 20, 10), (6, 10, 20)])
# primero creamos el vector en el cual le indicamos cuanto le queremos en este caso sumar a cada fila
vector = ([2, 1, 3])
# segundo creamos la matriz vacia con la funcion np.empty_lyke
nueva = np.empty_like(matriz)
# creamos un  bucle para que lo recorra
for i in range(3):
    nueva[i:] = matriz[i:]+vector

print(nueva)"""

# -----------------------------------------------------------------------------------------------------------------------------------------------------------
# PANDAS
# EJERCIO DE SERIES A PARTIR DE LISTAS

"""*********************Series*************************"""

"""serie = pd.Series(['matematicas', 'ingles', 'español'])
print(serie)"""

# EJERCICIO DE SERIES A APRTIR DE DICCIONARIOS
"""serie = pd.Series({'matematicas': 50, 'ingles': 32, 'español': 20})
print(serie)"""

# EJERCICIO PARA CAMBIAR LOS "INDICES" DE NUESTRA TABLA APARTIR DE DICCIONARIOS
"""serie = {'matematicas': 50, 'ingles': 32, 'español': 50}
serieDatos = pd.Series(data=serie.values(), index=['M1', 'M2', 'M3'])
print(serieDatos)"""

# EJERCICIO PARA CAMBIAR LOS INDICES DE NUESTRA TABLA A APRTIR DE TUPLAS
"""serie = (1, 2, 3)
seriedatos = pd.Series(serie, index=('h', 'l', 'm'))
print(seriedatos)"""

# EJERCIO DE TABLAS CON TUPLAS
"""series = pd.Series((1, 2, 3, 4, 5, 6))
print(series)"""

# EJERCICIOS DE INDICES IMPLICITOS
# IMPLICITOS QUIERES DECIR QUE LOS INDICES VAN A IR DE UN RANGO 0 --> n
"""series = pd.Series(['colombia', 'españa', 'francia'])
print(series)"""
# EJERCICIO DE INDICES EXPLICITOS
# EXPLICITOS QUIERE DECIR QUE NOSOTROS PODEMOS CAMBIAR LOS INDICES YA SE A NUESTRA TUPLAS , DICCIONARIOS Y LISTAS
# NO SE PUEDE HACER ESTAS MANIPULACIONES PARA LOS CONJUNTOS "SETS"
"""series = ["colombia", "españa", "tailandia"]
print(pd.Series(series, index=("hermoso", "medio", "feo")))"""

# EJERCICIO PARA AGREGARLE EL NOMBRES A NUESTRO INDEX DE LA TABLA

"""series = pd.Series(['colombia', 'españa', 'francia'])
series.index.rename = 'frutas'
series.index.name = 'codigo'
print(series)"""

# EJERCIO PARA ENCONTRAR LOS AXES DE NUESTRA TABLA
# .axes()-->axes para crear de forma explícita un conjunto de ejes en la última figura que se haya creado o referenciado (lo que se denomina la "figura actual").

"""series = pd.Series(['colombia', 'españa', 'francia'])
series.index.name = 'codigo'
print(series.axes)
print(series.shape)
# EJEMPLO PARA IMPRIMIR UN DATO EN ESPESIFICO DE NUESTRA SERIE O TABLA
print(series[1])"""

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# LOC
# ILOC

# EJERCICIO de como indicarle a python para que nos imprima los indices repetidos que se encuentren
# la funcion loc nos permite indicar los indices que se encuentran repetidos en paquetes de pandas
"""s = pd.Series([10, 20, 30], index=['a', 'b', 'b'])

print(s.loc['b'])"""


# EJERCICIO PARA INDICARLE A PYTHON QUE ME IMPRIMA UN RANGO DE LOS INDICES,"segun uno le indique "
"""z = pd.Series([10, 20, 30, 50, 10, 20], index=['a', 'b', 'b', 'c', 'b', 'g'])
print(z.iloc[0: 3])"""

# EJERCICIO PARA ELEGIR UN INDICE AL AZAR POR MEDIO  DEL METODO RANDOM
"""d = pd.Series([10, 20, 30, 50, 10, 20], index=['a', 'b', 'b', 'c', 'b', 'g'])
print(d.sample(1, random_state=30))"""
# ejercicio para eliminar un indice en especifico de un indice con el metodo pop
"""d = pd.Series([10, 20, 30, 50, 10, 20], index=['a', 'b', 'b', 'c', 'b', 'g'])
d.pop('b')
print(d)"""
# ejercicio para imprimir personas mayores a 15 años
"""d = pd.Series([10, 20, 30, 50, 10, 20], index=[
              'carlos', 'fabian', 'oscar', 'cristian', 'brayan', 'gonzalo'])
print(d[d >= 15])"""
# ejemplo para poner el nombre al index y al nombre general de la Serie
"""d = pd.Series([10, 20, 30, 50, 10, 20], index=['a', 'b', 'b', 'c', 'b', 'g'])

d.index.name = "columnass"
d.name = "perros
print(d)"""
# ejercicios para cambiar o alterar datos de un solo indice
"""c = pd.Series([10, 20, 30, 50, 10, 20], index=[
    'carlos', 'fabian', 'oscar', 'cristian', 'brayan', 'gonzalo'])
c[1] = 50
print(c)"""

# ejercicio para modificar o alterar los datos del indice con un mismo valor
"""c = pd.Series([10, 20, 30, 50, 10, 20], index=[
    'carlos', 'fabian', 'oscar', 'cristian', 'brayan', 'gonzalo'])
c[0:3] = 25
print(c)"""

# metodo WHERE
# En este ejemplo nos servira para saber un determinado numero de carecteres que hay en el indice o en la serie
# funcion ISNA
"""c = pd.Series([10, 20, 30, 50, 10, 20], index=[
    'carlos', 'fabian', 'oscar', 'cristian', 'brayan', 'gonzalo'])

variables = c.where(c == 10)
print(variables)
x = []
for i in range(len(variables)):
    if not(pd.isna(variables[i])):
        x.append(variables[i])
print(len(x))"""
"""****************************************************DataFrame***************************************************************"""
# EJEMPLO PARA HACER UN DATA FRAME Y IMPRIMIR SUS COLUMNAS Y SUS INDICES

"""dta = {'paises': ['colombia', 'españa', 'puerto rico'],
       'comidas': ['ajiaco', 'postres', 'fritos']}

dataframe = pd.DataFrame(dta, index=['pais 1', 'pais 2', 'pais 3'])


print('imprimir los indices')
print(dataframe.index)


print("imprimir las columnas")
print(dataframe.columns)


print("toda la informacion")
print(dataframe.axes)


print("imprimir solo los elementos de mi dataframe")
print(dataframe.values)


print("para ver la dimension o tamaño de mi Data frame")
print(dataframe.shape)"""

# crear un Data frame a partir de un array en numpy
"""matriz = np.array([[1, 2, 3, ], [5, 2, 1], [4, 7, 8]])

print(pd.DataFrame(matriz))"""


# crear un data frame a partir de diccionarios
"""casos_Covid = {'colombia': 50, 'argentina': 60, 'brasil': 80}
casos_Covid2 = {'colombia': 20, 'argentina': 80, 'brasil': 80}
casos_Covid3 = {'colombia': 5, 'argentina': 100, 'brasil': 10}


a = pd.DataFrame([casos_Covid, casos_Covid2, casos_Covid3],
                 index=[2020, 2021, 2022])
print(a)"""

# crear un dataframe a partir de las series,en este ejemplo podemos encontrar varias estadisticas a partir de metods como
# head(),tail(),sample(),describe(),info()

"""dias_trabajados = pd.Series([10, 20, 14, 1, 2, 4, 52, 12, 30, 53, 41, 2], index=[
                            'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'])

dias_pagados = pd.Series([10, 20, 1, 2, 4, 5, 6, 4, 8, 3, 4, 5], index=[
    'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'])

tabla = pd.DataFrame({'DIAS TRABAJADOS': dias_trabajados,
                     'DIAS PAGADOS': dias_pagados})
print(tabla)

print("primeros 5 elementos de mi dataFrame")
print(tabla.head())

print("ultimos 5 elementos de mi dataframe")
print(tabla.tail())

print("elementos aleatorios de mi data frame")
print(tabla.sample(6))

print("iformacion estadistica de es data frame ")
print(tabla.describe())

print("informacion basica del data frame ")
print(tabla.info())"""

# EJEMPLO PARA SABER CUANTAS VECES SE REPITE UN MISMO HECHO
# funciones como np.nan
# funciones como value_counts()
# la funcion dropna sirve , en este caso para traernos los NAn ah nuestra tabla de datos , diciendonos cuantas veces se repite

"""tabla = pd.DataFrame([3, 1, 2, 1, 2, 1, 5, 4, 6, np.nan])
print("conteo")
print(tabla.value_counts(dropna=False))"""

# EJEMPLO PARA SELECCIONAR INFORMACION DE UN DATAFRAME

"""tabla = pd.DataFrame({'Entradas': [45, 20, 10, 15],
                      'salidas': [14, 20, 15, 42],
                      'valoracion': [54, 52, 10, 15],
                      'limite': ['si', 'no', 'si', 'si']}, index=['enero', 'febrero', 'marzo', 'abril'])


print(tabla)
print("*"*50)
# De manera implicita
print(tabla['Entradas']['enero'])

# De manera explicita
print(tabla.iloc[0][0])"""

# ejemplo para seleccionar informacion de acuerdo a las filas y columnas que hay en el data frame


"""tabla = pd.DataFrame({'Entradas': [45, 20, 10, 15],
                      'salidas': [14, 20, 15, 42],
                      'valoracion': [54, 52, 10, 15],
                      'limite': ['si', 'no', 'si', 'si']}, index=['enero', 'febrero', 'marzo', 'abril'])
print(tabla)

print(tabla.iloc[1:3, 2:4])

# primero asignamos la funcion iloc [ de que fila : hasta que fila , de que columna : hasta que columna]"""

# -------------------------------------------------------------------------------------------------------------------------------

# EJEMPLO PARA CREAR UN ARRAY O UNA MATRIZ ATRAVES DE UN RANGO DE NUMEROS DEL 1 AL 10
# np.arange()--> sirve para crear los numeros que va estar compuesta nuestro array
# reshape()--> sirve para componer las filas y las columnas
# se le puede cambiar los nombres a las columnas por el metodo columns=
# se le puede cambiar el nombre de las filas a partir del metodo index=
"""tabla = pd.DataFrame(np.arange(1, 10).reshape([3, 3]), columns=[
                     'A', 'B', 'C'], index=['z', 'c', 'f'])
print(tabla)

r = tabla.where(tabla % 2 == 1)
print(r)
print(r.shape[1])"""

# ejemplo con shape y iloc
"""tabla = pd.DataFrame(np.arange(1, 10).reshape([3, 3]), columns=[
                     'A', 'B', 'C'], index=['z', 'c', 'f'])
print(tabla)

r = tabla.where(tabla % 2 == 1)
lista = []
for i in range(r.shape[0]):
    for x in range(r.shape[1]):
        print(r.iloc[i, x])
        if not (pd.isna(r.iloc[i, x])):
            lista.append(r.iloc[i, x])

print(lista)"""
# ejemplo para eliminar una fila , funcion drop()

"""tabla = pd.DataFrame(np.arange(1, 10).reshape([3, 3]), columns=[
                     'A', 'B', 'C'], index=['z', 'c', 'f'])
a = tabla.drop(['z'])
print(a)"""

# ejemplo para eliminar una columna , funcion drop()
"""tabla = pd.DataFrame(np.arange(1, 10).reshape([3, 3]), columns=[
                     'A', 'B', 'C'], index=['z', 'c', 'f'])


s = tabla.drop(columns=['B', 'C'])
print(s)"""

# EJEMPLO DE CONCATENAR DOS DATAFRAME
# funcion concat()
"""tabla = pd.DataFrame(np.arange(1, 10).reshape([3, 3]), columns=[
                     'A', 'B', 'C'], index=['z', 'c', 'f'])

tabla2 = pd.DataFrame(np.arange(1, 10).reshape([3, 3]), columns=[
    'V', 'N', 'X'], index=['#', '%', '&'])

print("tabla 1")
print(tabla)

print("tabla2")
print(tabla2)

print("concatenacion o union")
a = pd.concat([tabla, tabla2])
print(a)"""
