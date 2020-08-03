print("[    Diccionario Peliculas    ]")

answer="S" #variable que ayudara al ciclo while
movaño=[] #arreglo para almacenar el nombre y año de la pelicula
genero=[] #arreglo para almacenar el genero de la pelicula

class Diccionario_movies: #creamos la clase Peliculas
    def __init__(self): #definimos el metodo contructor
        pass
    def inf_movies(self): #metodo que pide los datos de las peliculas
        nombre=input("Nombre de pelicula: ") #pide el nombre de la pelicula
        año=input("Año de lanzamiento: ") #pide el año de lanzamiento de la pelicula
        genero_pelicula=input("Genero: ") #pide el genero de la pelicula
        movaño.append(str(nombre)+" Año: "+str(año)) #añade al arreglo el nombre y el año de estreno
        genero.append(genero_pelicula) #añade el nombre del genero de la pelicula
    
    def diccmovies(self): #metodo de busqueda,almacenamiento y convertir a diccionario
        datos=dict(zip(movaño,genero)) #crea un diccionario usando los arreglos creados
        print(datos) #imprime el diccionario creado
        nombre_genero=input("Genero de una pelicula: ") #pide el nombre de un genero de pelicula
        if nombre_genero in datos.values(): #si el nombre del genero esta el los valores del diccionario
            for catalogo in datos: #lee el diccionario
                if datos[catalogo]==nombre_genero: #si el diccionario tiene el genero que insertaste
                    print(catalogo) #impime las peliculas con ese genero

while answer=="s" or answer=="S" or answer=="Si" or answer=="si": #mientras respuesta sea positiva
    objeto_Peliculas=Diccionario_movies() #Llama a la clase objeto
    objeto_Peliculas.inf_movies() #invoca a los el metodo que pide los datos
    answer=input("¿Desea añadir más peliculas? ") #si deseas continuar capturando peliculas 
    
    if answer=="n" or answer=="N" or answer=="No" or answer=="no": #si la respuesta es negativa
        objeto_Peliculas.diccmovies() #invoca al metodo de que busca y crea un diccionario
        break #finaliza el codigo con un brake