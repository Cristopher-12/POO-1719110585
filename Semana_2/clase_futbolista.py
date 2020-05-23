class Futbolista:
    #ATRIBUTOS
    condicion_fisica = ""
    genero = ""
    dieta = ""
    altura = ""
    peso = ""
    posicion = ""
    Numero = ""
    uniforme = ""
    Apodo = ""
    velocidad = "" 
   #MÉTODOS
    def correr(self):
        print("Correr tras el balon")
    
    def brincar(self):
        print("Brincar para atrapar el balon ")
    
    def gritar(self):
        print("Gritar para dar indicaciones a largas distancias")

    def patear(self):
        print("Patear el balon")
    
    def festejar (self):
        print("Festejar al meter un gol")

Kylian_Mbappé = Futbolista()
print("#   METODOS   #")
Kylian_Mbappé.correr()
Kylian_Mbappé.patear()

print("#   ATRIBUTOS   #")
Kylian_Mbappé.condicion_fisica = "Excelente condicion"
Kylian_Mbappé.genero = "Masculino"
Kylian_Mbappé.dieta = "Dieta estricta alta en proteínas" 
Kylian_Mbappé.altura = "Mide: 1.78 m"
Kylian_Mbappé.peso = "Pesa: 73 kg"
Kylian_Mbappé.posicion = "Delantero"
Kylian_Mbappé.Numero = "Numero 7"
Kylian_Mbappé.uniforme = "Uniforme desfajado"
Kylian_Mbappé.Apodo = "Ningun apodo"
Kylian_Mbappé.velocidad = "38 km/h"

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