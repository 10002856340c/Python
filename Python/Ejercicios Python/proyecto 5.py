

"""car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.popitem()

print(car)"""


# lstrip () lo que hace esta funcion es movernos a la derecha el argumento es decir da como un espacio o salto de linea
"""txt = "     banana     "

x = txt.lstrip()

print(txt)

print(f"el {x} es re chimba")"""

# insert() ----------> lo que hace la funcio insert es insertar a nuestra lista un elemento de tipo str que nosotros queramos agrgarle y en que posicion o casilla de la lista

"""frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]

frutas.insert(3, "naranja")
print(frutas)"""
# ---------------------------->El método isdisjoint () devuelve True si dos conjuntos son conjuntos disjuntos. Si no, devuelve False.

"""marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)

print(conjuntos_aislados)"""


# -------------------------------------------------------------------------------------------------------------------------------------------------------

# FUNCIONES def()


# 1 ejercicio
"""def bienvenida(nombre: str):
    nombre_persona = (f"¡Bienvenido {nombre} !")
    return print(nombre_persona)

bienvenida("cristian")"""


# 2 ejercicio
"""def cuadrado(numero: int):
    potencia = numero**2
    return print(potencia)

cuadrado(952)"""


# 3 ejercicio

"""def potencia(numerobase: int, numeroexponente: int):
    potencias = numerobase**numeroexponente
    return (potencias)


potencia(5, 4)"""

# 4  ejercicio

"""def usd_eur(dinero: int):
    dolares = dinero * 0.85
    return print(dolares)


usd_eur(1000)"""


# 5  ejercicio

"""def invertir_palabra (palabra: str):

    palabra = palabra[::-1]
    mayuscula = palabra.upper()

    return print(mayuscula)


invertir_palabra("python")"""


# ejercicio 6

"""def cheaquear(lista: list):

    lista_vacia = []

    for n in lista:
        if n in range(100, 1000):
            lista_vacia.append(n)
        else:
            print("de que putas esta hablando?")
            pass
    return(print(lista_vacia))


cheaquear([300, 500, 60])"""


# ejercicio 7


"""def todos_positivos(lista: list):

    for n in lista:
        if n < 0:
            return (False)

    else:
        return (True)


lista_mumeros = todos_positivos([100, -5,  4])
print(lista_mumeros)"""


# ejercicio 8

"""def suma_menores(lista: list):

    for n in lista:
        if n in range(0, 1000):
            lista_numeros = sum(lista)
            return print(lista_numeros)
        else:
            return print("oiga se salio del rango egg")


suma_menores([100, 2000, 300])"""

# ejercicio 9

"""def cantidad_pares (lista: list):
    cantidad = 0
    for n in lista:
        if n % 2 == 0:
            cantidad += 1
            print()

        else:
            pass
    return print(cantidad)


cantidad_pares([40, 20, 50])"""

# ejercicio 10
"""precios_licores = [('cerveza', 1.5), ('wisky', 2.2), ('ron', 1.9)]


def licor_mas_caros(lista: list):

    precio_mayor = 0
    licor_mas_caro = ''
    for licor, precio in lista:
        if precio > precio_mayor:
            precio_mayor = precio
            licor_mas_caro = licor
        else:
            pass
    return(licor_mas_caro, precio_mayor)


print(licor_mas_caros(precios_licores))"""

# ejercicio 11 el pailito mas corto

# crear una lista
"""from random import randint, shuffle
palitos = ['--', '---', '----', '-----']


# mezclar palitos
def mezclar_palitos(lista: list):
    shuffle(palitos)
    return palitos


# pedirle el intento
def pedirle_intento():
    lista = ['1', '2', '3', '4']
    intento = ''

    while intento not in lista:
        intento = input("Elije un numero del 1 al 4  :  ")
    return int(intento)

# comprabar si es el intento


def comprobar(lista, intento):
    if lista[intento-1] == '--':
        print("A lavar los platos")
    else:
        print("te has salvado")

    print(f"te ha tocado {lista[intento-1]}")


palitos_mezclados = mezclar_palitos(palitos)
pedir_intento = pedirle_intento()

comprobar(palitos_mezclados, pedir_intento)"""

# -------------------------------------------------------------------------------------------------------------------------------------------------->


"""from random import randint
def lanzar_dados():

    numero1 = randint(1, 6)
    numero2 = randint(1, 6)
    sumados = numero1+numero2
    return sumados


def evaluar_jugada(sumados):

    if sumados <= 6:
        return(f"La suma de tus dados es {sumados} . lamentablemente")

    elif sumados > 6 and sumados < 10:
        return(f"la suma de tus dados es {sumados}.tienes buenas chances")

    elif sumados >= 10:
        return(f"la suma de tus dados es {sumados}. parece una jugada ganadora ")


lanzar = lanzar_dados()
evaluar = evaluar_jugada(lanzar)
print(evaluar)"""

# ----------------------------------------------------------------------------------------------------------------------------------------------------------->

"""lista = [4, 5, 3, 1, 2, 3, 2, 2, 2]


def reducir_lista(lista):
    Elista = list(set(lista))
    Elista.sort()
    Elista.pop(-1)
    return Elista


def promedio(Elista):
    sumlista = sum(Elista)
    promedio = sumlista/len(Elista)
    return promedio


hola = reducir_lista(lista)
holas = promedio(hola)
print(holas)"""
# -------------------------------------------------------------------------------------------------------------------------->

"""from random import choice
def lanzar_moneda ():
    menu = ["cara", "cruz"]
    sorteo = choice(menu)
    return sorteo


def probar_suerte(sorteo, lista):

    if sorteo == "cara":
        print("se autodestrudira")
        return []
    elif sorteo == "cruz":
        print("la lista fue salvada")
        return(lista)


lista = [1, 2, 3, 4, 5, 6]


a = lanzar_moneda()
b = probar_suerte(a, lista)

print(b)"""

# ------------------------------------------------------------------------------------------------------------------------------------->

# *args y *kwargs  ---> El principal uso de *args y **kwargs es en la definición de funciones. Ambos permiten pasar un número variable de argumentos a una función, por lo que si quieres definir una función cuyo número de parámetros de entrada puede ser variable, considera el uso de *args o **kwargs como una opción.

# 1 ejercicio -- > * args

"""def suma_cuadrados(*args):----> *args
    cero = 0
    for i in args:
        cero += i**2

    return cero


print(suma_cuadrados(1, 2, 3))"""


# 2 ejercicio -->  *args
"""def suma_absolutos(*args): ---->*args
    numero = 0
    for i in args:
        numero += abs(i)  ------> La función abs() calcula el valor absoluto de un número que recibe como parámetro y retorna el valor calculado como resultado. Si el número que recibe no es negativo devuelve el mismo valor sin cambios.
    return numero


print(suma_absolutos(1, -5, -6, 4, -5))"""


# 3 ejercicio -->  * args

"""def numeros_persona(nombres: str, *args): --->*args
    suma = 0
    for i in args:
        suma += i
    return f"{nombres}, la suma de tus numeros es {suma}"


print(numeros_persona("Cristian", 5, 15, 7))"""

# 4 ejercicio --> *kwargs

"""def suma(**kwargs):
    total=0

    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")
        total+=valor
    return total

a=suma(clave1=1,clave2=2,clave3=3)
print(a)"""

# 5 ejercicio kwargs --> ejercicio de combinacion  variables, *args , **kwargs


"""def suma(num1, num2, *args, **kwargs):

    print(f"este es el argumento {num1}")
    print(f"este es el argumento {num2}")

    for i in args:
        print(f"arg = {i}")

    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")


a = suma(100, 200, 5, 6, 7, 8, 9, clave1=54, clave2=55, clave3=412)

print(a)"""

# 6 ejercicio --> kwargs

"""def cantidad_atributos(**kwargs):
    numero = 0
    for clave, valor in kwargs.items():
        print(f"{clave}={valor}")
        numero += valor
    return numero


a = cantidad_atributos(a=12, b=13, c=52)
print(a)"""

# 7 ejercicio --> kwargs

"""def lista_atributos(**kwargs):
    lista = []

    for clave in kwargs.values():

        lista.append(clave)
    return lista


a = lista_atributos(a=12, b=13, c=15)
print(a)"""

# 8 ejercicio --kwargs


"""def describir_personas(nombre: str, **kwargs):
    print(f"Caracteristicas de{nombre} :")
    for clave, valor in kwargs.items():

     print(f" {clave} = {valor}")


a = describir_personas("Cristian", color_ojos="Azules", color_pelo="Rubio")
print(a)"""


# EJERCICIOS PRACTICOS PYTHON

"""def devolver_distintos(num1: int, num2: int, num3: int):
    suma = num1+num2+num3
    lista = [num1, num2, num3]
    if suma > 15:
        mayor = max(lista)

        return f"El mayor es {mayor}"

    elif suma < 10:
        menor = min(lista)

        return f"El menor de una lista es {menor}"
    elif suma in range(10, 15):
        lista.sort()
        medio = lista[1]

    return f"el valor promedio es {medio}"


a = devolver_distintos(7, 2, 4)
print(a)"""


# Ejercicio practico 2

"""def devolucion(argumento):
    a = set()
    for letra in argumento:
        a.add(letra)
        lista = list(a)
        lista.sort()

    return lista



print(devolucion("entretenido"))"""

# Ejercicio practico 3


"""def indefinida(*args):
    contador = 0
    for numero in args:
        if args[contador + 0] == 0 and args[contador + 1] == 0:
            return True
        else:
            contador += 1
    return False


print(indefinida(5, 6, 1, 0, 0, 9, 3, 5))"""


# Ejercicio practico 4
"""
def contar_primos(numero):
    primos = [2]
    iteracion = 3
    if numero < 2:
        return "No es un numero primo"

    elif numero > 2:
        while iteracion <= numero:

            for n in range(3, iteracion, 2):

                if iteracion % n == 0:
                    iteracion += 2
                    break
            else:
                primos.append(iteracion)
                iteracion += 2
    print(primos)
    return len(primos)


print(contar_primos())"""


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->
# PROYECTO 5 JUEGO DEL AHORCADO en proceso
from ntpath import join
from random import choice
print(
    "********************Bienvenido al juego del ahorcado*************************")

palabras = ["colombia", "españa", "mexico", "estados unidos"]
letras_conocidas = []
letras_desconocidas = []
intentos = 6
aciertos = 0
juego_terminado = False


def elegir_palabra(lista_palabras):
    palabra_elegida = choice(lista_palabras)
    letras_unicas = len(set(palabra_elegida))
    return palabra_elegida, letras_unicas


def pedir_letra():
    letra_elegida = ''
    es_valida = False
    abecedario = 'qwertyuiopasdfghjklñzxcvbnm'

    while not es_valida:
        letra_elegida = input("Ingrese una letra : ")
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print("no has elegido una letra , si no varias  ")

    return letra_elegida


def mostra_tablero(letra_elegida):

    lista_oculta = []
    for l in letra_elegida:
        if l in letras_conocidas:
            lista_oculta.append(l)
        else:
            lista_oculta.append("-")

    print('  '.join(lista_oculta))


def chequear_usuario(letra_elegida, palabra_oculta, vidas, coincidencias):
    fin = False

    if letra_elegida in palabra_oculta:
        letras_conocidas.append(letra_elegida)
        coincidencias += 1
    else:
        letras_desconocidas.append(letra_elegida)
        vidas -= 1

    if vidas == 0:
        fin = perder()
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)

    return vidas, fin, coincidencias


def perder():
    print("te has quedado sin vidas ")
    print("la palabra  oculta era :" + palabras)
    return True


def ganar(palabra_descubierta):
    mostra_tablero(palabra_descubierta)
    print("felicitaciones, has encontrado la palabra!!!")
    return True


palabra, letras_unicas = elegir_palabra(palabras)

while not juego_terminado:
    print(' \n' + '* ' * 20 + '\n')
    mostra_tablero(palabra)
    print('\n')
    print('letras incorrectas : ' + ' -'.join(letras_desconocidas))
    print(f"Vidas :  {intentos}")
    print("\n" + "*"*20+"\n")
    letra = pedir_letra()
    intentos, terminado, aciertos = chequear_usuario(
        letra, palabra, intentos, aciertos)
    juego_terminado = terminado
