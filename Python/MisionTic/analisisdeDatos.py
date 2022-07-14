
import matplotlib.pyplot as plt
import pandas as pd
"""************************************GAFICA CON DOS LINEAS O DOS GRUPOS DE INFORMACION******************"""
# primero vamos a crear una grafica de barras de un vector
# en esta grafica de barras va a ver informacion respecto al tiempo de demora para solucionar los retos del 1 al 5

"""
# 1 ) CREAR LAS LISTAS

profesiones1 = ['ing sistemas', 'ing electronico',
                'ing industrial', 'ing ambiental', 'ing mecatronicos']
salarios = [3000000, 2500000, 1500000, 1360000, 1400000]

profesiones2 = ['psiocologos', 'medicos',
                'enfermeros', 'cajeros', 'electricistas']
salarios2 = [1200000, 3800000, 1500000, 1150000, 1500000]

# 2 LE ASIGNAMOS DE QUE COLOR VAN A HACER LAS BARRAS , EL GROSOR , Y ALGUNAS VARIABLES
plt.bar(profesiones1, salarios, color='green',
        linewidth=3, label="sueldo")
plt.bar(profesiones2, salarios2, color='blue',
        linewidth=3, label="sueldo")

# 3 LE ASIGNAMOS EL TITULO DE LA GRAFICA
plt.title("sueldo segun profesiones")

# 4 LE ASIGNAMOS EL NOMBRE AL EJE X
plt.xlabel("profesiones")

# 5 LE ASIGNAMOS EL NOMBRE AL EJE Y
plt.ylabel("sueldo")

# 6 ASIGNAMOS PROPIEDADES PARA QUE SE EJECUTE EL PROGRAMA
plt.legend()
plt.grid()
plt.show()"""


"""**************************************SEGUNDO EJEMPLO CON UN CSV************************************************************"""
datosTitanic = pd.read_csv(r"D:\\usuario\\Documents\\python\\titanic3.csv")
print(datosTitanic)

vivos = datosTitanic.survived.value_counts()
print(vivos)

muertosx = [0]
cantidadmuertos = [vivos[0]]
sobrevivientesy = [1]
cantidadvivos = [vivos[1]]

plt.bar(muertosx, cantidadmuertos, color='green',
        width=0.2, label="muertos")
plt.bar(sobrevivientesy, cantidadvivos, color='blue',
        width=0.2, label="vivos")

# 3 LE ASIGNAMOS EL TITULO DE LA GRAFICA
plt.title("SOBREVIEVIENTES DEL TITANIC")

# 4 LE ASIGNAMOS EL NOMBRE AL EJE X
plt.xlabel("personas")

# 5 LE ASIGNAMOS EL NOMBRE AL EJE Y
plt.ylabel("cantidad")

# 6 ASIGNAMOS PROPIEDADES PARA QUE SE EJECUTE EL PROGRAMA
plt.legend()
plt.grid()
plt.show()
