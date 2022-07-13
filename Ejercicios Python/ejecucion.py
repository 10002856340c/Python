import Proyecto10


def preguntar():
    print("Bienvenido al centro comercial  de Python ")
    while True:
        print("Acontinuacion encontrara las opciones diponibles :\n")

        print("""
        ['P'] - Perfumeria
        ['D'] - Drogueria
        ['M'] - Sala de Belleza
         """)

        try:
            opcion = input("Escoja una opcion : ").upper()
            ["P", "D", "M"].index(opcion)
        except ValueError:
            print("Elige una opcion correcta.")
        else:
            break
    Proyecto10.decorador(opcion)


def inicio():
    while True:
        preguntar()
        try:
            otro_turno = input("Quieres sacar otro turno [SI]-[NO] ").upper()
            ["SI", "NO"].index(otro_turno)
        except ValueError:
            print("Elige una opcion correcta.")
        else:
            if otro_turno == "NO":
                print("Gracias por su visita ")
                break


inicio()
