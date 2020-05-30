class Banco_Azteca:
    #ATRIBUTOS
    dinero = "Dinero"
    personal =  "Personal"
    ventanillas = "Ventanillas"
    sala_de_espera = "Sala de espera"
    boveda = "Boveda"
    
    #MÉTODOS
    def hacer_depositos(self):
        print("Hacer depositos")
    
    def hacer_retiros(self):
        print("Hacer retiros")


class BBVA(Banco_Azteca):
    #ATRIBUTOS
    clave_de_acceso = "Clave de acceso"
    vigilantes = "Vigilantes"
    numero_de_camaras = "Numero de camaras"
    alarma_de_seguridad = "Alarma de seguridad"
    numero_de_escritorios = "Numero de escritorios"

    #constructor
    def init(self):
        print("hola")

    #MÉTODOS
    def emitir_creditos(self):
        print("Emitir creditos")
    
    def canalizar_ahorros(self):
        print("Canalizar Ahorros")

banamex = BBVA()
print("#   METODOS   #")

banamex.hacer_depositos()
banamex.hacer_retiros()
banamex.emitir_creditos()
banamex.canalizar_ahorros()

print("#   ATRIBUTOS   #")

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