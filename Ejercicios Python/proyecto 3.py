#mi_texto = "Esta es una prueba"
# resultado = mi_texto.index("a") --->para contar de izquierda a derecha
# resultado = mi_texto.rindex("a") --->para contar de derecha a izquierda
# print(resultado)


#---------------------------------------------------------------------------------------------------#


#frase = "En teoria, la teoria y la practica son los mismo .En la practica , no lo son."
#resultado = frase.rindex("practica")
# print(resultado)


#---------------------------------------------------------------------------------------------------#

#frase = "ABCDEFGHIJKLM"
#fragmento = frase[9: 3:2]
# print(fragmento)


#---------------------------------------------------------------------------------------------------#

#frase = "Controlar la complejidad es la esencia de la programacion"
#fragmento = frase[0:9]
# print(fragmento)


#---------------------------------------------------------------------------------------------------#

#frase = "Es genial trabajar con ordenadores. no discuten , lo recuerdan todo y no se beben tu cerveza "
# print(frase[:: -1]) ----->para poner invertida la frase o palabra puesta por el usuario


#---------------------------------------------------------------------------------------------------#

# upper() ------>PASAR A MAYUSCULAS
# lower() ------>PASAR A MINUSCULAS
# split() ------>SEPARARLO EN PARTES
# join() ------>UNIR ITEMS USANDO SEPARADOR
# find() ------>ENCONTRAR UN SUB-STRING
# replace() ------>REEMPLAZAR UN SUBSTRING


#---------------------------------------------------------------------------------------------------#


#texto = "Este es el texto de federico"
#resultado = texto.split("t")
# print(resultado)
#a = "aprender"
#b = "python"
#c = "es"
#d = "genial"
#e = " ".join([a, b, c, d, ])

# print(e)

#---------------------------------------------------------------------------------------------------#

#texto = "Este es el texto de federico"
#resultado = texto.replace("federico", "cristian")
# print(resultado)

#---------------------------------------------------------------------------------------------------#

# EJERCICIO
#frase = "hola amor"
#fragmento = frase.upper()
# print(fragmento)

#---------------------------------------------------------------------------------------------------#
# EJERCICIO
#lista_palabras = ["la", "legibilidad", "cuenta"]
#frase = " ".join(["la", "legibilidad", "cuenta"])
# print(frase)
#---------------------------------------------------------------------------------------------------#

# EJERCICIO
#frase = "si la implementacion es dificil de explicar , puede que sea una mala idea"
#resultado = frase.replace("dificil", "facil").replace("mala", "buena").replace("implementacion", "socializacion")
# print(resultado)

#----------------------------------------------------------------------------------------------------#
# poema = """mil pequeños peces
# blancos y tambien
# para hacerlo"""
#print("agua" in poema)

#-------------------------------------------------------------------------------------------------------------------------------#

#texto = "texto"
# resultado = len(texto) --------> len  sirve para hallar la longitud del texto o hallar cuantos caracteres tiene el texto
# print(resultado)

#-------------------------------------------------------------------------------------------------------------------------------#

# LISTAS O ARRAYS

#lista1 = ["a", "b", "c"]
#lista2 = ["d", "e", "f"]
#lista3 = lista1+lista2

# lista3.append("g")-------> append sirve para agregar mas caracteres a nuestras listas

# eliminado = lista3.pop(4) --->y pop sirve para eliminar un caracter en especial de la lista

# print(lista3)
# print(eliminado)

#-------------------------------------------------------------------------------------------------------------------------------#
#lista1 = ["1", "3", "2", "4"]
# lista1.sort()---->sirve para reorganizar numeros segun la logica
# print(lista1)
#-------------------------------------------------------------------------------------------------------------------------------#
#mediostransporte = ["avion", "carro", "moto", "bicicleta"]
# mediostransporte.append("motocicleta")
# print(mediostransporte)

# -------------------------------------------------------------------------------------------------------------------------------

# DICCIONARIOS

"""diccionario = {'palabra1': {'hola': 'como'}, 'palabra2': 'cristian'}
resultado = diccionario['palabra1']['hola']
print(resultado)"""


# -------------------------------------------------------------------------------------------------------------------------------

# cliente = {'nombre': 'cristian', 'apellido': 'galeano', 'peso': 60, 'altura': 1.68}
# consulta = cliente['peso']
# print(consulta)

# -------------------------------------------------------------------------------------------------------------------------------

# diccionario = {'c1': 55, 'c2': [25, 30, 50], 'c3': {'s1': {'s4':1578}, 's2': 200}}
# resultado = diccionario['c3']['s1']['s4']
# print(resultado)

# -------------------------------------------------------------------------------------------------------------------------------

# diccionario = {'c1': ['a', 'b', 'c'], 'c2': ['d', 'e', 'f']}
# print(diccionario['c2'][1].upper())

# -------------------------------------------------------------------------------------------------------------------------------

#novias = {'sandra': 1, 'anamaria': 2, 'alejandra': 3}
# print(novias)
# novias['anamaria'] = 4
# print(novias)


# print(novias.keys())------->imprimir todos los diccionarios que hay
# print(novias.values())------->imprimir los significados de los diccionarios
# print(novias.items())--------> imprimir el diccionario completo con sus significados

# -------------------------------------------------------------------------------------------------------------------------------

# TUPLES


# hola = 1, 2, (3, 4), 5
# print(hola[2])------>EN ESTE CASO ME VA A IMPRIMIR (3,4)


# hola = 1, 2, 3, 4
# x, y, z, e = hola
# print(x, y, z, e)---->EN ESTE CASO ME VA A VOLVER A IMPRIMIR 1,2,3,4, POR QUE SE ALAMCENA EN DIGITOS (X,Y,Z,E)


# COUNT
# hola = 1, 2, 3, 4, 4, 4, 5, 6, 7

# print(hola.count(4))------->SIRVE PARA SABER CUANTAS VECES SE ENCUENTRA REPETIDO UN NUMERO O UNA LETRA EN NUESTRA LISTA O TUPLE


#mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
#mi_lista = list(mi_tupla)
# print(type(mi_lista))------>utilizamos list() para cambiar de un tipo tupla a un tipo lista
# print(mi_lista)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# SETS

# set = {1, 2, 3, 4, 5, 6}---->los sets deben ir con 2 parentesis o corchetes para que python lo identifique como set
# print(type(set))
# print(set)


# set = {1, 2, 3, 4, 5, 6, 6, 6, 6, 6, 6, 4, 4}----------->en los set no se pueden repetir articulos ya que python los va a ignorar
# print(len(set))

# set = set((1, 2, 3, 4, 5, 6))
# print(9 not in set)----->para saber si esta(TRUE) o no esta(FALSE) un numero o una letra en un set


# set1={1,2,3}
# set2={4,5,6}
# set3 = set1.union(set2)-----> .union()se utiliza para unir varios set
# print(set3)


# set1 = {1, 2, 3}
# set1.add(4)------> .add() sirve para agregar mas elementos a un set
# set1.remove(3)----->.remove()para eliminar un elemento de un set
# set1.clear()----->.clear va borrar todo nuestro set
# print(set1)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# BOLEANOS

#numero = bool(5 == 3+2)

# print(numero)-------> va imprimir si la expresion planteada es verdadera (True) o  falsa (False)

#lista = [1, 2, 3, 4, 5]
#control = bool(5  in lista)
# print(control)

#prueba = bool(5 >= 4)
# print(prueba)

#print(bool(17834/34 > 87*56))

#import math


# print(round(math.sqrt(25)))


# Analizador de texto


texto = (input("Ingresa un texto :"))
letras = []

texto = texto.lower()


letras.append(input("ingresa la primera letra :").lower())
letras.append(input("ingresa la segunda letra :").lower())
letras.append(input("ingresa la tercera letra :").lower())

print(letras)

print("Cantidades de letras")

cantidad1 = texto.count(letras[0])
cantidad2 = texto.count(letras[1])
cantidad3 = texto.count(letras[2])

print(f"la letra ' {letras[0]} ' fue encontrada {cantidad1}")

print(f"la letra ' {letras[1]} ' fue encontrada {cantidad2}")

print(f"la letra ' {letras[2]} ' fue encontrada {cantidad3}")

convertido = list(texto)
print((convertido))

contador = (len(convertido))

print(f"el texto ' {texto}'  tiene una cantidad de {contador} palabras")

primera = texto[0]
ultima = texto[-1]

print(f"la primera letra es {primera} y la ultima palabra es {ultima}")

convertido.reverse()

print("el texto invertido quedaria de la siguiente manera")

print(' ' .join(convertido))

python = "python" in texto
dicc = {True: "si", False: "no"}
print(f"la palabra python {dicc[python]} aparece en el texto")
