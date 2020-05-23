class Estudiante:
    #ATRIBUTOS
    coeficiente_intelectual = ""
    tolerancia = ""
    respeto = ""
    amabilidad = ""
    creatividad = ""
    responsabilidad = ""
    uniforme = ""
    empatia = ""
    pensamiento_crítico = ""
    retencion = ""


    #MÉTODOS
    def aprender(self):
        print("Aprender")
    
    def Entender(self):
        print("Entender")
    
    def convivir(self):
        print("Convivir con los compañeros")

    def participar(self):
        print("Participaren clase")
    
    def exponer(self):
        print("Exponer temas en clase")

Cristopher = Estudiante()
print("#   METODOS   #")
Cristopher.aprender()
Cristopher.Entender()
Cristopher.convivir()
Cristopher.participar()
Cristopher.exponer()

print("#   ATRIBUTOS   #")

Cristopher.coeficiente_intelectual = "puntuacion de 100"
Cristopher.tolerancia = "Tolerancia con la comunidad universitaria"
Cristopher.respeto = "Respeto a la comunidad Universitaria"
Cristopher.amabilidad = "Amabilidad con todos"
Cristopher.creatividad = "Si"
Cristopher.responsabilidad = "Responsabilidad con las actividades en clase"
Cristopher.uniforme = "pants"
Cristopher.empatia = "Siempre"
Cristopher.pensamiento_crítico = "Al hacer un proyecto"
Cristopher.retencion ="Buena"

print(Cristopher.coeficiente_intelectual)
print(Cristopher.tolerancia)
print(Cristopher.respeto)
print(Cristopher.amabilidad)
print(Cristopher.creatividad)
print(Cristopher.responsabilidad)
print(Cristopher.uniforme)
print(Cristopher.empatia)
print(Cristopher.pensamiento_crítico)
print(Cristopher.retencion)