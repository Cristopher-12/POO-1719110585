class Vacaciones:
    #ATRIBUTOS
    Entretenimiento = "Entretenimiento"
    Diversion = "Diversion"
    Conocimiento = "Conocimiento"
    Ofertas = "Ofertas"
    #Constructor
    def init(self):
        print("Hola")
    
    #MÉTODOS
    def desestresar(self):
        print("Desestresar")
    
    def gastar(self):
        print("Gastar dinero")
class Vacaciones_Playa(Vacaciones):
#Atributos
    Distraccion = "Distraccion"
    Comodidad = "Comodidad"
    Recuerdos = "Recuerdos"

#Constructor
    def init(self):
        print("constructor herencia")

#Métodos

    def convivir(self):
        print("Convivir con personas o familiares")

    def descansar(self):
        print("No hacemos lo que hacemos cotidianamente")
    
    
visitar_un_familiar = Vacaciones_Playa()
print("#   Metodos  #")

visitar_un_familiar.desestresar()
visitar_un_familiar.gastar()
visitar_un_familiar.convivir()
visitar_un_familiar.descansar()

print("#   ATRIBUTOS   #")

print(visitar_un_familiar.Entretenimiento)
print(visitar_un_familiar.Diversion)
print(visitar_un_familiar.Conocimiento)
print(visitar_un_familiar.Ofertas)
print(visitar_un_familiar.Distraccion)
print(visitar_un_familiar.Comodidad)
print(visitar_un_familiar.Recuerdos)
