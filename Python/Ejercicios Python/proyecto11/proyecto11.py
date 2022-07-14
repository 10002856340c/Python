"""******************************************************************Buscador de numeros de serie*******************************************************"""

import math
import re
import shutil
import os
import datetime
import time
from pathlib import Path
import zipfile

from numpy import mat

inicio = time.time()
# 1) descomprimimos nuestro archivo .zip
"""zip_abierto = zipfile.ZipFile('Proyecto9.zip', 'r')
zip_abierto.extractall()
"""
# 2 ) creamos nuestra ruta
ruta = 'D:\\usuario\\Documents\\python\\UDEMY\\Python\\Ejercicios Python\\proyecto11\\Mi_Gran_Directorio'
Patron = r'N\D{3}-\d{5}'
hoy = datetime.date.today()
numerosEncontrados = []
archivosEncontrados = []


def buscar_numero(archivo, patron):
    este_archivo = open(archivo, 'r')
    texto = este_archivo.read()
    if re.search(patron, texto):
        return re.search(patron, texto)
    else:
        return " "


def crear_listas():
    # os.walk --> recorre el directorio indicado, y devuelve los nombres de carpetas, subcarpetas y archivos dentro de ellas en forma de tupla, a través de un generador.
    for carpeta, subcarpeta, archivos in os.walk(ruta):
        for x in archivos:
            # La clase Path permite representar rutas de archivos en elsistema de archivos de nuestro sistema operativo. Se destacapor su legibilidad frente a alternativas semejantes.
            resultado = buscar_numero(Path(carpeta, x), Patron)
            if resultado != " ":
                numerosEncontrados.append((resultado.group()))
                archivosEncontrados.append(x.title())


def mostrar_todo():
    indice = 0
    print("-"*50)
    print(f"Fecha de busqueda : {hoy.day} \ {hoy.month} \ {hoy.year}")
    print("\n")
    print("ARCHIVO \tNo DE SERIE")
    print("*"*10+"\t\t\t"+"*"*12)
    for y in archivosEncontrados:
        print(f"{y}\t{numerosEncontrados[indice]}")
        indice = indice+1
    print("\n")
    print(f"numeros encontrados : {len(numerosEncontrados)}")
    fin = time.time()
    # math.ceil sirve pararedondear haci arriba
    print(f"el tiempo fue : {math.ceil((fin-inicio))}")


crear_listas()
mostrar_todo()
