print("   PALINDROMOS   ")
class Palindromo: # Clase
    def __init__(self):#constructor
        pass
    def metodopalindromo(self): # Metodo que hace las comparaciones entre las cadenas
        answ = "S" # Respuesta de satisfactoria para repetir el analisis
        
        while answ == "S" or answ == "s": # Si la respuesta es S se hara otro analisis
            cad = input("inserta tu cadena: ") # Insertamos la cadena a analizar
            numeroespacios= 0 # Almacena el numero de espacios
            cad = cad.lower() # Reemplaza las mayusculas por minusculas
            for espacios in cad: # Analizara la cadena
                if espacios in " ": #Cada espacio será contado
                    numeroespacios +=1
            print("Numero de espacios: " +str(numeroespacios))
            
            cad = cad.lower() # Convierte todas las mayusculas en minusculas
            cad= cad.replace(" ","") # Elimina espacios de la cadena
                    # Cambia las letras con asento por una letra sin asento
            cad = cad.replace("á", "a") 
            cad = cad.replace("é", "e")
            cad = cad.replace("í", "i")
            cad = cad.replace("ó", "o")
            cad = cad.replace("ú", "u")
            numerovocales = 0 # Almacena el numero de Vocales
            for vocales in cad: # Analiza todos los valores de la cadena
                if vocales in "áéíóúaeiou":
                    numerovocales += 1 # Cada vocal se contará
            print("Numero de vocales: "+str(numerovocales))
            
            palindromo = "" # Almacena la cadena que se invertirá
            for i in cad: # i tendra como inicio la ultima letra de la cadena hasta la primera
                palindromo = i + palindromo # sera la cadena invertida que se obtuvo de la línea 33
            if cad == palindromo: # Analiza si la cadena es un palindromo 
                print("La cadena es un Palindromo") # Nos afirma si la cadena es un palindromo
            
            else: 
                
                print("La cadena no es un palindromo") # Nos Niega que la cadena sea un Palindromo en caso de no cumplir con los requisitos
            
            answ = input("Desea anlizar otra cadena? s/n: ") # Pregunta para analizar otra cadena
            if answ == "n" or answ == "N": # Si la respuesta es N se termina de ejecutar el analisis
                break #Fin del analisis


cadenapalindromo = Palindromo()

cadenapalindromo.metodopalindromo()

print("### FIN DEL ANALISIS ###")