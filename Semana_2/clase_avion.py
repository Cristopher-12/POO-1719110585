class Avion:
    #ATRIBUTOS
    alas = ""
    tren_de_aterrizaje = ""
    turbinas = ""
    ventanillas = ""
    cabina = ""
    cola = ""
    timones = ""
    alerones = ""
    estabilizadores = ""
    spoilers = ""


    #MÉTODOS
    def viajar(self):
        print("Viajar")
    
    def transportar(self):
        print("Transportar objetos")
    
    def volar(self):
        print("Volar")

    def encender(self):
        print("Encencer el motor")
    
    def apagar(self):
        print("Apagar el motor")
avion_de_pasajeros = Avion()
print("#   MÉTODOS   #")
avion_de_pasajeros.viajar()
avion_de_pasajeros.transportar()
avion_de_pasajeros.volar()
avion_de_pasajeros.encender()
avion_de_pasajeros.apagar()

print("#   ATRIBUTOS   #")
avion_de_pasajeros.alas = "2 alas"
avion_de_pasajeros.tren_de_aterrizaje = "El trende aterrizaje esta en correcto funcionamiento"
avion_de_pasajeros.turbinas = "4 turbinas"
avion_de_pasajeros.ventanillas = "Ventanillas para ver el exterior "
avion_de_pasajeros.cabina = "Cabina de mando del avion"
avion_de_pasajeros.cola = "Parte aerodinamica del avion"
avion_de_pasajeros.timones = "Parte aerodinamica 1"
avion_de_pasajeros.alerones = "Parte aerodinamica 2"
avion_de_pasajeros.estabilizadores = "Parte aerodinamica 3"
avion_de_pasajeros.spoilers = "Parte aerodinamica 4"


print(avion_de_pasajeros.alas)
print(avion_de_pasajeros.tren_de_aterrizaje)
print(avion_de_pasajeros.turbinas)
print(avion_de_pasajeros.ventanillas)
print(avion_de_pasajeros.cabina)
print(avion_de_pasajeros.cola)
print(avion_de_pasajeros.timones)
print(avion_de_pasajeros.alerones)
print(avion_de_pasajeros.estabilizadores)
print(avion_de_pasajeros.spoilers)