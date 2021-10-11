from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import math

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("calculadora.ui", self)
        #Seteamos los operadores
        self.operador1 = 0
        self.operador2 = 0
        #Seteamos el tipo de operación a realizar
        self.operacion = ""
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
        self.suma.clicked.connect(self.sumar)
        self.igual.clicked.connect(self.resultado)
        self.borrar.clicked.connect(self.on_borrar)
        self.borrartodo.clicked.connect(self.borrar_operador)
        self.division.clicked.connect(self.dividir)
        self.potencia.clicked.connect(self.potenciacion)
        self.raiz.clicked.connect(self.radicacion)
        
        
    #borra un numero
    def on_borrar(self):
        
        label_content = self.Calculo.text()
        self.Calculo.setText(label_content[:-1])    
    
    #borrar el operador entero
    
    def borrar_operador(self):
        self.Calculo.setText("")
        
            
    #suma
    
    def sumar(self):
  
        if(self.operador1 == 0):
            self.operador1 = int(self.Calculo.text())
            self.Calculo.setText("")
            self.operacion = "suma"
        

        else:       
            self.operador1 = int(self.Calculo.text())
            self.Calculo.setText("")
            self.operacion = "suma"          

    #division
    
    def dividir(self):
        if(self.operador1 == 0):
            self.operador1 = int(self.Calculo.text())
            self.Calculo.setText("")
            self.operacion = "division"
            

        if(self.operador1 and self.operador2 != 0):
            self.operador1 = int(self.Calculo.text())
            self.Calculo.setText("")
            self.operacion = "division"           
    
    #potencia
    
    def potenciacion(self):
    
        if(self.operador1 == 0):
            self.operador1 = int(self.Calculo.text())
            self.Calculo.setText("")
            self.operacion = "potencia"
        

        else:       
            self.operador1 = int(self.Calculo.text())
            self.Calculo.setText("")
            self.operacion = "potencia" 
             
    #radicacion     
    def radicacion(self):
    # Muestro directamente el resultado al presionar el boton raiz    
        if(self.operador1 == 0):
            self.operador1 = int(self.Calculo.text())
            self.Calculo.setText("")
            self.Calculo.setText(str(math.pow(self.operador1,(1/2))))
        

        else:       
            self.operador1 = int(self.Calculo.text())
            self.Calculo.setText("")
            self.Calculo.setText(str(int(math.pow(self.operador1,(1/2)))))  
            
    #Muestra los resultados    
        
    def resultado(self):
        #Se procede a la operación dependiendo del tipo y siempre y cuando este determinado el primer operador.
        if(self.operacion == "suma"):
            self.operador2 = int(self.Calculo.text())
            self.Calculo.setText(str(self.operador1+self.operador2))

        if(self.operacion == "division"):
            self.operador2 = int(self.Calculo.text())
            if self.operador2==0:
                self.Calculo.setText('Math ERROR')
            else:
                self.Calculo.setText(str(int(self.operador1/self.operador2)))
        
        if(self.operacion == "potencia"):
            self.operador2 = int(self.Calculo.text())
            self.Calculo.setText(str(int(math.pow(self.operador1,self.operador2))))


            
    #Eventos de asignación de valores al label
    def click_1(self):
        self.Calculo.setText(self.Calculo.text() + "1")

    def click_2(self): 
        self.Calculo.setText(self.Calculo.text() + "2")
    
    def click_3(self): 
        self.Calculo.setText(self.Calculo.text() + "3")
    
    def click_4(self): 
        self.Calculo.setText(self.Calculo.text() + "4")
    
    def click_5(self): 
        self.Calculo.setText(self.Calculo.text() + "5")
    
    def click_6(self): 
        self.Calculo.setText(self.Calculo.text() + "6")
    
    def click_7(self): 
        self.Calculo.setText(self.Calculo.text() + "7")
    
    def click_8(self): 
        self.Calculo.setText(self.Calculo.text() + "8")
    
    def click_9(self): 
        self.Calculo.setText(self.Calculo.text() + "9")
    
    def click_0(self): 
        self.Calculo.setText(self.Calculo.text() + "0")

app = QApplication([])
win = MiVentana()
win.show()
app.exec_()