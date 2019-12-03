import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
        QMessageBox, QProgressBar)

from PyQt5 import uic

#crear un clase hererada de QMainWindow que permita crear ventana
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        #cargamos la configuración .ui en el objeto
        uic.loadUi("maindemo.ui",self)
        self.setWindowTitle("Pantalla Demo DMS 1.0")
        #self.showMaximized()
        #Fijar tamaño de la ventana
        self.setMinimumSize(600,400)
        self.setMaximumSize(800,600)

#Instancia para lanzar la aplicación
app = QApplication(sys.argv)
#crear objeto de la clase que creamos con la ventana principal
_ventana = MainWindow();

_ventana.show()
#ejecutamos la aplicacion
app.exec_()