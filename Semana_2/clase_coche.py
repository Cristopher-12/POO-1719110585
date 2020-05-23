class Coche:
    #ATRIBUTOS
    motor = ""
    color = ""
    numeropuertas = ""
    velocidades = ""
    frenos = ""
    faros = ""
    asientos = ""
    cinturones = ""
    volante = ""
    espejos = ""

   
    #MÉTODOS
    def viajar(self):
        print("viajar a otros lugares")
    
    def encender(self):
        print("Enciende correctamente el motor")
    
    def transportar(self):
        print("Transorta objetos de un lugar a otro")

    def apagar(self):
        print("Apaga correctamente el motor")
    
    def acelerar (self):
        print("Acelerar al pisar el acelerador")

Rolls_Royce = Coche()
print("#   METODOS   #")

Rolls_Royce.viajar()
Rolls_Royce.encender()
Rolls_Royce.transportar()
Rolls_Royce.encender()
Rolls_Royce.acelerar()


print("#   ATRIBUTOS   #")

Rolls_Royce.motor = "Motor V12."
Rolls_Royce.color = "Color Negro"
Rolls_Royce.numeropuertas = "5"
Rolls_Royce.velocidades = "5 velocidades"
Rolls_Royce.frenos = "Discos de freno"
Rolls_Royce.faros = "Faros de Xenon"
Rolls_Royce.asientos = "Asientos comodos"
Rolls_Royce.cinturones = "4 cinturones de seguridad"
Rolls_Royce.volante = "Volante lujoso"
Rolls_Royce.espejos = "Espejos antireflejo"

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