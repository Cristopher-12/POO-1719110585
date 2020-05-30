class coche_deportivo:
#ATRIBUTOS
    faros = "Faros"
    asientos = "Asientos"
    cinturones = "Cinturones"
    volante = "Volante"
    espejos = "Espejos"

#constructor
    def init(self):
        print("hola")

#MÉTODOS
    def viajar(self):
        print("viajar a otros lugares")
    
    def encender(self):
        print("Enciende correctamente el motor")

class Coche_elegante(coche_deportivo):
    #ATRIBUTOS
    motor = "Motor"
    color = "Color"
    numeropuertas = "Numero de puertas"
    velocidades = "Velocidades"
    frenos = "Frenos"
   
    #Constructor
    def init(self):
        print("constructor herencia")
    
   
    #MÉTODOS
    def transportar(self):
        print("Transorta objetos de un lugar a otro")

    def apagar(self):
        print("Apaga correctamente el motor")
    

Rolls_Royce = Coche_elegante()
print("#   METODOS   #")

Rolls_Royce.viajar()
Rolls_Royce.encender()
Rolls_Royce.transportar()
Rolls_Royce.apagar()

print("#   ATRIBUTOS   #")

print(Rolls_Royce.motor)
print(Rolls_Royce.color)
print(Rolls_Royce.numeropuertas)
print(Rolls_Royce.velocidades)
print(Rolls_Royce.frenos)
print(Rolls_Royce.faros)
print(Rolls_Royce.asientos)
print(Rolls_Royce.cinturones)
print(Rolls_Royce.volante)
print(Rolls_Royce.espejos)
