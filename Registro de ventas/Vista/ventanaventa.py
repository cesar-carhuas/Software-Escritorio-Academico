from PyQt5 import QtWidgets, uic
from Controlador.arregloventa import *
import random

aVen = arregloventa()


class ventanaventa(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(ventanaventa, self).__init__(parent)
        uic.loadUi("UI/ventanaventa.ui", self)
        self.show()
        self.btnregistrar.clicked.connect(self.registrar)
        self.btnconsultar.clicked.connect(self.consultar)
        self.btneliminar.clicked.connect(self.eliminar)
        self.btnmodificar.clicked.connect(self.modificar)
        self.btnlistar.clicked.connect(self.listar)

        self.txtcodigo.setText(str(random.randint(1000, 9999)))

    def obtenercodigo(self):
        return self.txtcodigo.text()

    def obtenerdescripcion(self):
        return self.txtdescripcion.text()

    def obtenerprecio(self):
        return self.txtprecio.text()

    def obtenercantidad(self):
        return self.txtcantidad.text()

    def valida(self):
        if self.txtcodigo.text() == "":
            self.txtcodigo.setFocus()
            return "Código del producto...!!!"
        elif self.txtdescripcion.text() == "":
            self.txtdescripcion.setFocus()
            return "Descripción del producto...!!!"
        elif self.txtprecio.text() == "":
            self.txtprecio.setFocus()
            return "precio del producto...!!!"
        elif self.txtcantidad.text() == "":
            self.txtcantidad.setFocus()
            return "cantidad del producto...!!!"
        else:
            return ""

    def listar(self):
        self.tblventas.setRowCount(aVen.tamañoarregloventa())
        self.tblventas.setColumnCount(7)
        # Cabecera
        self.tblventas.verticalHeader().setVisible(False)
        for i in range(0, aVen.tamañoarregloventa()):
            p = float(aVen.devolverventa(i).getprecio())
            c = int(aVen.devolverventa(i).getcantidad())
            importe = p * c
            impuesto = importe * 0.18
            total = importe + impuesto
            self.tblventas.setItem(i, 0, QtWidgets.QTableWidgetItem(
                aVen.devolverventa(i).getcodigo()))
            self.tblventas.setItem(i, 1, QtWidgets.QTableWidgetItem(
                aVen.devolverventa(i).getdescripcion()))
            self.tblventas.setItem(i, 2, QtWidgets.QTableWidgetItem(
                aVen.devolverventa(i).getprecio()))
            self.tblventas.setItem(i, 3, QtWidgets.QTableWidgetItem(
                aVen.devolverventa(i).getcantidad()))
            self.tblventas.setItem(
                i, 4, QtWidgets.QTableWidgetItem(str(importe)))
            self.tblventas.setItem(
                i, 5, QtWidgets.QTableWidgetItem(str(impuesto)))
            self.tblventas.setItem(
                i, 6, QtWidgets.QTableWidgetItem(str(total)))

    def limpiarControles(self):
        self.txtcodigo.clear()
        self.txtdescripcion.clear()
        self.txtprecio.clear()
        self.txtcantidad.clear()

    def registrar(self):
        if self.valida() == "":
            objVen = venta(self.obtenercodigo(), self.obtenerdescripcion(),
                           self.obtenerprecio(),
                           self.obtenercantidad())
            cod = self.obtenercodigo()
            if aVen.buscarventa(cod) == -1:
                aVen.adicionaVenta(objVen)
                # acli.grabar()
                aVen.grabar()
                self.limpiarControles()
                self.txtcodigo.setText(str(random.randint(1000, 9999)))
            else:
                QtWidgets.QMessageBox.information(self, "Registrar venta",
                                                  "El codigo ingresado ya existe...!!!", QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, "Registrar venta",
                                              "Error en " + self.valida(), QtWidgets.QMessageBox.Ok)

    def consultar(self):
        # self.limpiarTabla()
        if aVen.tamañoarregloventa() == 0:
            QtWidgets.QMessageBox.information(self, "Consultar venta",
                                              "No existen venta a consultar...!!!", QtWidgets.QMessageBox.Ok)
        else:
            codigo, _ = QtWidgets.QInputDialog.getText(self, "Consultar venta",
                                                       "Ingrese el codigo a consultar")
            pos = aVen.buscarventa(codigo)
            if pos == -1:
                QtWidgets.QMessageBox.information(self, "Consultar venta",
                                                  "El codigo ingresado no existe...!!!", QtWidgets.QMessageBox.Ok)
            else:
                self.txtcodigo.setText(aVen.devolverventa(pos).getcodigo())
                self.txtdescripcion.setText(
                    aVen.devolverventa(pos).getdescripcion())
                self.txtprecio.setText(
                    aVen.devolverventa(pos).getprecio())
                self.txtcantidad.setText(
                    aVen.devolverventa(pos).getcantidad())

    def eliminar(self):
        codigo = self.txtcodigo.text()
        pos = aVen.buscarventa(codigo)
        if pos != -1:
            aVen.eleminarventa(pos)
            aVen.grabar()
            self.limpiarControles()
            self.listar

    def modificar(self):
        if aVen.tamañoarregloventa() == 0:
            QtWidgets.QMessageBox.information(self, "Modificar venta",
                                              "No existen venta a modificar...!!!", QtWidgets.QMessageBox.Ok)
        else:
            codigo = self.obtenercodigo()
            pos = aVen.buscarventa(codigo)
            if pos != -1:
                objVen = venta(self.obtenercodigo(), self.obtenerdescripcion(),
                               self.obtenerprecio(),
                               self.obtenercantidad())
                aVen.modificarVenta(objVen, pos)
                aVen.grabar()
                self.limpiarControles()
                self.listar
