

"""usuario = int(input("ingrese un numero :"))

if usuario == 1:
    print("Enero")
elif usuario == 2:
    print("Febrero")
elif usuario == 3:
    print("Marzo")
elif usuario == 4:
    print("Abril")
elif usuario == 5:
    print("Mayo")
elif usuario == 6:
    print("Junio")
elif usuario == 7:
    print("Julio")
elif usuario == 8:
    print("Agosto")
elif usuario == 9:
    print("Septiembre")
elif usuario == 10:
    print("Octubre")
elif usuario == 11:
    print("Noviembre")
elif usuario == 12:
    print("Diciembre")"""


"""usuario = int(input("Ingrese los segundos  que quiere convertir :"))
EquivalenciaSegundos_horas = round(usuario/3600)
usuario %= 3600
EquivalenciaSegundos_minutos = round(usuario/60)
Equivalenciasegundos_segundos = round(usuario % 60)


print(f"{usuario} segundos equivale a {EquivalenciaSegundos_horas} horas {EquivalenciaSegundos_minutos} minutos {Equivalenciasegundos_segundos} segundos ")"""

"""lista = ([
    (2001, 'rosca', 'PT29872', 2, 45, 'Luis Molero', 3456, '12/06/2020'),
    (2010, 'bujía', 'MS9512', 4, 15, 'Carlos Rondon', 1256, '12/06/2020'),
    (2010, 'bujía', 'ER6523', 9, 36, 'Pedro Montes', 1243, '12/06/2020'),
    (3578, 'tijera', 'QW8523', 1, 128, 'Pedro Faria', 1456, '12/06/2020'),
    (9251, 'piñón', 'EN5698', 2, 8, 'Juan Peña', 565, '12/06/2020')])


def AutoPartes(ventas):
    dic = {}
    for i in range(len(ventas)):
        dic[i] = [ventas[i]]
    return dic


def consultaRegistro(ventas, idProducto):
    dic2 = {}
    for i in ventas:
        if idProducto == ventas[i][0][0]:
            dic2[i] = ventas[i]
    concatenar = "  "
    if len(dic2) == 0:
        return print("No hay registro de venta de ese producto")
    else:
        for i in dic2:
            concatenar += f"\nProducto consultado :  {ventas[i][0][0]}  Descripción  {ventas[i][0][1]}  #Parte  {ventas[i][0][2]} Cantidad vendida  {ventas[i][0][3]}  Stock   {ventas[i][0][4]} Comprador {ventas[i][0][5]}  Documento  {ventas[i][0][6]} Fecha Venta  {ventas[i][0][7]}\n"
        return print(concatenar)


print(consultaRegistro(AutoPartes([
    (9852, 'Culata', 'XC9875', 2, 165, 'Luis Molero', 3455846, '14/06/2020'),
    (9852, 'Culata', 'XC9875', 2, 165, 'Jose Mejia', 1355846, '14/06/2020'),
    (2564, 'Cárter', 'PT29872', 2, 32, 'Peter Cerezo', 8545436, '14/06/2020'),
    (5412, 'válvula', 'AZ8798', 2, 11, 'Juan Peña', 568975, '14/06/2020')]), 9852))"""

"""lista = [2000, ('10', 5, 12)]
for elemento in lista:
    print(type(elemento))
    if type(elemento) is tuple:
        for el in elemento:
            print(type(el))"""
