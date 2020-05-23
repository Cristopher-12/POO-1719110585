class Banco:
    #ATRIBUTOS
    dinero = ""
    personal =  ""
    ventanillas = ""
    sala_de_espera = ""
    boveda = ""
    clave_de_acceso = ""
    vigilantes = ""
    numero_de_camaras = ""
    alarma_de_seguridad = ""
    escritorios = ""

    #MÉTODOS
    def hacer_depositos(self):
        print("Hacer depositos")
    
    def hacer_retiros(self):
        print("Hacer retiros")
    
    def emitir_creditos(self):
        print("Emitir creditos")

    def brindar_productos_financieros(self):
        print("Brindar productos financieros")
    
    def canalizar_ahorros(self):
        print("Canalizar Ahorros")

banamex = Banco()

banamex.clave_de_acceso = 123
banamex.numero_de_camaras = 10

print(banamex.clave_de_acceso)
print(banamex.numero_de_camaras)

banamex.hacer_depositos()
banamex.emitir_creditos()