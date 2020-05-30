class Basketbolista:
    #ATRIBUTOS
    posicion = "Posicion"
    Numero = "Numero"
    uniforme = "Uniforme"
    Apodo = "Apodo"
    velocidad = "Velocidad"

  #constructor
    def init(self):
        print("hola")

    #MÉTODOS
    def correr(self):
        print("Correr tras el balon")
    
    def brincar(self):
        print("Brincar para atrapar el balon ")

class Futbolista(Basketbolista):
    #ATRIBUTOS
    condicion_fisica = "Condicion Fisica"
    genero = "Genero"
    dieta = "Dieta"
    altura = "Altura"
    peso = "Peso"
    
    #Constructor
    def init(self):
        print("constructor herencia")
   
    #MÉTODOS
    def patear(self):
        print("Patear el balon")
    
    def festejar (self):
        print("Festejar al meter un gol")

Kylian_Mbappé = Futbolista()
print("#   METODOS   #")
Kylian_Mbappé.correr()
Kylian_Mbappé.patear()
Kylian_Mbappé.festejar()
Kylian_Mbappé.brincar()

print("#   ATRIBUTOS   #")

print(Kylian_Mbappé.condicion_fisica)
print(Kylian_Mbappé.genero)
print(Kylian_Mbappé.dieta)
print(Kylian_Mbappé.altura)
print(Kylian_Mbappé.peso)
print(Kylian_Mbappé.posicion)
print(Kylian_Mbappé.Numero)
print(Kylian_Mbappé.uniforme)
print(Kylian_Mbappé.Apodo)
print(Kylian_Mbappé.velocidad)