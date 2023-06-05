class Usuario:		
    def __init__(self, name):
        self.name = name
        self.balance_cuenta = 0
         # agregando el método de depósito
    def hacer_deposito(self, amount):
        self.balance_cuenta += amount
        print(f"el Usuario {self.name} ha depositado {amount}")
    # agregando el método de depósito
    def hacer_giro(self, amount):
        self.balance_cuenta -= amount	
        print(f"el Usuario {self.name} ha realizado un retiro por {amount}")

    def mostrar_balance_cuenta(self):
        print(f"el Usuario {self.name} Tiene un balance de  {self.balance_cuenta}")

    def transferir_dinero(self, destino, amount):
        self.balance_cuenta -= amount	
        destino.hacer_deposito(amount)
        print(f"el Usuario {self.name} transfirio {amount} a {destino.name}")
# instancias de Usuario
usuario1 = Usuario("Ana")
usuario2 = Usuario("Milena")
usuario3 = Usuario("Isabella")

# Hacer depósitos y giros para el primer usuario
usuario1.hacer_deposito(100)
usuario1.hacer_deposito(150)
usuario1.hacer_deposito(75)
usuario1.hacer_giro(100)
usuario1.mostrar_balance_cuenta()

usuario2.hacer_deposito(100)
usuario2.hacer_deposito(300)
usuario2.hacer_giro(50)
usuario2.hacer_giro(30)
usuario2.mostrar_balance_cuenta()

usuario3.hacer_deposito(900)
usuario3.hacer_giro(200)
usuario3.hacer_giro(50)
usuario3.hacer_giro(100)
usuario3.mostrar_balance_cuenta()

usuario1.transferir_dinero(usuario3,100)
usuario1.mostrar_balance_cuenta()
usuario3.mostrar_balance_cuenta()

# print("Balance: ", U.balance_cuenta) 
