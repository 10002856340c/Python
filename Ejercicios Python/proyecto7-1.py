

class Persona:

    def __init__(self, nombre, apellido) -> None:
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, balance=0) -> None:
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self) -> str:
        return f"El señor {self.nombre} {self.apellido}\n Con el numero de cuenta : {self.numero_cuenta}\n Balance cuenta : {self.balance}"

    def depositar(self, monto_depositar):
        self.balance += monto_depositar
        print("Monto depositado con exito")

    def retirar(self, monto_retirar):
        if monto_retirar <= self.balance:
            self.balance -= monto_retirar
            print("Monto retirado con exito")
        elif monto_retirar > self.balance:
            print("Saldo Insuficiente")


def crear_cliente():
    nombre = input("ingrese su nombre : ")
    apellido = input("ingrese su apellido : ")
    numero_cuenta = int(input("ingrese el numero de su cuenta Bancaria :"))
    mi_cliente = Cliente(nombre, apellido, numero_cuenta)
    return mi_cliente


def inicio():
    cliente = crear_cliente()
    print(cliente)
    opcion = 0
    while opcion != 'S':
        print("Elige una opcion :")
        print("""
        ['D'] - Depositar
        ['R'] - Retirar
        ['S'] - Salir
         """)
        opcion = input()
        if opcion == 'D':
            deposito = int(input("Ingrese el monto a Depositar :"))
            cliente.depositar(deposito)
        elif opcion == 'R':
            retiro = int(input("Ingrese el monto a Retirar :"))
            cliente.retirar(retiro)
        print(cliente)
    print("*"*50)
    print("GRACIAS POR HABER CONFIADO EN EL BANCO SMITH ")
    print("*"*50)


inicio()
