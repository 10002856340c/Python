# RETO 3

# lista = {'clave1': [(1, 2)],'clave2':{'clave3':2}}
# print(lista['clave2']['clave3'])


def AutoPartes(ventas: list):
    dic = {}
    for i in range(len(ventas)):
        dic[i] = [ventas[i]]
    return dic


def consultaRegistro(ventas, id_producto):
    dic = {}
    for i in ventas:
        if id_producto == ventas[i][0][0]:
            dic[i] = ventas[i]
    concatenar = ' '
    if len(dic) == 0:
        return(print("este producto no existe"))

    else:
        for i in dic:
            concatenar += f"Producto consultado :{ventas[i][0][0]} Descripción {ventas[i][0][1]} #Parte {ventas[i][0][2]} Cantidad vendida {ventas[i][0][3]} Stock {ventas [i][0][4]}Comprador {ventas[i][0][5]} Documento {ventas[i][0][6]} Fecha Venta {ventas[i][0][7]}\n\n"
    return print(concatenar)


print(consultaRegistro(AutoPartes([
    (2001, 'rosca', 'PT29872', 2, 45, 'Luis Molero', 3456, '12/06/2020'),
    (2010, 'bujía', 'MS9512', 4, 15, 'Carlos Rondon', 1256, '12/06/2020'),
    (2010, 'bujía', 'ER6523', 9, 36, 'Pedro Montes', 1243, '12/06/2020'),
    (3578, 'tijera', 'QW8523', 1, 128, 'Pedro Faria', 1456, '12/06/2020'),
    (9251, 'piñón', 'EN5698', 2, 8, 'Juan Peña', 565, '12/06/2020')]), 2010))
