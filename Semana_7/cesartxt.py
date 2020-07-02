class CodigoCesarArchivos: #Definimos la clase primaria
    def __init__(self): #definimos su metodo constructor
        pass
    def cifradoDesifrado(self): #Metodo que llevara a cabo el codigo que cifra o descifra
        respuesta="S" #Variable que ayudara el bucle while
        while respuesta=="S" or respuesta=="s": #Si respuesta es s o S se corre el resto del codigo
            cifrar = "" #variable que ayudara a guardar el cifrado del archivo
            descifrar = "" #variable que ayudara a guardar el descifrado del archivo
            archivo = input("Nombre del archivo y extencion ") #linea para escribir el nombre del archivo con su extencion
            abrir = open(archivo, "r") #esta variable abre el archivo en modo lectura
            leer = abrir.read() #lee las lineas de archivo de texto que abrio
            print(leer)#imprime las lineas del archivo de texto
            pregunta = input("¿Desea cifrar o descifrar? ") #pregunta si desea cifrar o descifrar
            if pregunta == "cifrar" or pregunta == "Cifrar": #si es cifrar
                abrir = open(archivo, "w") #abre el archivo para sustituir el texto
                for scannear in leer: #lee el archivo 
                    alfabeto = ord(scannear) #cada caracter del archivo lo convierte a su codigo ASCII
                    cifrar += chr(alfabeto - 7)#le resta al codigo ASCII 7 y los convierte en su propio caracter
                abrir.write(cifrar) #se cifra el archivo rescribiendo el cifrado
                print(cifrar) #imprime el cifrado que se le dio al texto
                abrir.close()# cierra el archivo
            if pregunta == "Descifrar" or pregunta == "descifrar": #si es descifrar
                abrir = open(archivo, "w") #abre al archivo para sustituir el texto
                for scannear in leer: #lee archivo 
                    alfabeto = ord(scannear)#convierte cada caracter en codigo ASCII
                    descifrar += chr(alfabeto + 7)#al cogico del caracter se le suma 7 y lo convierte en caracter
                abrir.write(descifrar) #escribe el cifrado del texto 
                abrir.close()#cierra el archivo de texto
                print(descifrar)#imprime el descifrado del archivo
            respuesta=input("Desea cifrar o desifrar otro archivo de texto? ") #pregunta si desea analizar otro archivo de texto
            if respuesta=="N" or respuesta=="N": #si la respuesta es N o n
                break #termina de ejecutar el codigo
objeto_cifrado=CodigoCesarArchivos() #se llama a la clase principal
objeto_cifrado.cifradoDesifrado() #se llama al metodo