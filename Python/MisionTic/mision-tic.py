
# TIPOS DE VARIABLES

# PRIMER EJEMPLO

# a = input("digite un texto")

# print(f"el texto digitado es : {a}")

# print(type(a))

#b = 16
#print("el tipo de texto es ")
# print(type(b))

# c = 17.5
# print("el tipo de texto es :")
# print(type(c))
# ---------------------------------------------------------------------------->

# SEGUNDO EJEMPLO( EL MAYOR DE CUATROS NUMEROS)

print("hola digita dos numeros")

a = int(input("digita el primer numero :"))
b = int(input("digita el segundo numero :"))
c = int(input("digita el tecer numero:"))
d = int(input("ingrese el cuarto numero :"))


print(type(a))
print(type(b))
print(type(c))
print(type(d))


if(a > b) and (a > c) and (a > d):
    print(f"el numero mayor es : {a}")

elif(b > a) and (b > c) and (b > d):
    print(f"el numero mayor es : {b}")

elif(c > a) and (c > b) and (c > d):
    print(f"el numero mayor es : {c}")

elif(d > a) and (d > b) and (d > c):
    print(f"el numero mayor es : {d}")
