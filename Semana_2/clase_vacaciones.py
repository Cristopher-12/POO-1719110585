class Vacaciones:
    #ATRIBUTOS
    Entretenimiento = ""
    Diversion = ""
    Conocimiento = ""
    Distraccion = ""
    Comodidad = ""
    #MÉTODOS
    def desestresar(self):
        print("Desestresar")
    
    def gastar(self):
        print("Gastar dinero")
    
    def convivir(self):
        print("Convivir con personas o familiares")

    def descansar(self):
        print("No hacemos lo que hacemos cotidianamente")
    
    def conocer(self):
        print("Conocemos el lugar al que viajemos")

visitar_un_familiar = Vacaciones()
print("#   Metodos  #")

visitar_un_familiar.desestresar()
visitar_un_familiar.gastar()
visitar_un_familiar.convivir()
visitar_un_familiar.descansar()
visitar_un_familiar.conocer()

print("#   ATRIBUTOS   #")

visitar_un_familiar.Entretenimiento = "Nos divertimos"
visitar_un_familiar.Diversion = "Convivimos"
visitar_un_familiar.Conocimiento = ""
visitar_un_familiar.Distraccion = ""
visitar_un_familiar.Comodidad = ""

print(visitar_un_familiar.Entretenimiento)
print(visitar_un_familiar.Diversion)
print(visitar_un_familiar.Conocimiento)
print(visitar_un_familiar.Distraccion)
print(visitar_un_familiar.Comodidad)