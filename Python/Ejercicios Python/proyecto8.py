# package que se llama colored lo descargago a travez de la terminal , y asi seria la forma para ejecutarlo y cambiar el color de texto en la terminal

"""from colored import fg, bg, attr

color = fg(10) + bg(10)
print(color + "Hola mundo"+attr(0))
"""
# package se llama openpyxl este packge sirve para manajeja excel atravez de python

"""******************************************************************MANEJO DE ERRORES ***********************************************************************************************"""

# try
# except
# finally

# 1) Ejemplo , poniendo a prueba diversos errores
# en es ta URL https://docs.python.org/es/3/library/exceptions.html podemos encontrar los diferentes errores comunes que tenemos al compilar nuestro codigo
# uno de los mas comunes que estan presentes en este codigo son TypeError y ValueError
# para eso crearemos codigo atravez de try  y except por si llegara a pasar ese error


"""def suma():
    n1 = int(input("numero 1 :"))
    n2 = int(input("numero 1 :"))
    print(n1+n2)
    print("gracias por sumar ")


# TypeError--> cuando los tipos de las variables no coincide con lo que se quiere ejecutar
# valueError --> cuando la informacion ingresada por teclado no coinciden

try:
    suma()
except TypeError:
    print("Estas intentando concatenar tipos distintos")
except ValueError:
    print("son mensajes distintos")
else:
    print("hiciste todo bien")
finally:
    print("eso fue todo")"""

# 2) Ejemplo


"""def pedir_numero():
    while True:
        try:
            numero = int(input("numero 1 :"))
        except:
            print("ese no es un numero")
        else:
            print(f"ingresaste el numero {numero}")
            break
    print("gracias")


pedir_numero()"""

# 3 Ejemplo
"""def suma(num1, num2):
    try:
        print(num1+num2)
    except:
        print("Error inesperado")


suma("1", 5)"""
# 4 Ejemplo
# Para este ejemplo vamos a utilizar un error llamado zero ZeroDivisionError
# ZeroDivisionError--> Se genera cuando el segundo argumento de una operación de división o módulo es cero. El valor asociado es una cadena que indica el tipo de operandos y la operación.

"""
def cociente(num1, num2):
    try:
        print(num1/num2)
    except TypeError:
        print("Los argumentos a ingresar deben ser números")
    except ZeroDivisionError:
        print("El segundo argumento no debe ser cero")


cociente(10, "")
"""
# 5 Ejemplo
# Para este ejemplo vamos a utilizar un error llamado FileNotFoundError
# FileNotFoundError --> es cuando no se encuetra nignun archivo o carpeta dentro del sistema que esta indicando


"""def abrir_archivo(nombre_archivo):

    try:
        archivo = open(nombre_archivo)
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    except:
        print("Error desconocido")
    else:
        print("abierto exitosamente")
    finally:
        print("Finalizando ejecución")


abrir_archivo("hola")
"""

"""

Este es un modulo que imprime algo 
"""
# para hacer un analizis de nuestro codigo mas detallado utilizamos la libreria pylint, y se ejecuta en la terminal de la siguiente manera "pylint "nombre.py" -r y

# El puntaje que de al final tratar de que sea mayor de 7, para tener un buen desempeño en el codigo
