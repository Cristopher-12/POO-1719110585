print("[   TEMPERATURAS   ]")

class Temperaturas:#definimos la clase
    def __init__(self): #definimos el metodo constructor
        pass
    def promediotemp(self):#definimos el metodo
        c=[] #almacenara los grados en centigrados
        f=[]#almacena los grados que ce convertieron a farentheit
        respuesta="S"#variable que ayudara a realizar el while
        accountant=0 #ayudara acontar el numero veses que se repitio el codigo
        
        while respuesta=="S" or respuesta=="s" or respuesta=="Si" or respuesta=="si": #si respuesta es positiva
            accountant+=1 #contador aumentara 1 vez
            temperatura=int(input("Inserte la temperatura: ")) #Linea para insertar la temperatura de tipo entero
            c.append(temperatura) #agraga los valores de Temperatura a la variable centigrados
            conv=(temperatura*9/5)+32 #convierte de centigrados a farentheit
            f.append(conv) #agrega la convercion a la variable farentheit
            respuesta=input("¿Desea leer otra temperatura? ") #pregunta si desea leer otra temperatura
            
            if respuesta=="N" or respuesta=="n" or respuesta=="No" or respuesta=="no": #si la se respuesta es negativa
                abrir=open("almacenamiento.txt","a") #abre el archivo de texto en modo de agregar
                abrir.write("Resultado\n") #agrga el siguente texto Resultado + un salto de linea
                abrir.write("las temperaturas capturadas en centigrados son: "+str(c)+"\n") #escrebe las temperaturas de centigrados
                abrir.write("Las temperaturas convertidas a farentheit son: "+str(f)+"\n")#escribe las temperatutas en farentheit
                promedio=sum(c)/accountant#suma todos los grados °C y los divide entre la variavle contador para determinar el promedio de las temperaturas
                promedio_farentheit=sum(f)/accountant#suma todos los °F y los divide entre la variable contador para determinar el promedio de las temperaturas
                abrir.write("Promedio de la temperatura en centigrados: "+str(promedio)+"\n")#escreibe el promedio de los °C
                abrir.write("Promedio de las temperaturas en farentheit: "+str(promedio_farentheit)+"\n")#escribe el promedio de los °F
                abrir.close()#cierra el archivo de texto
                
                print("El promedio de la temperatura en centigrados es "+str(promedio))#imprime en pantalla el promedio de °C
                print("El promedio de las tempertaruras en farentheit es "+str(promedio_farentheit)) #imprime en pantalla el promedio de °F
                
                break #termina el proceso

objeto_Temperaturas=Temperaturas() #llamamos a la clase primaria
objeto_Temperaturas.promediotemp() #llamamos a su metodo para realizar su codigo.

print("[    Esto ha sido todo, Gracias.    ]")