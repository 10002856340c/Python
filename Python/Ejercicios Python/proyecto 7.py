
"""****************************PROGRAMACION ORIENTADA A OBJETOS (POO)********************************"""

# 1 ejemplo


"""class PlataformaStreaming:
    pass


netflix = PlataformaStreaming()
hbo_max = PlataformaStreaming()
amazon_prime_video = PlataformaStreaming()"""

# 2 ejemplo

"""
class Casa:

    def __init__(self, color: str, cantidad_pisos: int) -> None:
        self.color = color
        self.cantidad_pisos = cantidad_pisos


casa_blanca = Casa("blanco", 4)


print(
    f"mi casa es de color {casa_blanca.color} y tiene  {casa_blanca.cantidad_pisos} pisos")"""

# 3 ejemplo

"""
class Cubo:
    caras = 6

    def __init__(self, color) -> None:
        self.color = color


cubo_rojo = Cubo("rojo")

print(cubo_rojo.color)
print(cubo_rojo.caras)"""

# 4 ejemplo


"""class Personaje:
    real = False

    def __init__(self, especie: str, magico: bool, edad: int) -> None:
        self.especie = especie
        self.magico = magico
        self.edad = edad

    def peliculas(self):
        print(f"a los{self.edad} hizo su primera pelicula")

    def metas(self, metas):
        self.metass = metas
        print(f"cuando cumplio 23 años cumplio su meta que era {self.metass}")


harry_poter = Personaje("Humano", True, 17)
print(
    f"harry poter es un {harry_poter.especie}, es magico ? = {harry_poter.magico} y tiene una edad {harry_poter.edad}")

print(harry_poter.metas("ser actor"))"""


# ejemplo 5

"""class Perro:

    def ladrar(self):
        print("Guau !")


perro = Perro()
perro.ladrar()
print(perro)"""

# ejemplo 6


"""class Mago:
    def lanzar_hechizo(self):
        print("!Abracadabra¡")


merlin = Mago()
merlin.lanzar_hechizo()"""


"""class Alarma:
    def postergar(self, cantidad_minutos: int):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")


sonar = Alarma()
print(sonar.postergar(150))"""

"""********************************************METODOS DE INSTANCIA ************************************************"""
# Los métodos de instancia son los métodos normales, de toda la vida, que hemos visto anteriormente. Reciben como parámetro de entrada self que hace referencia a la instancia que llama al método. También pueden recibir otros argumentos como entrada. Para saber más: El uso de "self" es totalmente arbitrario.
# Los metodos de instancia tiene 3 caracteristicas principales:
# 1)Acceden y modifican atributos del objeto es decir de la funcion
# 2)Acceder a otros metodos
# 3)Modificar el estado de clase


# 1)Creamos una clase
""""
class Pajaro:
    def __init__(self, color: str, especie: str) -> None:
        self.color = color
        self.especie = especie

    # 2)Creamos una funcion
    def piar(self):
        print("Pio")
     # 3)Creamos otra funcion

    def volar(self, metros: int):
        print(f"el pajaro vuela {metros} metros")
        self.colorPajaro()

     # 4)Creamos una tercera funcion

    def colorPajaro(self):
        self.color = "negro"
        print(f"el color del pajaro es de color {self.color}")


federico = Pajaro("rojo", "tukan")
federico.volar(50)"""
"""***************************************************METODOS DE CLASE*********************************************************"""
# Python permite definir métodos de clase para esto. Los métodos de clase son aquellos que están ligados directamente con los atributos definidos en la clase que los contiene. Para definir un método de clase se utiliza el decorador @classmethod y por convención se utiliza cls como argumento inicial en lugar de self .
# 1)Los metodos de clase no pueden estar asociados con los metodos de instancia
# 2)pueden manipular los datos de una variable dentro de la clase


"""class Pajaro:
    variables = False

    def __init__(self, color: str, especie: str) -> None:
        self.color = color
        self.especie = especie

    def piar(self):
        print("Pio")

    def volar(self, metros: int):
        print(f"el pajaro vuela {metros} metros")
        self.colorPajaro()

    def colorPajaro(self):
        self.color = "negro"
        print(f"el color del pajaro es de color {self.color}")

    @classmethod
    def poner_huevos(cls, cantidad: int):
        print(f"puso {cantidad} huevos")
        # se puede modificar la variable que esta dentro de la  clase de la siguiente manera
        cls.variables = True
        print(Pajaro.variables)


federico = Pajaro("rojo", "tukan")
federico.poner_huevos(10)"""

# ejemplo de metodos estaticos


"""class Mascota:
    @staticmethod
    def respirar():
        print("Inhalar...Exhalar")


mascota = Mascota()
mascota.respirar()"""

# ejemplo de metodos de clase


"""class Jugador:
    vivo = True

    @classmethod
    def revivir(cls):
        cls.vivo = False
        print(Jugador.vivo)


jugador = Jugador()
jugador.revivir()"""

# ejemplo de metodos de instancia


"""class Personaje:
    def __init__(self, cantidad_flechas: int) -> None:
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flechas(self):
        print(f"tiene una cantidad {self.cantidad_flechas - 1} flechas")


personaje = Personaje(10)
personaje.lanzar_flechas()"""

"""**********************************************METODOS DE HERENCIA *************************************************"""

"""# 1) un ejemplo sseria crear una clase que tenga un metodo o funcion de instancia que haga una funcion en especifico


class Animal:
    def sumas(self, num1: int, num2: int):
        self.suma = num1+num2
        print(f"la suma de {num1} y {num2} es {self.suma}")

# 2) creamos otra clase que cumpla una funcion ene especifico pero se le añade o se hereda la clase "Animal"


class Pajaro(Animal):
    print("un ejemplo es la guiente suma")


# 3)ya solo es llamar a la clase "Pajaro" y va heredar la funcion o el metodo de la clase "Animal" sin tener necesidad de invocar  a la clase padre "Anima"
hola = Pajaro()
hola.sumas(2, 5)"""

# ejemplo 1


"""class Persona:
    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre = nombre
        self.edad = edad


class Alumno(Persona):
    pass"""

# ejemplo 2:


"""class Mascota:

    def __init__(self, edad: int, nombre: str, cantidad_patas: int) -> None:
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas


class Perro(Mascota):
    pass"""

# ejemplo 3


"""class Vehiculo:
    def acelerar(self):
        pass

    def frenar(self):
        pass


class Automovil(Vehiculo):
    pass"""
"""******************************************METODOS DE HERENCIA EXTENDIDA******************************************************"""
"""# 1) un ejemplo seria crear una clase que tenga un metodo o funcion de instancia que haga una funcion en especifico

# En este ejemplo vamos hacer dos clase en el cual la clase padre "Animal" y la clase "hij@" va a heredar sus atributos y funciones ,


class Animal:
    def __init__(self, edad: int, color: str) -> None:
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")

    def hablar(self):
        print("este animal ha nacido")
# 2) creamos otra clase que cumpla una funcion en especifico pero se le añade o se hereda la clase "Animal"


class Pajaro(Animal):

    def hablar(self):
        print("pio")

    def volar(self, metros: int):
        print(f"el pajaro vuela {metros} metros")


# 3) ya solo es llamar a la clase "Pajaro" y va heredar la funcion o el metodo de la clase "Animal" sin tener necesidad de invocar  a la clase padre "Anima"
# posteriormente tambien se le va a heredar los atributos creados en la clase padre que enbte caso es la clase "Animal"
# tambien facilmente se puede llamar las funciones asignadas ya sean las funciones heredadas de otra clase o la funciones de la clase misma que hemos llamado
piolin = Pajaro(18, "verde")
piolin.volar(50)"""

# 2 ejemplo )

# En este ejemplo vamos a a signar atributos nuevos a la clase hija --> "Pajaro" que ha heredado atributos de la clase padre --> "Animal"
# tambien conoceremos una funcion muy utilizada cuando se quiere soobrescribir los atributos propiamente heredados de la clase padre , y queramos agragar otro atributo a la clase hija con la funcion  ->  super().__init__(variable1,variable2)


"""class Animal:
    def __init__(self, edad: int, color: str) -> None:
        self.__edad = edad
        self.__color = color

    def nacer(self):
        print("Este animal ha nacido")

    def hablar(self):
        print("este animal ha nacido")
# 2) creamos otra clase que cumpla una funcion en especifico pero se le añade o se hereda la clase "Animal"


class Pajaro(Animal):
    def __init__(self, edad: int, color: str, altura_vuelo: int) -> None:
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print("pio")

    def volar(self, metros: int):
        print(f"el pajaro vuela {metros} metros")


# 3) ya solo es llamar a la clase "Pajaro" y va heredar la funcion o el metodo de la clase "Animal" sin tener necesidad de invocar  a la clase padre "Anima"
# posteriormente tambien se le va a heredar los atributos creados en la clase padre que enbte caso es la clase "Animal"
# tambien facilmente se puede llamar las funciones asignadas ya sean las funciones heredadas de otra clase o la funciones de la clase misma que hemos llamado
piolin = Pajaro(18, "verde", 50)
# se recomienda poner en una variable la clase heredada
mi_animal = Animal(10, "rojo")

piolin.volar(100)
"""

"""******************************************HERENCIA MULTIPLES**********************************************************************"""

# ejemplo 1
"""class Padre:
    def Hablar(self):
        print("Hola")

    def reir(self):
        print("jojo")


class Madre:
    def Hablar(self):
        print("ja ja")


class Hijo(Madre, Padre):
    pass


hijo = Hijo()
hijo.Hablar()
hijo.reir()
"""

# ejemplo 2
"""class Padre():
    def trabajar(self):
        print("Trabajando en el Hospital")

    def reir(self):
        print("Ja ja ja!")


class Madre():
    def trabajar(self):
        print("Trabajando en la Fiscalía")


class Hija(Madre, Padre):
    pass


hija = Hija()
hija.reir()
hija.trabajar()"""


# ejemplo 3

"""class Vertebrado:
    vertebrado = True


class Ave(Vertebrado):
    tiene_pico = True

    def poner_huevos(self):
        print("Poniendo huevos")


class Reptil(Vertebrado):
    venenoso = True


class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")

    def poner_huevos(self):
        print("Poniendo huevos")


class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")

    def amamantar(self):
        print("Amamantando crías")


class Ornitorrinco(Mamifero, Pez, Reptil, Ave):
    pass


animal = Ornitorrinco()
animal.caminar()
"""
# ejemplo 4


"""class Padre():
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"

    def reir(self):
        return "Jajaja"

    def hobby(self):
        return "Pinto madera en mi tiempo libre"

    def caminar(self):
        return "Caminando con pasos largos y rápidos"

# En este caso se sobrescribe el metodo def hobby y automaticamente se va a sobrescribir cuando uno lo llame


class Hijo(Padre):
    def hobby(self):
        return "Juego videojuegos en mi tiempo libre"


hijo = Hijo()
hijo.hobby()
"""
# Ejemplo 5

"""class Mago():

    def atacar(self):
        print("Ataque mágico")


class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")


class Samurai():
    def atacar(self):
        print("Ataque con katana")


uno = Mago()
dos = Arquero()
tres = Samurai()

Personajes = [dos, uno, tres]

for i in Personajes:
    i.atacar()"""

# ejemplo 6


"""class Mago():

    def defender(self):
        print("Escudo mágico")


class Arquero():
    def defender(self):
        print("Esconderse")


class Samurai():
    def defender(self):
        print("Bloqueo")


def personaje_defender(objeto):
    objeto.defender()


personaje_defender(Samurai())"""


# EJEMPLO DE ACOPLAMIENTO
"""class Mascota:
    tiene_patas = True
    pass


class Perro:
    def correr(self, objeto):
        if Mascota.tiene_patas:
            self.objeto = objeto


mascota = Perro()
print(mascota.correr("rapido"))
"""
# METODOS ESPECIALES
# Para mostrar objetos, Python indica que hay que agregarle a la clase un método especial, llamado __str__ que debe devolver una cadena de caracteres con lo que queremos mostrar. Ese método se invoca cada vez que se llama a la función str .
# ejemplos, hay muchos metodos especiales, que se pueden encontra en la documentacion d epython
# ___str___(self)--> para que nos devuelva algun str en especifico
# ___len__(self)--> para que nos devuelva algun numero
# ___del__(self)-->para que nos devuel algun str cuando se ejecute la fun del


class CD:
    def __init__(self, autor, titulo, cansiones) -> None:
        self.autor = autor
        self.titulo = titulo
        self.cansiones = cansiones

    def __str__(self) -> str:
        return f"album : {self.autor} de {self.cansiones}"

    def __len__(self):
        return self.cansiones

    def __del__(self):
        return print("el archivo cd ha sido eliminado")


mi_cd = CD("cristian", "python", 40)


print(len(mi_cd))

del mi_cd
# /-------------------------------------------------------------------------------------------------------------------------/


class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __str__(self) -> str:
        return f' "{self.titulo}" , de autor {self.autor}'


libros = Libro("el amor", "cristian", "10")
print(libros)


# /-------------------------------------------------------------------------------------------------------------------------/
class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __len__(self):
        return self.cantidad_paginas


libros = Libro("el amor", "cristian", "10")
