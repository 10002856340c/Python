
""""********************************************************************Decoradores **********************************************************************"""

# 1)Ejemplo

"""def inicio_aplicacion(variable):

    def mayusculas(palabra):
        print(palabra.upper())

    def minusculas(palabra):
        print(palabra.lower())
# IMPORTANTE --> cuando se llama a una funcion que esta dentro de una funcion principál , se debe llamar sin los parentesis
    if variable == "mayus":
        return mayusculas
    elif variable == "minuscu":
        return minusculas


variable = inicio_aplicacion("minuscu")
variable("PALABRA")"""

# 2)Ejemplo probando decoradores @

""""# 1) primero creamos una funcion para poder hacer la funcionalidad


def inicio_operacion(funcion):

    # 2) Creamos una funcion en el cual queremos que se añada el codigo

    def otra_funcion(palabra):
        print("hola")
        funcion(palabra)
        print("adios ")
    return otra_funcion

# 4) Agregamos atravez del @ la funcion principal que en este caso es @inicio_operacion


@inicio_operacion
# 5)creamos otra funcion aparte de la funcion principal, con funcionalidades especiales , en este caso es convertir las letras a mayusculas
def mayusculas(palabra):
    print(palabra.upper())


@inicio_operacion
# 6)creamos otra funcion aparte de la funcion principal, con funcionalidades especiales , en este caso es convertir las letras a minusculas
def minusculas(palabra):
    print(palabra.lower())

#7)llamamos las funciones 
minusculas("CRISTIAN")
mayusculas("perro")
"""

# Ejemplo probando sin @ en decoradores


"""def otra_funcion(funcion):

    def Ejecucion(palabra):
        print("hola")
        funcion(palabra)
        print("adios")
    return Ejecucion


def mayusculas(palabra):
    print(palabra.upper())


def minusculas(palabra):
    print(palabra.lower())


ejecucion2 = otra_funcion(mayusculas)
print(ejecucion2("cristian"))"""

"""****************************************************************Generadores ****************************************************************************"""
# generadores --> Los generadores son tipos especiales de funciones que devuelven un iterador que no almacena su contenido completo en memoria, sino que "demora" la ejecución de una expresión hasta que su valor se solicita


"""# Para este ejemplo veremos una nueva funcion que reemplaza al return , que en este caso seria yield--> que significa rendir o producir


# 1)En esta primera funcion vemos un return normal que se va a generar apartir del bucle que estamos haciendo
def principal():

    lista = []
    for i in range(1, 5):
        lista.append(i*10)
    return lista

# 2) A la hora de querer hacer un generador en vez del return hacemos un yield, que en este caso nos ocupa menos espacio de memoria


def generador():

    for i in range(1, 5):
        yield i*10


# llamamos normal la funcion
print(principal())

# A la hora de querer ver la funcion generador tenemos que primero meterla en una variable para poder ejecutarla
variable = generador()
# despues tenemos que poner el next para que la variable se ejecute con el generador
print(next(variable))

# POR CADA VEZ QUE EJECUTEMOS EL CODIGO NOS VA A IMPRIMIR UN NUMERO DIFERENTE QUE ESTA GUARDADO, YA QUE EN ESTE CASO EL RANGO DEL BUCLE ESTA DEL 1,5
print(next(variable))


print(next(variable))


print(next(variable))
"""
# 2)Ejemplo


"""def mi_generador():
    x = 1
    yield x

    x = x+1
    yield x

    x = x+1
    yield x


variable = mi_generador()
print(next(variable))
print(next(variable))
print(next(variable))"""


"""def mi_generador():
    variable = 1
    while True:
        yield variable
        variable += 1


generador = mi_generador()
print(next(generador))
"""

# 3)Ejemplo multiplos de 7
# itertools.count()--> le permite a uno crear un rango infinito


"""import itertools
def mi_generador(numero):
    for x in itertools.count(1):
        yield x*numero


generador = mi_generador(7)
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
"""
# 4)Ejemplo


def vidas(x):

    x = "Te quedan 3 vidas"
    yield x

    x = "Te quedan 2 vidas"
    yield x

    x = "Te queda 1 vida "
    yield x

    x = "Game Over"
    yield x


generador = vidas(3)
print(next(generador))
print(next(generador))
print(next(generador))
