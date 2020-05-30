class Calculadora:
 #ATRIBUTOS
    botones = "Pilas"
    color = "color"
    pilas = "Pilas"
   #constructor
    def init(self):
        print("hola")

    #MÉTODOS
    def sumar(self):
        print("Sumar una cantidad con otra")
    def restar(self):
        print("Resta cantidades")

class Caluladora_Grafica(Calculadora):
    #Atributos
    funciones = "Funciones"
    formulas = "Formulas"
    pantalla = "Pantalla"
    
    #constructor
    def init(self):
        print("constructor herencia")

    #Métodos
    def dividir(self):
        print("Divide cantidades")
    
    def multiplicar(self):
        print("Multiplica cantidades")

Calculadora_avanzada = Caluladora_Grafica()
print("#   METODOS   #")

Calculadora_avanzada.sumar()
Calculadora_avanzada.restar()
Calculadora_avanzada.dividir()
Calculadora_avanzada.multiplicar()

print("#   ATRIBUTOS   #")

print(Calculadora_avanzada.botones)
print(Calculadora_avanzada.color)
print(Calculadora_avanzada.funciones)
print(Calculadora_avanzada.formulas)
print(Calculadora_avanzada.pilas)
print(Calculadora_avanzada.pantalla)