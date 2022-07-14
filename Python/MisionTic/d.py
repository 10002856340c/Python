
import pandas as pd

rutaFileCsv = 'https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv?raw=true'


def listaPeliculas(rutaFileCsv: str) -> str:

    if rutaFileCsv.split('.')[-1] == 'csv?raw=true':
        try:
            leer = pd.read_csv(rutaFileCsv)
            dataframe = leer[["Country", "Language", "Gross Earnings"]]
            pivot = dataframe.pivot_table(index=["Country", "Language"])
            return pivot.head(10)
        except:
            print("ruta no encontrada")
    else:
        print("Extensión inválida")


print(listaPeliculas(rutaFileCsv))
