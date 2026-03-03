from PyQt5 import QtWidgets, uic
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QWidget
# from VISTA.ventanaPrincipal import VentanaPrincipal
from Controlador.conexion import registro_datos


class gastos(QtWidgets.QMainWindow):
    def __init__(self, previous_window=None):
        super(gastos, self).__init__(previous_window)
        uic.loadUi("UI/gastos.ui", self)
        self.datos = registro_datos()
        self.show()

        self.previous_window = previous_window
        self.btnvolver.clicked.connect(self.volver)
        self.btnagregar.clicked.connect(self.agregar_Datos_salida)

    def volver(self):
        self.close()
        if self.previous_window:
            self.previous_window.show()

    def agregar_Datos_salida(self):
        tiempo = self.txttiempo.text()
        tipo = self.txttipo.text()
        nombre = self.txtnombre.text()
        salida = self.txtsalida.text()
        cur = self.datos.conexion.cursor()

        query = "INSERT INTO historial (fecha, tipo, nombre, salida) VALUES (%s, %s, %s, %s)"
        valores = (tiempo, tipo, nombre, salida)
        cur.execute(query, valores)
        self.datos.conexion.commit()
        cur.close()

        self.txttiempo.clear()
        self.txttipo.clear()
        self.txtnombre.clear()
        self.txtsalida.clear()

        QtWidgets.QMessageBox.information(self, "Exito",
                                          "Se agrego el dato correcto...!!!", QtWidgets.QMessageBox.Ok)
