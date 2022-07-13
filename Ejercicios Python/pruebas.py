import itertools

# creamos las funciones


def Turnos_Papeleria():
    for x in itertools.count(1):
        yield f"Papeleria-Turno-{x}"


def Turnos_Lavanderia():
    for z in itertools.count(1):
        yield f"Lavanderia-Turno-{z}"


def Turnos_Cigarreria():
    for y in itertools.count(1):
        yield f"Cigarreria-Turno-{y}"


Papeleria = Turnos_Papeleria()
Lavanderia = Turnos_Lavanderia()
Cigarreria = Turnos_Cigarreria()


def operador(opcion):
    if opcion == "P":
        print(next(Papeleria))
    elif opcion == "L":
        print(next(Lavanderia))
    elif opcion == "C":
        print(next(Cigarreria))
