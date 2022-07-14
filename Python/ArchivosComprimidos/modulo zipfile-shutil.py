"""*********************************************************************Modulo zipfile y shutil*******************************************************************"""
import zipfile
import shutil

# 1 Ejemplo)Comprimir un archivo
"""# 1) creamos la carpeta con el metodo zipfile.ZipFile("nombre del archivo . zip")--> nombre de la carpeta donde se va a guardar nuestro archivo comprimido
mi_zip = zipfile.ZipFile('ArchivoComprimido.zip', 'w')

# 2)elegimos los archivo que queremos comprimir a travez del metodo variable.write("nombre del archivo")
mi_zip.write('main.txt')
mi_zip.write('main2.txt')
# 3) cerramos la carpeta
mi_zip.close()"""

# 2 Ejemplo)Descomprimir un Archivo...

"""zip_abierto = zipfile.ZipFile('ArchivoComprimido.zip', 'r')
zip_abierto.extractall()
"""

# 3 Ejemplo)
"""#  En esta ocacion vamos a comprimir archivos de otra ruta y enviarlo comprimido a nuestra ruta origen

# 1)primero creamos una variable donde va ir la ruta en el cual esta el archivo que queremos comprimir
carpeta_origen = 'D:\\usuario\Downloads\\ORACLE-ONE\\CarpetaSuperior'
# 2)  creamos otra variable en el cual le indicamos com se va a llamar el archivo comprimido
archivo_destino = 'todocomprimido'
# 3) con la funcion make_archive('nombre del archivo','extension','ruta donde esta el archovo')
shutil.make_archive(archivo_destino, 'zip', carpeta_origen)
"""
