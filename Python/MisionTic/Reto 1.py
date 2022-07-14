

# Ejercicio CRISTIAN
def CDT(usuario: str, capital: int, tiempo: int):
    if tiempo > 2:
        valor_intereses = round(((capital*0.03*tiempo)/12))
        return valor_intereses+capital
    else:
        valor_aperder = round(capital*0.02)
        valor_total = capital-valor_aperder
        return valor_total


usuario = input("digite su usuaurio :")
capital = int(input("digite su capital :"))
tiempo = int(input("digite su tiempo estimado en meses  :"))
respuesta = CDT(usuario, capital, tiempo)

print(f"Para el  usuario{usuario} La cantidad de dinero a recibir , segun el monto inicial de  {capital} COP para un tiempo de {tiempo} meses es de : {respuesta} COP")

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->
