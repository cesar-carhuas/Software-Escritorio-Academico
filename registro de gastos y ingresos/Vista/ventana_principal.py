from PyQt5 import QtWidgets, uic
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QWidget
# from VISTA.ventanaPrincipal import VentanaPrincipal
from Vista.ventana_ingresos import ingresos
from Vista.ventana_gastos import gastos
from Vista.ventana_historial import historial
from Vista.ventana_graficos import graficos


class ventanaPrincipal(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(ventanaPrincipal, self).__init__(parent)
        uic.loadUi("UI/ventana_principal.ui", self)
        self.show()

        self.btningreso.clicked.connect(self.ingresos)
        self.btngastos.clicked.connect(self.gastos)
        self.btnhistorial.clicked.connect(self.historial)
        self.btngrafico.clicked.connect(self.graficos)

    def ingresos(self):
        self.close()
        Vingreso = ingresos(self)
        Vingreso.show()

    def gastos(self):
        self.close()
        Vgastos = gastos(self)
        Vgastos.show()

    def historial(self):
        self.close()
        Vhistorial = historial(self)
        Vhistorial.show()

    def graficos(self):
        self.close()
        Vgraficos = graficos(self)
        Vgraficos.show()
