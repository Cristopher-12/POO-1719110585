class Cajero_Cash:
    #ATRIBUTOS
    billetes = "Billetes"
    papelticket = "Papel Ticket"
    camara = "Camara"
    funciones = "Funciones"
   
    #constructor
    def init(self):
        print("hola")

    #MÉTODOS
    def retiros(self):
        print("Retirar cantidad de cuenta bancaria")
    
    def depositos(self):
        print("Depositar dinero a cuenta bancaria")

class Cajero_Full(Cajero_Cash):
    #ATRIBUTOS
    botones = "Botones"
    pantalla = "Pantalla"
    monedas = "Monedas"
    Asistente = "Asistente"

    #Constructor
    def init(self):
        print("constructor herencia")
    
    #MÉTODOS
    def pagoservicios(self):
        print("Pago de servicios")

    
    
    def transferencias(self):
        print("Transferencias de dinero entre cuentas bancarias")

Cajero_ATM_BBVA = Cajero_Full()
print("#   METODOS   #")

Cajero_ATM_BBVA.retiros()
Cajero_ATM_BBVA.depositos()
Cajero_ATM_BBVA.pagoservicios()
Cajero_ATM_BBVA.transferencias()

print("#   ATRIBUTOS   #")

print(Cajero_ATM_BBVA.botones)
print(Cajero_ATM_BBVA.pantalla)
print(Cajero_ATM_BBVA.billetes)
print(Cajero_ATM_BBVA.papelticket)
print(Cajero_ATM_BBVA.camara)
print(Cajero_ATM_BBVA.monedas)
print(Cajero_ATM_BBVA.funciones)
print(Cajero_ATM_BBVA.Asistente)
