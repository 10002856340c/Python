from functools import reduce


rutinaContable = [
    [6589, ("9874", 1, 125698.20), ("88112", 2,
                                    135645.20), ("3218", 4, 13645.20)],
    [6590, ("5236", 8, 11.99), ("7733", 11, 18.99), ("88112", 5, 390.95)],
    [6591, ("7812", 2, 11.99), ("9652", 11, 18.99)], ]


def ordenes(rutinaContable):
    print('----------------- Inicio Registro diario --------------------------')

    for i in rutinaContable:
        multiplicacion = (list(map(lambda x: x[1]*x[2], i[1:])))
        suma = (reduce(lambda x, y: x+y, multiplicacion[0:]))
        if suma < 600000:
            suma += 25000
        else:
            pass
        print(
            f"La factura {i[0]} tiene un total en pesos de {suma:,.2f}")

    print('--------------------Fin Registro diario -----------------------------')


ordenes(rutinaContable)
