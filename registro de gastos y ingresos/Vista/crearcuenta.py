from PyQt5 import QtWidgets, uic
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QWidget
# from VISTA.ventanaPrincipal import VentanaPrincipal
from PyQt5.QtGui import QIntValidator
from Controlador.conexion import registro_datos
import time


class crearcuenta(QtWidgets.QMainWindow):
    def __init__(self, previous_window=None):
        super(crearcuenta, self).__init__(previous_window)
        uic.loadUi("UI/crear_cuenta.ui", self)
        self.conexion = registro_datos()
        self.show()
        self.previous_window = previous_window
        self.btncrear.clicked.connect(self.crearCuenta)
        self.btnlogin.clicked.connect(self.VolverLogin)
        self.txttelefono.setValidator(QIntValidator())

    def crearCuenta(self):
        nombre = self.txtnombre.text()
        apellido = self.txtapellido.text()
        usuario = self.txtusuarioCrear.text()
        password = self.txtpassCrear.text()
        telefono = self.txttelefono.text()
        correo = self.txtcorreo.text()
        cur = self.conexion.conexion.cursor()

        cur.execute("SELECT * FROM empleado WHERE nombreEmp = %s", (nombre,))

        result = cur.fetchall()

        if result:
            QtWidgets.QMessageBox.information(self, "Registrar Empleado",
                                              "El nombre ingresado ya existe...!!!", QtWidgets.QMessageBox.Ok)
        elif len(nombre) <= 4:
            QtWidgets.QMessageBox.information(self, "Registrar Empleado",
                                              "no hay nombre...!!!", QtWidgets.QMessageBox.Ok)
        elif len(apellido) <= 4:
            QtWidgets.QMessageBox.information(self, "Registrar Empleado",
                                              "no hay apellido...!!!", QtWidgets.QMessageBox.Ok)
        elif len(usuario) <= 4:
            QtWidgets.QMessageBox.information(self, "Registrar Empleado",
                                              "no hay usuario...!!!", QtWidgets.QMessageBox.Ok)
        elif len(password) <= 4:
            QtWidgets.QMessageBox.information(self, "Registrar Empleado",
                                              "no hay contraseña...!!!", QtWidgets.QMessageBox.Ok)
        elif len(telefono) <= 7:
            QtWidgets.QMessageBox.information(self, "Registrar Empleado",
                                              "no hay telefono...!!!", QtWidgets.QMessageBox.Ok)
        elif len(correo) <= 4:
            QtWidgets.QMessageBox.information(self, "Registrar Empleado",
                                              "no hay correo...!!!", QtWidgets.QMessageBox.Ok)

        else:
            cur.execute("insert into empleado values (%s, %s, %s, %s, %s, %s, %s)",
                        ("", nombre, apellido, usuario, password, telefono, correo))
            self.conexion.conexion.commit()
            # QtWidgets.QMessageBox.information(self, "Registrar Empleado",
            #                                   "no hay DATOS...!!!", QtWidgets.QMessageBox.Ok)
            for i in range(0, 100):
                time.sleep(0.02)
                self.progressBar.setValue(i)
            cur.close()
            self.VolverLogin()

    def VolverLogin(self):
        self.close()
        if self.previous_window:
            self.previous_window.show()
