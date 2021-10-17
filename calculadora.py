from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import math
import re

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("calculadora.ui", self)
        #Seteamos los operadores

        #Seteamos el tipo de operación a realizar

        #Listeners de Eventos de los botones de los números
        self.boton1.clicked.connect(self.click_1)
        self.boton2.clicked.connect(self.click_2)
        self.boton3.clicked.connect(self.click_3)
        self.boton4.clicked.connect(self.click_4)
        self.boton5.clicked.connect(self.click_5)
        self.boton6.clicked.connect(self.click_6)
        self.boton7.clicked.connect(self.click_7)
        self.boton8.clicked.connect(self.click_8)
        self.boton9.clicked.connect(self.click_9)
        self.boton0.clicked.connect(self.click_0)
        #Listeners de Eventos de los botones de las operaciones
        self.suma.clicked.connect(self.click_mas)
        self.igual.clicked.connect(self.resultado)
        self.borrar.clicked.connect(self.on_borrar)
        self.division.clicked.connect(self.click_division)
        self.potencia.clicked.connect(self.click_potencia)
        self.raiz.clicked.connect(self.click_raiz)
        self.borrar_operador.clicked.connect(self.on_borrar_operador)
        self.borrartodo.clicked.connect(self.on_borrar_todo)
        self.punto.clicked.connect(self.click_punto)
        self.Calculo.setText("0")
        
    #borra un numero
    def on_borrar(self):
        #Borrar un digito, se utiliza try y except para que no me saque por error de sintaxis
        try:
            label_content = self.label.text()
            self.label.setText(label_content[:-1])
            self.operation = self.label.text() 
            self.result = eval (self.operation)
            self.Calculo.setText(str(self.result))
        except SyntaxError: 
            pass 
            
    def on_borrar_operador(self):
        #Borrar las operaciones en la  pantalla "label"
        self.label.setText("") 
    
    def on_borrar_todo(self):
        #Borramos todo en pantalla label como Calculo
        self.label.setText("")
        self.Calculo.setText("")
          
    
    def resultado(self):
        #al presional el boton igual.
        
        try:
            self.operation = self.label.text() 
            self.result = eval (self.operation)
            self.label.setText(self.label.text() + "=" )
            self.Calculo.setText(str(self.result))
        except ZeroDivisionError:
            self.Calculo.setText('No se puede dividir entre cero')


    
    
    def hacer_operacion(self,num):
        if "^" in self.label.text():
            self.label.setText(self.label.text() + num)
            self.new_operador = self.label.text().replace('^','**')
            self.result = eval (self.new_operador)
            self.Calculo.setText(str(self.result))
        else:   
            self.label.setText(self.label.text() + num )
            self.operation = self.label.text() 
            self.result = eval (self.operation)
            self.Calculo.setText(str(self.result))
    
            
    #asignamos a cada tecla la operacion, mientras presionamos el numero se muestra en label y automaticamente me realiza la operacion
    def click_1(self):
        self.hacer_operacion("1")
        
        
           
    def click_2(self):
        self.hacer_operacion("2")

    
    def click_3(self):
        self.hacer_operacion("3")


    
    def click_4(self):
        self.hacer_operacion("4")

        
    def click_5(self):
        self.hacer_operacion("5")
        
    def click_6(self):
        self.hacer_operacion("6")
 
    
    def click_7(self):
        self.hacer_operacion("7")

    
    def click_8(self):
        
        self.hacer_operacion("8")

    
    def click_9(self):
        self.hacer_operacion("9")

    
    def click_0(self):
        if "^" in self.label.text():
            self.label.setText(self.label.text() + "0")
            self.new_operador = self.label.text().replace('^','**')
            self.result = eval (self.new_operador)
            self.Calculo.setText(str(self.result)) 
        else:
            self.label.setText(self.label.text() + "0")
            #se utiliza try por que podemos clickear el 0 en una division y como denominador no es posible
            try:    
                self.operation = self.label.text()
                self.result = eval (self.operation)
                self.Calculo.setText(str(self.result))
            except ZeroDivisionError:
                self.Calculo.setText('No se puede dividir entre cero')

    
    def click_mas(self):
        if (("=")) in self.label.text():
            self.label.setText(self.Calculo.text()+"+")
        #Para seguir mostrando la operacion de sumandos 
        elif "+" in self.label.text():
            self.label.setText(self.label.text() + "+")
        #Si borro la operacion q esta en label al presionar "+" lo que esta en Calculo pasa a label mas el signo (+)
        elif "" in self.label.text():
            self.label.setText(self.Calculo.text() + "+")
        else:
            self.label.setText(self.label.text() + "+")
            

    def click_division(self):
        if ("=") in self.label.text():
            self.label.setText(self.Calculo.text()+"/")
        else:
            try:    
                self.label.setText(self.label.text() + "/")
            except ZeroDivisionError:
                self.Calculo.setText('No se puede dividir entre cero')

        
    def click_raiz(self):
        #Obtengo la raiz del numero que se encuentra en la pantalla Calculo
            self.result = float(self.Calculo.text())**(1/2)
            self.label.setText("√" + "(" +self.Calculo.text()+")")
            self.Calculo.setText(str(self.result))
    
    def click_potencia(self):

        self.label.setText(self.label.text() + "^")
        
    def click_punto(self):
        self.label.setText(self.label.text() + ".")
        
        
   

            
app = QApplication([])
win = MiVentana()
win.show()
app.exec_()