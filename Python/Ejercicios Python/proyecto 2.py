# from tkinter import Y

# x = 6
# y = 2
# z = 7

#print(f"{x}+{y} es igual a : {x+y}")
#print(f"{x}-{y} es igual a : {x-y}")
#print(f"{x}*{y} es igual a : {x*y}")
#print(f"{x}/{y} es igual a : {x/y}")


#print(f"{z} dividido al piso de {y}es igual a {z//y}")
#print(f"el modulo ente {z} y {y} es {z%y}")
#print(f"{x} elevado a la {y} es {x**y}")
#print(f"{x} elevado a la {5} es {x**5}")
# print(f"la raiz cuadrada de {x} es {x**0.5}"

#print(f"{874} dividido al piso de {27}es igual a {874//27}")


# CALCULADORA DE COMISIONES

nombre = (input("Ingresa tu nombre :"))
apellido = (input("Ingresa tu apellido :"))
ventas = (input("Ingresa el numero de ventas que realizaste :"))
comisiones = int(ventas)*13/100
comisiones = round(comisiones)
print(f"Hola {nombre}  {apellido} , el numero de ventas totales que hiciste en este mes fueron de {ventas} ventas . Felicitaciones , por lo tanto tus comisiones fueron de {comisiones} $ dolares ")
