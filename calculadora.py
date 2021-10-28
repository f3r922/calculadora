from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from PyQt5 import Qt
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
        self.resta.clicked.connect(self.click_menos)
        self.igual.clicked.connect(self.resultado)
        self.borrar.clicked.connect(self.on_borrar)
        self.division.clicked.connect(self.click_division)
        self.potencia.clicked.connect(self.click_potencia)
        self.raiz.clicked.connect(self.click_raiz)
        self.borrar_operador.clicked.connect(self.on_borrar_operador)
        self.borrartodo.clicked.connect(self.on_borrar_todo)
        self.punto.clicked.connect(self.click_punto)
        self.producto.clicked.connect(self.click_por)
        self.paren1.clicked.connect(self.click_parentesis_abro)
        self.paren2.clicked.connect(self.click_parentesis_cierro)
        self.Calculo.setText("0")
        
    #agrega por teclado    
    def keyPressEvent(self,event):
        
        
        if event.text() == "1":
            self.hacer_operacion("1")
        if event.text() == "2":
            self.hacer_operacion("2")
        if event.text() == "3":
            self.hacer_operacion("3")
        if event.text() == "4":
            self.hacer_operacion("4")
        if event.text() == "5":
            self.hacer_operacion("5")
        if event.text() == "6":
            self.hacer_operacion("6")
        if event.text() == "7":
            self.hacer_operacion("7")
        if event.text() == "8":
            self.hacer_operacion("8")
        if event.text() == "9":
            self.hacer_operacion("9")
        if event.text() == "0":
            self.click_0()
        if event.text() == ".":
            self.click_punto()
        #operaciones
        if event.text() == "+":
            self.click_mas()
        if event.text() == "-":
            self.click_menos()
        if event.text() == "*":
            self.click_por()
        if event.text() == "/":
            self.click_division()
        if event.key() == 16777220:
            self.resultado()
        
            
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
            self.Calculo.setText("0")
            
    def on_borrar_operador(self):
        #Borrar las operaciones en la  pantalla "label"
        self.label.setText("") 
    
    def on_borrar_todo(self):
        #Borramos todo en pantalla label como Calculo
        self.label.setText("")
        self.Calculo.setText("0")
          
    
    def resultado(self):
        #al presional el boton igual.
        
        try:
            self.operation = self.label.text() 
            self.result = eval (self.operation)
            self.label.setText("")
            numero_coma = "{:,}".format(self.result)
            self.Calculo.setText(str(numero_coma))
            
    
            
        except ZeroDivisionError:
            self.Calculo.setText('No se puede dividir entre cero')
        except SyntaxError:
            self.Calculo.setText('Syntax Error')
            self.label.setText("")


    #cambia el las etiquitas y actaliza el contenido
    
    def hacer_operacion(self,num):
        try:
            if "," in self.label.text():
                self.new_operador = self.label.text().replace(',','')
            if "No se puede dividir entre cero" in self.Calculo.text():
                self.Calculo.setText("0")
            if "Math ERROR" in self.Calculo.text():
                self.Calculo.setText("0")
        

        
        #verifica el simbolo de potencia y lo cambia por el operador
            if "^" in self.label.text():
                self.label.setText(self.label.text() + num)
                self.new_operador = self.label.text().replace('^','**')
                self.result = eval (self.new_operador)
                numero_coma = "{:,}".format(self.result)
                self.Calculo.setText(str(numero_coma))

            else:   
                self.label.setText(self.label.text() + num )
                self.operation = self.label.text() 
                self.result = eval (self.operation)
                numero_coma = "{:,}".format(self.result)
                self.Calculo.setText(str(numero_coma))
        except SyntaxError:
            pass
                
        
                
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
            numero_coma = "{:,}".format(self.result)
            self.Calculo.setText(str(numero_coma))
            
        else:
            self.label.setText(self.label.text() + "0")
            #se utiliza try por que podemos clickear el 0 en una division y como denominador no es posible
            try:    
                self.operation = self.label.text()
                self.result = eval (self.operation)
                numero_coma = "{:,}".format(self.result)
                self.Calculo.setText(str(numero_coma))
                
            except ZeroDivisionError:
                self.Calculo.setText('No se puede dividir entre cero')
                self.label.setText("")

    
    def click_mas(self):
        

            if self.label.text() == (""):
                a = self.Calculo.text().replace(',','')
                self.label.setText( a + "+")
                
            ##Para seguir mostrando la operacion de sumandos 
            #elif "+" in self.label.text():
            
                #self.label.setText(self.label.text() + "+")
            #Si borro la operacion q esta en label al presionar "+" lo que esta en Calculo pasa a label mas el signo (+)
            #elif "" in self.label.text():
                #a = self.Calculo.text().replace(',','')
                #self.label.setText( a + "+")
                
             
            else:
                self.label.setText(self.label.text() + "+")

    
            
    def click_menos(self):
        
        if self.label.text() == (""):
            
            a = self.Calculo.text().replace(',','')
            self.label.setText( a + "-")
        #Para seguir mostrando la operacion de sumandos 
        
        #elif "-" in self.label.text():
            #self.label.setText(self.label.text() + "-")
        #Si borro la operacion q esta en label al presionar "+" lo que esta en Calculo pasa a label mas el signo (+)
        
        #elif "" in self.label.text():
            #a = self.Calculo.text().replace(',','')
            #self.label.setText( a + "-")
        else:
            self.label.setText(self.label.text() + "-")        

    def click_division(self):

        if self.label.text() == (""):
            a = self.Calculo.text().replace(',','')
            
            self.label.setText( a + "/")
                
        else:
            try:    
                self.label.setText(self.label.text() + "/")
            except ZeroDivisionError:
                self.Calculo.setText('No se puede dividir entre cero')

        
    def click_raiz(self):
        #Obtengo la raiz del numero que se encuentra en la pantalla Calculo

        try:
            self.operador = eval (self.Calculo.text().replace(',',''))
            self.result = float(math.sqrt(self.operador))
            self.label.setText("√" + "(" + str(self.operador) +")")
            self.Calculo.setText(str(self.result))   
        except ValueError:
            self.Calculo.setText('Math ERROR')
            self.label.setText("")   
            
    def click_potencia(self):
        if self.label.text() == (""):
                
            a = self.Calculo.text().replace(',','')
            self.label.setText( a + "^")
        else:
            self.label.setText(self.label.text() + "^")
        
    def click_punto(self):
            
        self.label.setText(self.label.text() + ".")
    
    def  click_por(self): 
        if self.label.text() == (""):
                
            a = self.Calculo.text().replace(',','')
            self.label.setText( a + "*")
        else:
            self.label.setText(self.label.text() + "*")
    
    def click_parentesis_abro(self):
        self.label.setText(self.label.text() + "(")


    def click_parentesis_cierro(self):
        try:
            self.label.setText(self.label.text() + ")")
            self.operation = self.label.text() 
            self.result = eval (self.operation)
            self.Calculo.setText(str(self.result))
        except SyntaxError:
            pass
            
app = QApplication([])
win = MiVentana()
win.show()
app.exec_()