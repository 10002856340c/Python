
# RETO 2  CRISTIAN

def cliente(informacion: dict):
    if informacion['edad'] > 18:
        atraccion = 'X-Treme'
        apto = True
        if informacion['primer_ingreso'] == True:
            valorBoleta = 19000.0
        else:
            valorBoleta = 20000

    elif informacion['edad'] >= 15 and informacion['edad'] <= 18:
        atraccion = 'Carros chocones'
        apto = True
        if informacion['primer_ingreso'] == True:
            valorBoleta = 4650.0
        else:
            valorBoleta = 5000

    elif informacion['edad'] >= 7 and informacion['edad'] < 15:
        atraccion = "Sillas voladoras"
        apto = True
        if informacion['primer_ingreso'] == True:
            valorBoleta = 9500.0
        else:
            valorBoleta = 10000
    else:
        atraccion = informacion['atraccion'] = 'N/A'
        apto = informacion['apto'] = False
        valorBoleta = informacion['total_boleta'] = 'N/A'
        informacion['primer_ingreso'] = False

    resultado = {'nombre': informacion['nombre'], 'edad': informacion['edad'], 'atraccion': atraccion,
                 'apto': apto, 'primer_ingreso': informacion['primer_ingreso'], 'total_boleta': valorBoleta}
    return resultado


# informacion asignada
informacion = {}

informacion['id_cliente'] = int(input("digite su id : "))
informacion['nombre'] = input("Digite su nombre : ")
informacion['edad'] = int(input("Digite su edad : "))
informacion['primer_ingreso'] = bool(input("primer ingreso ? :"))
print(cliente(informacion))


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->
