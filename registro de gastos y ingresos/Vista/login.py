from PyQt5 import QtWidgets, uic
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QWidget
# from VISTA.ventanaPrincipal import VentanaPrincipal
from Vista.crearcuenta import crearcuenta
from Vista.ventana_principal import ventanaPrincipal
from Controlador.conexion import registro_datos
import time


class login(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(login, self).__init__(parent)
        uic.loadUi("UI/login.ui", self)
        self.datos = registro_datos()
        self.show()
        # EVENTOS.....
        self.btniniciar.clicked.connect(self.iniciarSesion)
        self.btncrear.clicked.connect(self.crearCuenta)

    # Aquí van las nuevas funciones
    def iniciarSesion(self):
        self.usuario_incorrecto.setText('')
        self.pass_incorrecto.setText('')
        users_entry = self.txtusuario.text()
        password_entry = self.txtpass.text()

        # users_entry = str("'" + users_entry + "'")
        # password_entry = str("'" + password_entry + "'")

        dato1 = self.datos.buscar_user(users_entry)
        dato2 = self.datos.busca_pass(password_entry)

        if dato1 == [] and dato2 == []:
            self.usuario_incorrecto.setText('usuario incorrecto')
            self.pass_incorrecto.setText('contraseña incorrecto')

        else:
            if dato1 == []:
                self.usuario_incorrecto.setText('usuario incorrecto')
            else:
                dato1 = dato1[0][3]

            if dato2 == []:
                self.pass_incorrecto.setText('contraseña incorrecto')
            else:
                dato2 = dato2[0][4]

            if dato1 != [] and dato2 != []:
                for i in range(0, 100):
                    time.sleep(0.02)
                    self.progressBar.setValue(i)
                self.close()
                self.mesas = ventanaPrincipal()
                self.mesas.show()

        # usuario = self.txtusuario.text().lower()
        # contraseña = self.txtpass.text()
        # if usuario == "cesar" and contraseña == "123456":
        #     self.close()
        #     # vprincipal = VentanaPrincipal(self)
        #     # vprincipal.show()
        # else:
        #     QtWidgets.QMessageBox.information(self, "contraseña incorrecta",
        #                                       "colocar bien la contraseña...!!!", QtWidgets.QMessageBox.Ok)

    def crearCuenta(self):
        self.close()
        Vcuenta = crearcuenta(self)
        Vcuenta.show()
