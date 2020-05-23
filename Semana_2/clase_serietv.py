class SerieTV:
    #ATRIBUTOS
    entretenimiento = ""
    genero = ""
    trama = ""
    reparto = ""
    guion = ""
    capitulos = ""
    duracion = ""
    personajes =""
    inicio = ""
    final = ""
    #MÉTODOS
    def entretener(self):
        print("Entretener")
    
    def grabar(self):
        print("Grabar las escenas")
    
    def actuar(self):
        print("Perfecta actuación")

    def causar_emociones(self):
        print("Espantar, entristecer, enojar")
    
    def interesar (self):
        print("Interesar a la audiencia a seguir viendo la serie")

serieterror = SerieTV()
print("#   METODOS   #")
serieterror.entretener()
serieterror.grabar()
serieterror.actuar()
serieterror.causar_emociones()
serieterror.interesar()


print("#   ATRIBUTOS   #")

serieterror.entretenimiento = ""
serieterror.genero = "Actividades Paranormales"
serieterror.trama = "Terror"
serieterror.reparto = "Actores y actrices"
serieterror.guion = "Guion terrorifico"
serieterror.capitulos = "20 capitulos en la primera temporada"
serieterror.duracion = "30-40 minutos por capitulo"
serieterror.personajes = "Protagonista, objeto terrorifico, Amigos"
serieterror.inicio = "Inicio oscuro"
serieterror.final = "Final sangriento"

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