import bs4
import requests
#  importamos las librerias

# variables donde se alamacena la ruta de la pagina web
resultado = requests.get(
    'https://escueladirecta.com/p/excel-aplicado-al-analisis-financiero')
print(resultado.text)

# para indicar que vamos a empezar hacer web sacraping con bs4.BeautifulSoup(variable de la ruta,'lxml)
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
# para indicar con el metedo select que parte de la pagina queremos consultar
# el metodo getText()--> sirve para quitar las etiqutas las etiquetas html
print(sopa.select('h2')[0].getText())
parrafo_especial = sopa.select('p')[3].getText()
print(parrafo_especial)
