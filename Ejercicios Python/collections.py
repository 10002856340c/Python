
"""**********************************************************************Modulos de collections*********************************************"""
import re
import datetime
from datetime import datetime
import os
import shutil
from collections import Counter
from collections import defaultdict
from collections import namedtuple
import collections
import math

import send2trash
import time
import timeit


"""# El metodo Counter --> es una subclase de diccionario integrada en Python que se utiliza para realizar cuentas o conteos sobre listas, palabras… Podríamos resumir la función Counter como un contador en Python.

# 1) En este ejemplo vamos hacer una lista con numeros repetidos , y vamos a utilizar el modulo counter para saber cuantas veces se repite ese numero en especifico

numeros = [1, 5, 4, 5, 6, 2, 3, 4, 3, 2, 8,
           7, 4, 5, 2, 1, 3, 2, 2, 1, 2, 1, 2, 2, 5]

print(Counter(numeros))

# 2)  En este ejemplo vamos hacer una variable que contenga una cadena de caracteres con letra repetidas , y vamos a utilizar el modulo counter para saber cuantas veces se repite esa letra en especifico

cadena = "crrrisssstiiiiiiiiaaaaaaaannnnnn"

print(Counter(cadena))


# 3)  En este ejemplo vamos hacer una frase que contenga valga la redundancia frases repetidas, vamos averiguar cuantas veces se repite cada frase , utilizando de la mano el metodo split()

frase = "al pan pan al vino vino"

print(Counter(frase.split()))

# 4)  En este ejemplo vamos hacer una  de lista utilizando el modulo counter y vamos saber cual es el numero mas comun que hay en esa lista

lista = Counter([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2,
                2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])

# utilizando el metodo must_common(el mas comun), vamos hayar el mas comun de esa lista
# most_common --> es un metodo especial del modulo Counter
print(lista.most_common())
print(list(lista))"""

"""# el metodo defaultdict
# defaultdict -->Es una subclase del diccionario, usado para proporcionar valores por defecto para las claves que no existan, sin generar un mensaje de error. El valor pordefecto puede ser un tipo de dato (int, list, etc.) o una función lambda que proporcione dicho valor directamente (lambda:"mi valor").

# 1) en este ejemplo lo que vamos hacer es hacer un mensaje atravez del metodo lambda para hacer que cuando haya un error nos imprima ese mensaje
variable = defaultdict(lambda: "es un error")

variable["uno"] = "verde"
print(variable["unos"])
"""

"""# el metodo namedtuple

# devuelve una tupla donde las posiciones de sus elementos tienen un nombre, además de un número de índice como las tuplas tradicionales

persona = namedtuple("persona", ["nombre", "altura", "peso"])
ariel = persona("cristian", 1.68, 62)

print(ariel[2])"""

# ejercicios con el metodo defaultdict
"""mi_diccionario = defaultdict(lambda: "valor no encontrado ")
mi_diccionario["edad"] = 44

print(mi_diccionario["edads"])"""

"""DoubleEnded = collections.deque(["Mon", "Tue", "Wed"])
print(DoubleEnded)
print("Adding to the right: ")
DoubleEnded.append("Thu")
print(DoubleEnded)
"""
# ejercicios con el ,etodo collections.deque
# este metod permite agregar informacion a nuestra lista de ciudades
"""lista_Ciudades = collections.deque(
    ["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])
print(lista_Ciudades)
print("*"*100)
lista_Ciudades.append("Bogota")
print(lista_Ciudades)
"""
"""*******************************************************************Modulos OS y Shutil********************************************************************************"""


# listdir--> funciona para ver todas  los archivos que tenemos en nuestra ruta
"""try:
    archivo = open('main.txt', 'w')
    archivo.write("hola como vamos ")
    archivo.close()
    print("se ejecuto con exito el archivo")
except:
    print("Error")

print(os.listdir())
"""


# shutil()--> Para mover un archivo de una ruta a otra se hace lo siguiente
# 1)  importamos el metodo shutil
# 2) despues ponemos el archivo con la extencion --> tener en cuenta que el archivo debe estar en la ruta local para moverlo a otra ruta
# 3) ponermos la ruta a donde queremos mover el archivo

"""try:
    shutil.move('cesantias.pdf', 'D:\\usuario\\Documents\\SANANTONIO (2)')
    print("se ejecuto con exito ")
except:
    print("Hubo un error")"""

# send2trash--> envía un archivo a la papelera de reciclaje es necesario instalar el módulo desde la terminal y luego importarlo)
"""try:
    send2trash.send2trash("retiro.pdf")
    print("archivo eliminado con exito")
except:
    print("Hubo un error")
"""

# os.walk --> recorre el directorio indicado, y devuelve los nombres de carpetas, subcarpetas y archivos dentro de ellas en forma de tupla, a través de un generador.
"""ruta = 'D:\\usuario\\Desktop\\CarpetaPrincipal'

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f" En la carpeta -- {carpeta}")
    print(f" Las subCarpetas son : ")
    for sub in subcarpeta:
        print(f" \t -- {sub}")
    print("los archivos son :")
    for asrchiv in archivo:
        print(f"\t --  {asrchiv}")
    print("\n")
"""
"""******************************************************************Modulo datetime**********************************************************************"""

# El módulo datetime (incorporado en Python) puede importarse en proyectos para trabajar con fechas y horas, así como intervalos y duraciones.

# 1)ejemplo para impartir una hora con datetime.time(horas,minutos segundos ,etc..)
"""mi_hora = datetime.time(17, 40, 10)
#para saber la hora 
print(mi_hora)
#para saber solo las horas
print(mi_hora.hour)
#para saber solo los minutos
print(mi_hora.minute)
#para saber solo los segundos 
print(mi_hora.second)"""


# 2 ejmplo para impartir una fecha con datetime.date(año,mes,dia)
"""mi_fecha = datetime.date(2025, 6, 12)
# para saber la fecha
print(mi_fecha)
# para saber el dia
print(mi_fecha.day)
# para saber el mes
print(mi_fecha.month)
# para saber el año
print(mi_fecha.year)
# para saber en que dia de la semana es la fecha que estipulamos principalmente con la funcion ctime()
print(mi_fecha.ctime())
# para saber nuestra fecha actual con la funcion today()
print(mi_fecha.today())
"""

# 3 ejemplo para cambiar ya sea nuestro mes, dia, hora, segundos, etc , atravez del metodo replace()
"""mi_fecha = datetime(2025, 6, 12, 12, 30, 30, 5000)
mi_fecha = mi_fecha.replace(month=11)
print(mi_fecha)
"""

# 4 ejemplo para saber cuantos dias vivio una persona ya fallecida
"""nacimiento = date(1985, 10, 10)
fallecimiento = date(2050, 2, 10)

diasVivos = nacimiento-fallecimiento
print(diasVivos)"""
# 5 ejemplo para saber cuantas hora estuvo despierta una persona desde que se levanto hasta que se durmio
"""despierto = datetime(2025, 7, 12, 6, 30)
dormido = datetime(2025, 7, 12, 22, 15)
HorasDormidas = despierto-dormido

print(HorasDormidas.seconds)"""
# 6 ejemplo para saber los minutos de la fecha actual , es un datos que va ir cambiando
"""minutos = datetime.now()
print(minutos)
print(minutos.minute)"""

""""*************************************************************time y timeit***************************************************************************"""
# En este apartado los modulos time y timeit --> nos ayudaran para determinar el tiempo en que se ejecuta un codigo en especifico , asi nos ayudara a saber si un codigo es mas eficiente a otro

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# time()---> Para funciones que toman varios segundos para ejecutarse
# 1) ejemplo time ()

"""# 1)Creamos dos funciones que hacen exactamente lo mismo


def prueba_for(numero):
    lista = []
    for i in range(1, numero+1):
        lista.append(i)
    return lista


def prueba_while(numero):
    contador = 1
    lista = []
    while contador <= numero:
        lista.append(contador)
        contador = contador+1
    return lista


# 2 Para probar nuestras funciones hacemos dos variables utilizando el metodo time.time "inicio", "final" , y entre ellas llamamos a nuestra funcion
inicio = time.time()
prueba_for(1000000)
final = time.time()
# 3 despues hacemos una simple resta
print(final-inicio)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# 4 Para probar nuestras funciones hacemos dos variables utilizando el metodo time.time "inicio", "final" , y entre ellas llamamos a nuestra funcion
inicio = time.time()
prueba_while(1000000)
final = time.time()
# 5 despues hacemos una simple resta
print(final-inicio)
"""

# timeit (declaracion,setup,number=numero) :
# declaracion --> recibe el código que cuya duración de ejecución queremos medir
# setup --> : recibe las instrucciones que el parámetro declaracion requiere para funcionar
# number --> number: cantidad de veces que se evaluará el código para obtener su tiempo de ejecución mínimo.

# ejemplo con timeit
"""# 1)Creamos dos funciones que hacen exactamente lo mismo


def prueba_for(numero):
    lista = []
    for i in range(1, numero+1):
        lista.append(i)
    return lista


def prueba_while(numero):
    contador = 1
    lista = []
    while contador <= numero:
        lista.append(contador)
        contador = contador+1
    return lista


# 2) vamos hacer una variables una donde va ir la funcion añadiendole el valor, en este caso la variable se llama declaracion
declaracion = '''

prueba_for(10)
'''

# 3 vamos hacer otra variable donde va ir el codigo de mi funcion for(), en este caso mi variable se llama mi_setup
mi_setup = '''

def prueba_for(numero):
    lista = []
    for i in range(1, numero+1):
        lista.append(i)
    return lista


'''
# 4 creamos una variable, en este caso se llama duracion
# 5 dentro de esa variable vamos a utilizar el metodo timeit.timeit() --> y dentro de el vamos añadir las variables posteriormente creadas
# 6 ) Es de decir --> timeit.timeit(declaracion,mi_setup,number=("el numero de veces que queremos que se repita nuestro codigo"))
duracion = timeit.timeit(declaracion, mi_setup, number=1000000)
# 7)imprimimos para ver su duracion
print(duracion)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# posteriormente hacemos lo mismo con la otra funcion a evaluar
declaracion2 = '''

prueba_while(10)


'''
mi_setup2 = '''

def prueba_while(numero):
    contador = 1
    lista = []
    while contador <= numero:
        lista.append(contador)
        contador = contador+1
    return lista

'''
duracion2 = timeit.timeit(declaracion2, mi_setup2, number=1000000)
print(duracion2)
"""
"""************************************************************************Modulo Math**********************************************************************"""
# ejemplos del modulo math
# 1 ejemplo
"""resultado = math.log(25, 10)
logaritmo2 = math.log10(25)

print(resultado)
print(logaritmo2)
"""
# 2 ejemplo
"""resultado = math.sqrt(math.pi)
print(resultado)
"""
# ejemplo factorial de un numero
"""resultado=math.factorial(7)
print(resultado)"""

"""***********************************************************************Modulo re*********************************************************************************"""
# Ejemplo 1)
"""texto = "Si necesitas ayuda llama al siguiente numero (601)-306-4471 opcion 3 de la linea telefonica "
patron = "necesitas"

# search()--> buscar
busqueda = re.search(patron, texto)
# span()--> ubicacion de donde esta la palabra "necesitas", segun los indices , promedia un rango(inicio,hasta)
print(busqueda.span())
# star() ---> ubicacion del inicio de esa palabra
print(busqueda.start())
# end( )---> ubicacion del final de esa palabra
print(busqueda.end())
"""
# Ejemplo 2)
"""texto = "Si necesitas ayuda llama al siguiente numero (601)-306-4471 opcion 3 de la linea telefonica "
patron = "necesitas"

# findall--> buscar cuantas veces se repite esa palabra
busqueda = re.findall(patron, texto)
# para buscar esa palbra
print(busqueda)
# para buscar cuantas veces se repite
print(len(busqueda))
"""
# Ejemplo 3)
"""texto = "Llama al 317-470-1221 ya mismo"
patron = r'\d\d\d-\d\d\d-\d\d\d\d'
resultado = re.search(patron, texto)

print(resultado.group())"""

# Ejemplo 4
"""texto = "Llama al 317-470-1221 ya mismo"
patron = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
resultado = re.search(patron, texto)
#para imprimir por indices nuestro numero telefonico
print(resultado.group(2))
"""
# Ejemplo 5
"""# \D ---> para decirle a python que nos genere una clave identica con cierto numero de caracteres de tipo string ""
# \w ---> para decirle a pytthon que nos genere una clave identica con cierto nuero de caracteros de tipo int
clave = input("ingrese su clave : ")
patron = r'\D{2}\w{5}'
chequear = re.search(patron, clave)
print(chequear)
"""
# Ejemplo 6
"""texto = "No atendemos los lunes por la tarde "
buscar = re.search(r'lunes|martes', texto)
print(buscar)"""

# Ejemplo 7
"""texto = "No atendemos los lunes por la tarde "
buscar = re.search(r'demos...|martes', texto)
print(buscar)"""

# Ejemplo 8
"""# separar nuestro texto por medio de cadena de caracteres
#re.findall()-->devuelve una lista que contiene todos los hallazgos del patrón
texto = "no atendemos los lunes por la mañana "
buscar = re.findall(r'[^\s]+', texto)
print(buscar)"""

# Ejemplo 9
"""# para verificar si un email tiene @ y .com

# \w --> Para caracteres alfanumericos como por ejemplo el '@'
# \.  --> como por ejemplo un caracteres cualquiera


def verificaremail(email):
    patron = r'@\w+\.com'
    chequear = re.search(patron, email)
    if chequear:
        print("ok")
    else:
        print("invalido")


verificaremail("rodolfomartiens123@gmail.com")
"""

# Ejemplo 10
"""def verificar_saludo(frase):
    patron = 'Hola'
    chequear = re.findall(patron, frase)
    if chequear:
        print("Ok")
    else:
        print("No has saludado")


verificar_saludo("Buenas")
"""

# Ejemplo 11
"""# \w --> caracteres alfanumericos
# \d --> caracteres numericos


def verificar_cp(cp):
    patron = r'\w{2}\d{4}'
    chequear = re.search(patron, cp)
    if chequear:
        print("Ok")
    else:
        print("codigo postal invalido")


verificar_cp("xx1234")"""
