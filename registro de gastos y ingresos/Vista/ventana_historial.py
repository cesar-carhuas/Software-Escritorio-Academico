from PyQt5 import QtWidgets, uic
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QWidget
# from VISTA.ventanaPrincipal import VentanaPrincipal
from Controlador.conexion import registro_datos


class historial(QtWidgets.QMainWindow):
    def __init__(self, previous_window=None):
        super(historial, self).__init__(previous_window)
        uic.loadUi("UI/historial.ui", self)
        self.datos = registro_datos()
        self.show()

        self.previous_window = previous_window
        self.btnvolver.clicked.connect(self.volver)
        self.btneliminar.clicked.connect(self.eliminar)
        self.btnmodificar.clicked.connect(self.modificar)
        self.cargar_datos()

    def volver(self):
        self.close()
        if self.previous_window:
            self.previous_window.show()

    def cargar_datos(self):
        cur = self.datos.conexion.cursor()
        cur.execute("SELECT * FROM historial")

        resultados = cur.fetchall()

        self.tblistar.setRowCount(len(resultados))
        self.tblistar.setColumnCount(6)

        for fila, datos in enumerate(resultados):
            for columna, dato in enumerate(datos):
                if dato is not None:
                    dato = str(dato)
                    if columna in (4, 5):
                        dato = f"S/ {dato}"
                item = QtWidgets.QTableWidgetItem(dato)
                self.tblistar.setItem(fila, columna, item)

    def eliminar(self):
        fila_seleccionada = self.tblistar.currentRow()
        if fila_seleccionada >= 0:
            id_ingreso = self.tblistar.item(fila_seleccionada, 0).text()
            cur = self.datos.conexion.cursor()
            cur.execute(
                "DELETE FROM historial WHERE idingreso = %s", (id_ingreso,))
            self.datos.conexion.commit()
            self.cargar_datos()

    def modificar(self):
        fila_seleccionada = self.tblistar.currentRow()
        if fila_seleccionada >= 0:
            id_ingreso = self.tblistar.item(fila_seleccionada, 0).text()

            # Modificar la fecha
            nueva_fecha, ok = QtWidgets.QInputDialog.getText(
                self, 'Modificar fecha', 'Nueva fecha (YYYY-MM-DD):', text=self.tblistar.item(fila_seleccionada, 1).text())
            if ok:
                # Realizar la modificación en la base de datos
                cur = self.datos.conexion.cursor()
                cur.execute(
                    "UPDATE historial SET fecha = %s WHERE idingreso = %s", (nueva_fecha, id_ingreso))
                self.datos.conexion.commit()
                self.cargar_datos()

            # Modificar el tipo
            nuevo_tipo, ok = QtWidgets.QInputDialog.getText(
                self, 'Modificar tipo', 'Nuevo tipo:', text=self.tblistar.item(fila_seleccionada, 2).text())
            if ok:
                cur = self.datos.conexion.cursor()
                cur.execute(
                    "UPDATE historial SET tipo = %s WHERE idingreso = %s", (nuevo_tipo, id_ingreso))
                self.datos.conexion.commit()
                self.cargar_datos()

            # Modificar el nombre
            nuevo_nombre, ok = QtWidgets.QInputDialog.getText(
                self, 'Modificar nombre', 'Nuevo nombre:', text=self.tblistar.item(fila_seleccionada, 3).text())
            if ok:
                cur = self.datos.conexion.cursor()
                cur.execute(
                    "UPDATE historial SET nombre = %s WHERE idingreso = %s", (nuevo_nombre, id_ingreso))
                self.datos.conexion.commit()
                self.cargar_datos()

            # Modificar la salida
            salida_actual_texto = self.tblistar.item(
                fila_seleccionada, 4).text()
            # Extraer el valor numérico real eliminando el símbolo 'S/. '
            salida_actual_valor = float(salida_actual_texto.replace(
                'S/. ', '')) if salida_actual_texto.startswith('S/. ') else None

            if salida_actual_valor is not None:
                nueva_salida, ok = QtWidgets.QInputDialog.getDouble(
                    self, 'Modificar salida', 'Nueva salida:', value=salida_actual_valor)
            else:
                nueva_salida, ok = QtWidgets.QInputDialog.getDouble(
                    self, 'Modificar salida', 'Nueva salida:')

            if ok:
                cur = self.datos.conexion.cursor()
                cur.execute(
                    "UPDATE historial SET salida = %s WHERE idingreso = %s", (nueva_salida, id_ingreso))
                self.datos.conexion.commit()
                self.cargar_datos()

            # Modificar la entrada
            entrada_actual_texto = self.tblistar.item(
                fila_seleccionada, 5).text()
            # Extraer el valor numérico real eliminando el símbolo 'S/. '
            entrada_actual_valor = float(entrada_actual_texto.replace(
                'S/. ', '')) if entrada_actual_texto.startswith('S/. ') else None

            if entrada_actual_valor is not None:
                nueva_entrada, ok = QtWidgets.QInputDialog.getDouble(
                    self, 'Modificar entrada', 'Nueva entrada:', value=entrada_actual_valor)
            else:
                nueva_entrada, ok = QtWidgets.QInputDialog.getDouble(
                    self, 'Modificar entrada', 'Nueva entrada:')

            if ok:
                cur = self.datos.conexion.cursor()
                cur.execute(
                    "UPDATE historial SET entrada = %s WHERE idingreso = %s", (nueva_entrada, id_ingreso))
                self.datos.conexion.commit()
                self.cargar_datos()
