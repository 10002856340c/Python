import itertools


def generador_perfumeria():
    for i in itertools.count(1):
        yield f"Perfumeria-Turno-{i}"


def generador_Farmacia():
    for x in itertools.count(1):
        yield f"Farmacia-Turno{x}"


def generador_maquillaje():
    for z in itertools.count(1):
        yield f"Salon de Belleza-Turno-{z}"


perfumeria = generador_perfumeria()
drogueria = generador_Farmacia()
maquillaje = generador_maquillaje()


def decorador(opcion):

    print("*"*50)
    if opcion == "P":
        print(next(perfumeria))
    elif opcion == "F":
        print(next(drogueria))
    elif opcion == "M":
        print(next(maquillaje))
