
"""*******************************************MANEJO DE ARCHIVOS CSV/PYTHON***************************"""
# ejemplo para crear un Data frame a partir de diccionarios y exportarlo aun CVS para verlo en exel

from cProfile import label
import matplotlib.pyplot as plt
from turtle import color
from numpy import var
import requests
import json
from operator import index


import pandas as pd
# 1 ) creamos nuestro DataFrame
"""tablaDatos = {'nombres': ['cristian', 'maria', 'oscar', 'daniel', 'umberto'],
              'apellidos': ['galeano', 'sanchez', 'ramirez', 'alfredo', 'leon'],
              'edad': [19, 25, 19, 23, 24],
              'estatura': [1.69, 1.60, 1.70, 1.58, 1.65],
              'profesiones': ['ing de sistemas', 'ing industrial', 'psicologo', 'ing electronico', 'ing mecatronico']


              }

TablaDatos = pd.DataFrame(tablaDatos)
print(TablaDatos)

# 2 )Exportamos nuestro Data Frame a un CSV.
# TablaDatos.to_csv('cristianing.csv')
print("el archivo cvs ah sido exportado con exito ")"""


# EJEMPLO PARA EXPORTAR UN ARCHIVO CSV A PYTHON
# 1 usamos la funcion read_csv
# 2 usamos la ruta donde este el archivo
"""archivos = pd.read_csv(
    "D:\\usuario\\Documents\\python\\cristianing.csv")
archivos.head()
print(archivos)
"""
# EJEMPLO PARA CAMBIAR LOS NOMBRES DE LOS DATOS DE NUESTRO DATA FRAME, filas y columnas
# la funcion names sirve para cambiar los nombres de la columna de nuestro data frame
# la funcion skiprows sirve para irnorar filas y que no aparezcan en nuestro Data Frame

"""archivos = pd.read_csv(
    "D:\\usuario\\Documents\\python\\cristianing.csv", names=["nombres", "apellidos", "edades", "estatura", "profesiones"], skiprows=1)
archivos.head()
print(archivos)"""

"""*********************************MANEJO DE ARCHIVOS EN EXCEL **************************"""
# PRIMER EJEMPLO  CREAR UN ARCHIVO DESDE PYTHON Y EXPORTARLO A UN EXCEL


# 1 CREAMOS NUESTRO ARCHIVO DATA FRAME
"""tablaDatos = {'nombres': ['cristian', 'maria', 'oscar', 'daniel', 'umberto'],
              'apellidos': ['galeano', 'sanchez', 'ramirez', 'alfredo', 'leon'],
              'edad': [19, 25, 19, 23, 24],
              'estatura': [1.69, 1.60, 1.70, 1.58, 1.65],
              'profesiones': ['ing de sistemas', 'ing industrial', 'psicologo', 'ing electronico', 'ing mecatronico']
              }

DataFrame = pd.DataFrame(tablaDatos)

print(DataFrame)

# 2 EXPORATMOS NUESTRO ARCHIVO A EXCEL
try:
    DataFrame.to_excel("D:\\usuario\\Documents\\python\\smithcristian.xlsx")
    print("el archivo se ejecuto con exito")
except:
    print("no se ha encontrado el archivo")"""


# SEGUNDO EJERCICIO , TRAER UN ARCHIVO EXCEL YA CREADO Y LO TRAEMOS A PYTHON PARA VISUALIZARLO
# la funcion index_col = sirve para quitar los index que tienen 0 de nuestro DataFrame
"""excel = pd.read_excel(
    "D:\\usuario\\Documents\\python\\smithcristian.xlsx", index_col=0)
try:
    print(excel)

except:
    print("no se encontro con exito")"""

"""*********************************** MANEJO DE ARCHIVOS TXT/PYTHON*******************************************"""
# PRIMER EJEMPLO
#   vamos abrir un archivo txt existente y vamos agregarle texto

"""abrir = open("D:\\usuario\\Documents\\python\\main.txt", "w")

nombres = ["cristian", "smith", "galeano", "sanchez"]
for i in nombres:
    abrir.write(i+"\n")

abrir.close"""
# SEGUNDO EJEMPLO

"""# vamos abrir un archivo y leer el archivo txt
archivo = open("D:\\usuario\\Documents\\python\\main.txt", "r")
lista = []

for linea in archivo:
    lista.append(linea)
archivo.close()
print(lista)

# para eliminar los saltos de linea "\n" en nuestra lista
# la funcion rstrip()--> Este método se utiliza para eliminar todos los espacios en blanco iniciales y finales de una cadena. También tiene en cuenta los tabuladores y saltos de línea. En realidad strip() devuelve una copia de la cadena con los caracteres iniciales y finales en blanco eliminados.
sinsaltodelinea = [letra.rstrip('\n')for letra in lista]
print(sinsaltodelinea)"""

"""*************************************MANEJO DE ARCHIVOS JSON/PYTHON****************************************"""

# EJEMPLO PARA EXPORTAR UN ARCHIVO DESDE PYTHON AL FORMATO JSON

# primero creamos algun elemento para poderlo exportar a un formato json
""""profesiones = {
    'nombres': 'cristian smith ',
    'apellidos': 'galeano sanchez',
    'profesion': 'ingeniero de sistemas',
    'edad': 19,
    'estatura': 1.69
}

# segundo creamos el json
try:
    with open("D:\\usuario\\Documents\\python\\testerqa.json", "w") as file:
        json.dump(profesiones, file, indent=2)
except:
    "el archivo no se ha exportado con exito"""

# EJEMPLO PARA LEER UN ARCHIVO JSON DESDE PYTHON

"""with open("D:\\usuario\\Documents\\python\\testerqa.json") as file:
    info = json.load(file)


for clave in info.items():
    print(clave)"""

# TERCER EJEMPLO
# ejemplo para importar una api
# pagina web  ip-api.com

"""variable = requests.get('http://ip-api.com/json/190.143.15.67')
print(variable)

variable2 = json.loads(variable.content)

print(variable2)"""
