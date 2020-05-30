class Avion_Pasajeros:
    #ATRIBUTOS
    alas = "Alas"
    tren_de_aterrizaje = "Tren de aterrizaje"
    turbinas = "Turbinas"
    ventanillas = "Ventanillas"
    cabina = "Cabina"
 
    #constructor
    def init(self):
        print("hola")
        
    def despegar():
        print("despegar")
            
    
    #MÉTODOS
    def viajar(self):
        print("Viajar")
    
    def volar(self):
        print("Volar")

class Avion_de_carga(Avion_Pasajeros):
   #Atributos
    cola = "Cola"
    timones = "Timones"
    alerones = "Alerones"
    estabilizadores = "Estabilizadores"
    spoilers = "Spoilers"
    
    #Constructor
    def init(self):
        print("constructor herencia")
    

    #MÉTODOS
    def encender(self):
        print("Encencer")

    def apagar(self):
        print("Apagar")

Avion_DHL = Avion_de_carga()
print("#   METODOS   #")
Avion_DHL.viajar()
Avion_DHL.volar()
Avion_DHL.encender()
Avion_DHL.apagar()

print("#   Atributos   #")
print(Avion_DHL.alas)
print(Avion_DHL.tren_de_aterrizaje)
print(Avion_DHL.turbinas)
print(Avion_DHL.ventanillas)
print(Avion_DHL.cabina)
print(Avion_DHL.cola)
print(Avion_DHL.timones)
print(Avion_DHL.alerones)
print(Avion_DHL.estabilizadores)
print(Avion_DHL.spoilers)