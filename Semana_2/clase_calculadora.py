class Calculadora:
 #ATRIBUTOS
    botones = ""
    color = ""
    funciones = ""
    formulas = ""
    pilas = ""
    pantalla = ""
   
    #MÉTODOS
    def sumar(self):
        print("Sumar una cantidad con otra")
    
    def encender(self):
        print("Enciende correctamente al presionar el boton de encendido")
    
    def restar(self):
        print("Resta cantidades")

    def dividir(self):
        print("Divide cantidades")
    
    def multiplicar(self):
        print("Multiplica cantidades")

Calculadora_Cientifica = Calculadora()
print("#   METODOS   #")

Calculadora_Cientifica.sumar()
Calculadora_Cientifica.encender()
Calculadora_Cientifica.restar()
Calculadora_Cientifica.dividir()
Calculadora_Cientifica.multiplicar()

print("#   ATRIBUTOS   #")

Calculadora_Cientifica.botones = "Botones de encendido y apagado, numericos, punto decimal"
Calculadora_Cientifica.color = "Color Gris"
Calculadora_Cientifica.funciones = "Sin, cos, tan"
Calculadora_Cientifica.formulas = "formula general algebraica"
Calculadora_Cientifica.pilas = "1 pila"
Calculadora_Cientifica.pantalla = "LED capaz de mostrar digitos"


print(Calculadora_Cientifica.botones)
print(Calculadora_Cientifica.color)
print(Calculadora_Cientifica.funciones)
print(Calculadora_Cientifica.formulas)
print(Calculadora_Cientifica.pilas)
print(Calculadora_Cientifica.pantalla)