class Classroom:
 #ATRIBUTOS
    clases = ""
    diseño = ""
    tareas = ""
    profesores = ""
    almacenamiento = ""

   
    #MÉTODOS
    def notificar(self):
        print("Notificar al recibir una tarea")
    
    def almacenar_calificaciones(self):
        print("Almacena calificaiones")
    
    def colaboraciones(self):
        print("Colaboraciones en linea mediante documentos Online")

    def almacenar_tareas(self):
        print("Almacenar Tareas que los profesores suben")
    
    def promedios(self):
        print("Calcula promedios")

Google_Classroom = Classroom()
print("#   METODOS   #")

Google_Classroom.notificar()
Google_Classroom.almacenar_calificaciones()
Google_Classroom.colaboraciones()
Google_Classroom.almacenar_tareas()
Google_Classroom.promedios()

print("#   ATRIBUTOS   #")
Google_Classroom.clases = ""
Google_Classroom.diseño = "Colorido"
Google_Classroom.tareas = ""
Google_Classroom.profesores = ""
Google_Classroom.almacenamiento = "Almacenamiento de Goofle Drive del alumno"

print(Google_Classroom.clases)
print(Google_Classroom.diseño)
print(Google_Classroom.tareas)
print(Google_Classroom.profesores)
print(Google_Classroom.almacenamiento)
