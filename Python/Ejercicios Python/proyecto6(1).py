import os
from pathlib import Path
from os import system


mi_ruta = Path(Path.home(), "Recetas")


def contar_recetas(ruta):
    contar = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contar += 1
    return contar


def inicio():
    system('cls')
    print("*"*50)
    print("*"*5 + "Bienvenido al administrador de  "+"*"*5)
    print("*"*50)
    print("\n")
    print(f"Las recetas se encuentran en {mi_ruta}")
    print(f"el total de recetas es de {contar_recetas(mi_ruta)}")

    # funcion isnumeric --> La función isnumeric() funciona de manera similar a la función isdigit() y proporciona un valor True si todos los caracteres de una cadena dada son números

    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1, 7):
        print("Elige una opcion :")
        print("""
        [1] - Leer Receta
        [2] - Crear Receta Nueva
        [3] - Crear Categoria Nueva
        [4] - Eliminar Receta
        [5] - Eliminar Categoria
        [6] - Salir del programa
         """)
        eleccion_menu = input()
    return int(eleccion_menu)


def mostrar_categorias(ruta):
    print("Categorias : ")
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1
    # la funcion iterdir()-->tienen un método llamado iterdir() que crea un iterador que recorre todos los archivos y carpetas de un directorio. Además, los objetos de clase Path contienen propiedades como name
    for i in ruta_categorias.iterdir():
        carpeta = str(i.name)
        print(f"[{contador} - {carpeta}]")
        lista_categorias.append(i)
        contador += 1
    return lista_categorias


def elegir_categoria(lista):
    eleccion = 'x'
    # funcion isnumeric --> La función isnumeric() funciona de manera similar a la función isdigit() y proporciona un valor True si todos los caracteres de una cadena dada son números
    while not eleccion.isnumeric() or int(eleccion) not in range(1, len(lista) + 1):
        eleccion = input("\n Elige una categoria :")

    return lista[int(eleccion) - 1]


def mostrar_recetas(ruta):
    print("Recetas : ")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 0
    for x in ruta_recetas.glob('*.txt'):
        receta = str(x.name)
        print(f"[{contador}] - {receta}")
        lista_recetas.append(x)
        contador += 1
    return lista_recetas


def elegir_recetas(lista):
    eleccion_receta = ' x '
    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1,  len(lista) + 1):
        eleccion_receta = input("\nElige una receta :")

    return lista[int(eleccion_receta) - 1]


def leer_receta(receta):
    print(Path.read_text(receta))


def crear_receta(ruta):
    existe = False
    while not existe:
        print("Escribe el nombre de tu nueva receta : ")
        nombre_receta = input() + '.txt '
        print("Describe tu nueva receta : ")
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
            # write text ()--> la funcion de write text es escribir un nuevo ,que esta copuesto por una ruta y una nueva informacion
            Path.write_text(ruta_nueva, contenido_receta)
            print(f"Tu receta {nombre_receta} ha sido creada")
            existe = True
        else:
            print("lo siento esa receta ya existe ")


def crear_categoria(ruta):
    existe = False
    while not existe:
        print("escribe el nombre de la nueva categoria :")
        nombre_categoria = input()
        ruta_nueva = Path(ruta, nombre_categoria)
        if not os.path.exists(ruta_nueva):
            # .mkdir --> lo que hace es crear una nueva categoria, dentro de la ruta que le estamos asignando
            Path.mkdir(ruta_nueva)
            print(f"tu nueva categoria es {nombre_categoria}")
            existe = True
        else:
            print("Lo siento pero ya existe esta categoria")


def eliminar_receta(receta):
    # unlink método () --> se utiliza para eliminar un archivo, si el archivo es un directorio devuelve un error.
    Path(receta).unlink()
    print(f"la receta {receta.name} ha sido eliminada")


def eliminar_categoria(categoria):
    # rmdir método () --> se utiliza para eliminar la ruta del directorio especificado. Sólo cuando esta carpeta está vacía antes de que de lo contrario pueden ser lanzadas OSError.
    Path(categoria).rmdir()
    print(f"la categoria {categoria.name} ha sido eliminada ")


def volver_inicio():
    eleccion = "x"
    while eleccion.lower() != "v":
        eleccion = input(" \n presione v para volver al menu")


finalizar_programa = False
while not finalizar_programa:

    menu = inicio()

    if menu == 1:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        mi_receta = elegir_recetas(mis_recetas)
        leer_receta(mi_receta)
        volver_inicio()

    elif menu == 2:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        crear_receta(mi_categoria)
        volver_inicio()

    elif menu == 3:
        crear_categoria(mi_ruta)
        volver_inicio()

    elif menu == 4:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        mi_receta = elegir_recetas(mis_recetas)
        eliminar_receta(mi_receta)
        volver_inicio()

    elif menu == 5:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        eliminar_categoria(mi_categoria)
        volver_inicio()

    elif menu == 6:
        finalizar_programa = True
