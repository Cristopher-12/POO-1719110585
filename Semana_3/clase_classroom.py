class Moodle:
    #ATRIBUTOS
    profesores = "Profesores"
    almacenamiento = "Almacenamiento"
    configuracion = "Configuracion"

    #constructor
    def init(self):
        print("hola")

    #MÉTODOS
    def almacenar_tareas(self):
        print("Almacenar Tareas que los profesores suben")
    
    def promedios(self):
        print("Calcula promedios")

class Classroom(Moodle):
    #ATRIBUTOS
    clases = "Clases"
    diseño = "Diseño"
    tareas = "Tareas"
    interfaz = "Interfaz"

   #Constructor
    def init(self):
        print("constructor herencia")
    
    #MÉTODOS
    def notificar(self):
        print("Notificar al recibir una tarea")
    
    def almacenar_calificaciones(self):
        print("Almacena calificaiones")
    

Google_Classroom = Classroom()
print("#   METODOS   #")

Google_Classroom.notificar()
Google_Classroom.almacenar_calificaciones()
Google_Classroom.almacenar_tareas()
Google_Classroom.promedios()

print("#   ATRIBUTOS   #")

print(Google_Classroom.clases)
print(Google_Classroom.diseño)
print(Google_Classroom.tareas)
print(Google_Classroom.profesores)
print(Google_Classroom.almacenamiento)