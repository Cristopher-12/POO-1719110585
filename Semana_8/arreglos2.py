print("[   TEMPERATURAS   ]")

contador = 0  #variable contador
class Temperaturas:  #definimos la clase
	promedio_c = 0  #ayudara a almacenar en promedio °C
	promedio_f = 0  #ayudara a almacenar el pomedio de °F
	fechas = []  #almacena las fechas
	centigrados = []  #almacena los °C
	farentheit = []  #almacena la convercion de °c a °f

	def __init__(self):  #metodo constructor
		pass

	def datostemp(self):  #metodo que llevara el recabar los datos
		date = input("Fecha: ")  #pide la fecha
		self.fechas.append(date)  #alamacena la fecha en la variable fechas
		temperatura = int(input("Inserte la temperatura en °C ")
		                  )  #pide la temperatura en °c y de tipo entero
		self.centigrados.append(
		    temperatura)  #almacena en la variable centigrados
		convertir = (temperatura * 9 / 5) + 32  #convierte los °c a °f
		self.farentheit.append(convertir)  #almacena en la variable farentheit

	def convertsearch(self):  #metodo convertit y buscar
		datos = dict(
		    zip(self.farentheit,
		        self.fechas))  #convierte fechas y farentheit a diccionario
		maximo = max(
		    datos.items(), key=lambda x: x[1]
		)  #busca el mayor dato posible, items()Devuelve una lista de tuplas, cada tupla se compone de dos elementos: el primero será la clave y el segundo, su valor.
		#Key retorna una lista de elementos, los cuales serán las claves de nuestro diccionario
		#lambada convierte una funcion a algo anonimo
		abrir = open("Temperaturas.txt",
		             "a")  #abre el archivo en modo append o agregar en español
		abrir.write("los datos son " + str(datos) +
		            "\n")  #escribe en el documento los datos del diccionario
		abrir.write("Temperatura mas alta: " + str(maximo) +
		            "\n")  #escribe y el resultado de la temperatura mas alta
		abrir.close()  #cierra el archivo
		print("Temperatura mas alta es: " +
		      str(maximo))  #imprime la temperatura mas alta y su fecha

	def obtpromedio(self):  #metodo promedio
		self.promedio_centigrados = sum(
		    self.centigrados) / contador  #el calcula el promedio en °c
		#sum() suma todos los numeros de una tupla siempre y cuando sea un dato numerico
		self.promedio_farentheit = sum(
		    self.farentheit) / contador  #calcula el promedio en °f
		print("Promedio en farentheit: " + str(
		    self.promedio_farentheit) + "\n")  #imprime el promedio de los °c
		print("Promedio en centigrados: " + str(
		    self.promedio_centigrados) + "\n")  #imprime el pormedio de los °f

	def archivotext(self):  #metodo archivo
		abrir = open("Temperaturas.txt",
		             "a")  #abre el archivo en modo append o agregar
		abrir.write("Promedio en centigrados: " + str(
		    self.promedio_centigrados) + "\n")  #agrega el promedio de los °c
		abrir.write("Promedio en farentheit: " + str(
		    self.promedio_farentheit) + "\n")  #agrega el promedio de los °f
		abrir.close()  #cierra el archivo


objeto = Temperaturas()  #declaramos el objeto
respuesta = "S"  #variable respuesta ayudara al while y al if
while respuesta == "S" or respuesta == "s":  #mientras respuesta sea S o S
	contador += 1  #el contador sumara 1
	objeto.datostemp()  #llamara al metodo que se encarga de los datos
	respuesta = input("¿Desea leer otra fecha y temperatura?: "
	                  )  #pregunta si quieres leer otra fecha y temperatura
	if respuesta == "N" or respuesta == "n":  #si la respuesta es n o N
		objeto = Temperaturas()  #se declara el objeto
		objeto.obtpromedio()  #llama al metodo preomedio
		objeto.convertsearch()  #llama al metodo de convercion y busqueda
		objeto.archivotext()  #llama al metodo archivo
		break  #termina el codigo
