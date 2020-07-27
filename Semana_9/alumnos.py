answer="S" #variable para ayudar al ciclo while
datos = [] #arreglo para ayudar a almacenar los datos

class Alumnos: #creamos una clase
    def __init__(self): #metodo constrcutor
        pass
    
    def datos(self): #creamos un metodo para perdir datos
        name=input("Inseta el nombre del alumno: ") #Pide el nombre del alumno
        año=int(input("Año de nacimeinto del alumno: ")) #pide el año de nacimiento del alumno tipo entero
        grupo=input("Inserta el grupo del alumno: ") #pide el grupo del alumno
        años_total=2020-año #calcula la edad restando el año actual con el año de nacimiento
        datos.append("Nombre:"+str(name)+" Edad:"+str(años_total)+" Grupo:"+str(grupo)) #agrega los datos
        #al arreglo datos
    
    def Print(self): #creamos metodo para imprimir los datos capturados
        for leer in datos: #leera el arreglo datos
            print(leer) #imprimira en pantalla los datos capturados por indice

while answer=="s" or answer=="S" or answer=="Si" or answer=="si": #mientras que la repuesta sea S
    objecto_Almuno=Alumnos() #creamos el objeto
    objecto_Almuno.datos()#se estara llamando al metodo para la captura de datos
    answer=input("¿Desea leer mas datos de alumnos? S/N ") #pregunta si deseas hacer mas capturas de alumnos
    if answer=="N" or answer=="n" or answer=="No" or answer=="no": #si la respuesta es "N" o "n"
        objecto_Almuno.Print() #llama al metodo que permitira imprimir
        break #termina el ciclo del programa