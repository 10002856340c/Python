import bs4
import requests
#  importamos las librerias

# 1 Ejemplo
"""# variables donde se alamacena la ruta de la pagina web
resultado = requests.get(
    'https://escueladirecta.com/p/excel-aplicado-al-analisis-financiero')
print(resultado.text)

# para indicar que vamos a empezar hacer web sacraping con bs4.BeautifulSoup(variable de la ruta,'lxml)
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
# para indicar con el metedo select que parte de la pagina queremos consultar
# el metodo getText()--> sirve para quitar las etiqutas las etiquetas html
# los indices se utilizar pa
print(sopa.select('h2')[0].getText())
parrafo_especial = sopa.select('p')[3].getText()
print(parrafo_especial)
"""
# 2 Ejemplo
"""# ponemos la ruta
variable = requests.get(
    'https://escueladirecta.com/p/analisis-de-datos-con-pandas-y-python')
# indicamos que vamos hacer con beautifulSoup
sopa = bs4.BeautifulSoup(variable.text, 'lxml')

# indicamos a que class o id , o div queremos hacer alusion en nuestro html
columna_lateral = sopa.select('.course-title ')
print(columna_lateral)
"""
# 3 Ejemplo Trabajando con Imagenes

"""resultado=requests.get('https://escueladirecta.com/courses')
sopa=bs4.BeautifulSoup(resultado.text,'lxml')
imagenes=sopa.select('.course-box-image')[0]['src']
print(imagenes)

imagen_curso1=requests.get(imagenes)


abrir=open('mi_imagen.jpg','wb')
abrir.write(imagen_curso1)
abrir.close()"""

# 4 Ejemplo  Explorar diferentes paginas o html de una pagina web

"""for n in range(1, 11):
    url_base = f'https://books.toscrape.com/catalogue/page-{n}.html'
    print(url_base)"""

# 5 Ejemplo Extraer toda la informacion de la pagina en la cual tenga esa clase
"""url_base = 'https://books.toscrape.com/catalogue/page-{}.html'
resultado = requests.get(url_base.format('1'))
soup = bs4.BeautifulSoup(resultado.text, 'lxml')
print((soup.select('.product_pod')))"""

# 6) Extraer las estrellas del  libro
"""url_base = 'https://books.toscrape.com/catalogue/page-{}.html'
resultado = requests.get(url_base.format('1'))
soup = bs4.BeautifulSoup(resultado.text, 'lxml')
libros = (soup.select('.product_pod'))

ejemplo = libros[0].select('.star-rating.Three')
print(ejemplo)"""

# 7) Extraer el titulo del libro
"""url_base = 'https://books.toscrape.com/catalogue/page-{}.html'
resultado = requests.get(url_base.format('1'))
soup = bs4.BeautifulSoup(resultado.text, 'lxml')
libros = (soup.select('.product_pod'))
ejemplo = libros[0].select('a')[1]['title']
print(ejemplo)"""
# 8) Combinar items buscados
"""url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

# Lista de tituloa con 4 o 5 estrellas
titulos_rating_alto = []
# iterar paginas
for pagina in range(1, 51):
    # crear soup en cada pagina
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
    # seleccionar datos de los libros
    libros = sopa.select('.product_pod')

    for libro in libros:

        # chequear libros 5 estrellas
        if len(libro.select('star-rating. Four')) != 0 or len(libro.select('star-rating. Five')):
            # guardar tirulo variable
            titulo_libro = libro.select('a')[1]['title']
            # Agregar el libro a la lista
            titulos_rating_alto.append(titulo_libro)

for t in titulos_rating_alto:
    print(t)
"""
