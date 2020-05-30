class SerieTV:
    #ATRIBUTOS
    entretenimiento = "Entretenimiento"
    genero = "Genero"
    trama = "Trama"
    reparto = "Reparto"
    guion = "Guion"

    #constructor
    def init(self):
        print("hola")
    
    #MÉTODOS
    def entretener(self):
        print("Entretener")
    
    def grabar(self):
        print("Grabar las escenas")
    
class SerieTV_Accion(SerieTV):

    #ATRIBUTOS
    capitulos = "Capitulos"
    duracion = "Duración"
    personajes ="Personajes"
    inicio = "Inicio"
    final = "Final"
    
    #Constructor
    def init(self):
        print("constructor herencia")
    
    #MÉTODOS
    def actuar(self):
        print("Perfecta actuación")

    def causar_emociones(self):
        print("Espantar, entristecer, enojar")
    

serieterror = SerieTV_Accion()
print("#   METODOS   #")
serieterror.entretener()
serieterror.grabar()
serieterror.actuar()
serieterror.causar_emociones()


print("#   ATRIBUTOS   #")

print(serieterror.entretenimiento)
print(serieterror.genero)
print(serieterror.trama)
print(serieterror.reparto)
print(serieterror.guion)
print(serieterror.capitulos)
print(serieterror.duracion)
print(serieterror.personajes)
print(serieterror.inicio)
print(serieterror.final)