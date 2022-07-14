
import pandas as pd

rutaFileCsv = 'https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv?raw=true'


def listaPeliculas(rutaFileCsv: str) -> str:

    if rutaFileCsv.split('.')[-1] == "csv?raw=true":
        try:
            read = pd.read_csv(rutaFileCsv)
            indices = read[['Country', 'Language', ' Gross Earnings']]
            pivot = indices.pivot_table(index=['Country', 'Language'])
            return pivot.head(10)
        except:
            print("Error al leer el archivo de datos")
    else:
        print("extension_invalida")


print(listaPeliculas(rutaFileCsv))
