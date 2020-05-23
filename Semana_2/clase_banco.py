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
    numero_de_escritorios = ""
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
print("#   METODOS   #")

banamex.hacer_depositos()
banamex.hacer_retiros()
banamex.emitir_creditos()
banamex.brindar_productos_financieros()
banamex.canalizar_ahorros()

print("#   ATRIBUTOS   #")

banamex.dinero = 1000000000
banamex.personal = "Cajeros, Gerentes, Auxiliar"
banamex.ventanillas = "12 Ventanillas"
banamex.sala_de_espera = 2
banamex.boveda = 1
banamex.clave_de_acceso = "Clave personal por cada empleado"
banamex.vigilantes = "GSI seguridad privada"
banamex.numero_de_camaras = 26
banamex.alarma_de_seguridad = "Alarma de seguridad integrada"
banamex.numero_de_escritorios = 10

print(banamex.dinero)
print(banamex.personal)
print(banamex.ventanillas)
print(banamex.sala_de_espera)
print(banamex.boveda)
print(banamex.clave_de_acceso)
print(banamex.vigilantes)
print(banamex.numero_de_camaras)
print(banamex.alarma_de_seguridad)
print(banamex.numero_de_escritorios)
