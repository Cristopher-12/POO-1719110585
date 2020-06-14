class Palindromo:
    def __init__(self):
        pass
    def metodoPalindromo(self):
        respuesta= "S"
        while respuesta == "S" or respuesta == "s":
            cadena = input("inserta tu cadena: ")
            cadena = cadena.lower() # Reemplaza las mayusculas por minusculas
            cadena= cadena.replace(" ","")#eiminar espacios de la cadena
            palindromo = "" #variable de tipo cadena
            for i in cadena: #lee la dacena de atras hacia adelante
                palindromo= i+palindromo
                if cadena == palindromo:
                    print("Tu cadena es un palindromo")
                else :
                    print("Tu cadena no es palindromo")
                respuesta = input("Desea analzar otra cadena? S/N")
                if respuesta!= "S" or respuesta!= "s":
                    break #terminar de ejecutar

objeto_palindromo= Palindromo()
objeto_palindromo.metodoPalindromo()
