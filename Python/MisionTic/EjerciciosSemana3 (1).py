# Ejercicio No. 1 Variables de incremento y decremento

"""x=1

x=x+1
x+=1

x-=2
print(x)"""

# Ejercicio No. 2 . "Ciclo while
"""numero=5

while numero>3:
    print(numero)
    numero-=1

#For imprimir los números del 1 al 10 con for

rango=range(2,11,2)
print('Números del Pares 1 al 10 con for ')
for i in rango:
    print(i)

nombre='Calletana'

#for i in nombre:
#    print(i)"""

# Ejercicio No. 3 Factorial

"""def factorial(n: int) -> int:
    resultado = 1
    numero_actual = 2
    while numero_actual <= n:
        resultado = resultado * numero_actual
        numero_actual += 1
    return resultado

print(factorial(3))"""

# Ejercicio No. 4. While con else

"""promedio, total, contar = 0.0, 0, 0
mensaje = "Introduzca la nota de un estudiante (-1 para salir): "

grado = int(input(mensaje))#3
while grado != -1:#True#True#False
    total = total + grado#3#8
    contar += 1#1#2
    grado = int(input(mensaje))#5#-1
else:
    promedio = total / contar#8/2#4
    print("Promedio de notas del grado escolar: " + str(promedio))#4"""

# Ejercicio No. 5 Sentencias break y continue

"""variable = 10

while variable > 0:#True#True#True#True#True
    print('Actual valor de variable:', variable)#10#9#8#7#6
    variable = variable -1#9#8#7#6#5
    if variable == 5:#False#False#False#FalseTrue
        break"""


"""variable = 10

while variable > 0:
    variable = variable -1
    if variable == 5:#True
        continue#Continue
    print('Actual valor de variable:', variable) # no imprime el 5"""

# Ejercicio No. 6.. Lista

"""lista=[1,2,3,4,5]

lista2=['nombres', 'apellidos']

listas3=[1,2,'nombres']

listas4=[[1,2,3],5]


print(listas4[1])

#Rangos --- trozos

print(lista[1:4])

listaEjemplo = [1, 2.5, 'DevCode', [5,6] ,4]

print(listaEjemplo[0:5:2])

print('El tamaño de la lista es: ', len(listas4[0]))"""

# Métodos
# append()
# agrega un elemento al final de la lista

"""listaUsuario=[]

nombre=input('Digite su nombre : ')
apellido=input('Digite su apellido : ')

listaUsuario.append(nombre)
listaUsuario.append(apellido)

print(listaUsuario)"""

# Método count()
# Contar la cantidad de veces que aparece cierto elemento en mi lista

"""listaUno=[2,3,4,2,5,6,7,9]

print('Lista original', listaUno)
print(f'El número dos aparecece {listaUno.count(2)} ')

#Método extend()
#Agregar iterables al final de la lista

rango=range(5,8)
listaUno.extend(rango)
print(f'Agregando con extend un rango de números {listaUno}')

#Médoto index()
#Devuelve el índice del elemento

print(f'El índice del elemento 4 es: {listaUno.index(2)}')

#Método insert()
#Insertar un elemento en un índice indicado

listaUno.insert(2,2.5)
print(f'Insertamos elemento 2.5 en el índice 2, la nueva lista es: {listaUno}')

#Método pop()
#Devuelve y elimina el último elemento de la lista

print(f'El último elemento de la lista es: {listaUno.pop()}')
print(f'La nueva lista es: {listaUno}')

#Método remove()
#Elimina la primera aparición de un elemento en la lista

listaUno.remove(2)
print(f'La nueva lista es: {listaUno}')

#Método reverse()
#Invierte el orden de la lista

listaUno.reverse()
print(f'La nueva lista con reverse {listaUno}')

#Método sort()
#Ordenar los elementos de la lita de menor a mayor
listaUno.sort()
print(f'La lista ordenada es: {listaUno}')
listaUno.reverse()
print(f'Lista ordenada de mayor a menor: {listaUno} ')"""

# Ejercicio No.7 --- Listas paralelas

"""nombres=[]
edades=[]

rango=range(0,5)

for i in rango:
    nombre=input('Por favor digite su nombres: ')
    edad=int(input('Por favor digite su edad: '))
    nombres.append(nombre)
    edades.append(edad)

print('Las personas mayores a 18 años son: ')

for i in rango:
    if edades[i]>=18:
        print(nombres[i])"""


# Ejercicio No. 8. Listas compuestas

"""lista=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

#Imprimir un elemento (una de sus lista)

print(lista[2])

#imprimir los elementos que están dentro de listas internas

print(lista[2][1])

#imprimir los elementos de la lita contenida [0]

for i in range(len(lista[2])):
    print(lista[2][i])

#Recorrer todos los elementos de lista
print('Todos los elementos de la lista')
for i in range(len(lista)):
    for j in range(len(lista[i])):
        print(lista[i][j])"""


# Ejercicio No. 9 "Listas compuestas - Padres e hijos"
"""padres=[]
hijos=[]
rango=range(0,3)
for i in rango:
    nombrePadre=input('Por favor digite el nombre del padre: ')
    nombreMadre=input('Por favor digite el nombre de la madre: ')
    padres.append([nombrePadre,nombreMadre])
    cantidadHijos=int(input('Cuántos hijos tiene la familia: '))
    hijos.append([])
    rangoHijos=range(0,cantidadHijos)
    for j in rangoHijos:
        nombreHijo=input('Por favor digite el nombre de su hijo(a): ')
        hijos[i].append(nombreHijo)
for i in rango:
    print(f'Nombre del padre: {padres[i][0]}')
    print(f'Nombre del madre: {padres[i][1]}')
    for j in range(len(hijos[i])):
        print(f'Hijo(a): {hijos[i][j]}')
print('Listado de padres con sus hijos')
for i in rango:
    print(f'Nombre del padre {padres[i][0]}')
    print(f'Cantidad de hijos: {len(hijos[i])}')"""

# Ejercicio No. 10 "Tuplas"
# Diccionarios={}
# Listas=[]
# Tupas=()


"""tupla=(1,2,3,4,5)
vocales='a','e','i','o','u'

print(tupla)
print(vocales)

print(type(tupla))

tuplaX='x',

print(type(tuplaX))

#imprimir los elementos de la tupla

print(tupla[2])
print(vocales[1:4])

print(len(tupla))


print(f'La vocal a aparece: {vocales.count("a")}')

print(f'La vocal e está en el índice: {vocales.index("e")}')"""

# Ejercicio No. 11 Tuplas "Cosméticos"
"""def Cosmeticos(ventas: list):
    ventacliente = {}
    for Identificador, NombreProducto, Descripcion in ventas:
        if ventacliente.get(Identificador) == None:
            ventacliente[Identificador] = []                                  
        ventacliente[Identificador].append((NombreProducto, Descripcion))                 
    print(ventacliente) #Ocultar al ejecutar
    return ventacliente

Cosmeticos([
    (2001,'Labial', 'Pintura de mujer Labial'),
    (2010,'Sombra','Sombra de ojos')])
print()"""

# Ejercicio No. 12 "Conjuntos"
#Dict ---{key:value}
#Conjuntos --- {}

"""tupla=(1,2,3,4)
conjunto={2,4,5,3,4}

print('Ésta es la tupla')
print(tupla)
print('Éste es el conjunto')
print(conjunto)

conjunto.add(22.6)

print(conjunto)"""

# Ejercicio No. 13 "Contenedores"

from functools import reduce
diccionarioEstudiantes = {
    'E3454fdf': {
        'nombres': 'Laura',
        'apellido': 'Jaramillo',
        'acudientes': ['Andrea', 'Juan'],
        'promedio': 5.0
    },
    'Egg56dfg': {
        'nombres': 'Samir',
        'apellido': 'Gómez',
        'acudientes': ['Alejandro', 'Sofía'],
        'promedio': 5.0
    },
    'FHT43523': {
        'nombres': 'Sara',
        'apellido': 'Cabrera',
        'acudientes': ['Carlos', 'Amparo'],
        'promedio': 5.0
    },
    'Z4edkdf': {
        'nombres': 'Iván',
        'apellido': 'Arcila',
        'acudientes': ['Esposa'],
        'promedio': 5.0,
        123: 'Este estudiante es alérgico al maní'
    },
}

# print(diccionarioEstudiantes)

# print(diccionarioEstudiantes['FHT43523'])

#Diccionario --- key -- value
# Sólo por su key o por su valor
