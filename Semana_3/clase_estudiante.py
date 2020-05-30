class Estudiante_Universidad:
    #ATRIBUTOS
    coeficiente_intelectual = "Coeficiente Intelectual"
    tolerancia = "Tolerancia"
    respeto = "Respeto"
    amabilidad = "Amabilidad"
    creatividad = "Creatividad"
   
    #constructor
    def init(self):
        print("hola")


    #MÉTODOS
    def aprender(self):
        print("Aprender")
    
    def Entender(self):
        print("Entender")

class Estudiante_Prepa(Estudiante_Universidad):
    #Atributos
    responsabilidad = "Responsabilidad"
    uniforme = "Uniforme"
    empatia = "Empatia"
    pensamiento_crítico = "Pensamiento Critico"
    retencion = "Retención"
    
    #constructor
    def init(self):
        print("constructor herencia")

    #Métodos
    def participar(self):
        print("Participaren clase")
    
    def exponer(self):
        print("Exponer temas en clase")

Cristopher = Estudiante_Prepa()
print("#   METODOS   #")
Cristopher.aprender()
Cristopher.Entender()
Cristopher.participar()
Cristopher.exponer()

print("#   ATRIBUTOS   #")

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