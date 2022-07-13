# Programa para que calucule el precio de un producto con iva
producto = int(input("Digite el precio del producto : "))
cantidad = int(input("cuantas cantidades del producto desea llevar  :"))


def precioconIVA(producto, cantidad):
    multiplicacion = producto*cantidad
    Iva = multiplicacion*0.19
    total = Iva+multiplicacion
    print(
        f"El precio digitado es :{producto}\n La cantidad digitada es : {cantidad}\n Precio total sin IVA es de.. : {multiplicacion}\n"+"*"*50)

    return print(f"precio TOTAL incluido el IVA es de : {total}")


precioconIVA(producto, cantidad)


# -------------------------------------------------------------------------------------------------------------------------------
