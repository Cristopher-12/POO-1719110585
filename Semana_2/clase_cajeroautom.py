class CajeroATM:
 #ATRIBUTOS
    botones = ""
    pantalla = ""
    dinero = ""
    papelticket = ""
    camara = ""

   
    #MÉTODOS
    def retiros(self):
        print("Retirar cantidad de cuenta bancaria")
    
    def depositos(self):
        print("Depositar dinero a cuenta bancaria")
    
    def pagoservicios(self):
        print("Pago de servicios")

    def consultasaldo(self):
        print("Consultar saldo de cuenta bancaria")
    
    def transferencias(self):
        print("Transferencias de dinero entre cuentas bancarias")

Cajero_ATM_BBVA = CajeroATM()
print("#   METODOS   #")

Cajero_ATM_BBVA.retiros()
Cajero_ATM_BBVA.depositos()
Cajero_ATM_BBVA.pagoservicios()
Cajero_ATM_BBVA.consultasaldo()
Cajero_ATM_BBVA.transferencias()

print("#   ATRIBUTOS   #")

Cajero_ATM_BBVA.botones = "20 botones"
Cajero_ATM_BBVA.pantalla = "Pantalla LCD tactil 17 pulgadas"
Cajero_ATM_BBVA.dinero = "Efectivo y monedas"
Cajero_ATM_BBVA.papelticket = "Papel ticket a la mitad de su capacidad"
Cajero_ATM_BBVA.camara = "2 megapixeles para capturar rostro"

print(Cajero_ATM_BBVA.botones)
print(Cajero_ATM_BBVA.pantalla)
print(Cajero_ATM_BBVA.dinero)
print(Cajero_ATM_BBVA.papelticket)
print(Cajero_ATM_BBVA.camara)
