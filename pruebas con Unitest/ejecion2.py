
import pruebas


def preguntar_usuario():
    print("Bienvenido al Centro  Comercial de python :"+"\n")
    while True:

        print("A continuacion los lugares Abiertos  :" + "\n")
        print("""
            ['P'] - Papelerias
            ['L'] - Lavanderia
            ['C'] - Cigarreria
            """)
        try:
            usuario = input("Escoja una opcion :").upper()
            ["P", "L", "C"].index(usuario)
        except ValueError:
            print("Escoja una opcion Correcta ...")
        else:
            break
    pruebas.operador(usuario)


def inicio():

    while True:
        preguntar_usuario()
        try:
            usuarios = input("Desea escoger otra Opcion [SI]-[NO] :").upper()
            ["SI", "NO"].index(usuarios)
        except ValueError:
            print("Escoja una opcion corecta ...")
        else:
            if usuarios == "NO":
                print("Gracias por haber venido")
                break


inicio()
