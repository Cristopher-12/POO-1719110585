print("   CIFRAR / DESCIFRAR   ")
class Clave: # Clase
    def __init__(self):#constructor
        pass
    def metodocifrado_descifrado(self): # Metodo que hace las comparaciones entre las cadenas
        respuesta = "S"
        while respuesta == "S" or respuesta == "s":

            # Cadena de texto que deseamos cifrar
            texto = input("Inserta tu texto: ")

            # La llave de cifrado o descifrado
            n = 3

            # Le decimos al programa que queremos realizar
            accion = input("¿Cifrar o descifrar? ")   #'decrypt' # 'encrypt' o 'decrypt'

            # Abecedario a utilizar en el cifrado
            abecedario = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

            # Variable para guardar mensaje cifrado
            cif = ''

            # Ponemos en mayúsculas todo el texto
            texto = texto.upper()

            # Recorremos el mensaje
            for s in texto:
                if s in abecedario:
                    # Obtenemos el indice del simbolo
                    num = abecedario.find(s) 
                    if accion == 'cifrar' or accion == 'Cifrar':
                        num = num + n
                    elif accion == 'descifrar' or accion == 'Descifrar':
                        num = num - n

                    # si num es mayor que el largo de
                    # abecedario o es menor que  0
                    if num >= len(abecedario):
                        num = num - len(abecedario)
                    elif num < 0:
                        num = num + len(abecedario)

                    # Agregamos el simbolo al texto cifrado
                    cif = cif + abecedario[num]

                else:
                    # Agregamos el simbolo
                    cif = cif + s
            print(cif)

            # Pregunta para continuar cifrando y descifrando o terminar el proceso
            respuesta = input("Desea cifrar o descifrar de nuevo? S/N ")
            if respuesta == "N" or respuesta == "n":
                #Fin del Cifrado/Descifrado
                break 

# Se imprimen los resultados
password = Clave()
password.metodocifrado_descifrado()
print("###   Codigo CESAR Finalizado   ###")