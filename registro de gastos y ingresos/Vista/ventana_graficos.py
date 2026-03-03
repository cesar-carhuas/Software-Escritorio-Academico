from PyQt5 import QtWidgets, uic
from Controlador.conexion import registro_datos
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np


class graficos(QtWidgets.QMainWindow):
    def __init__(self, previous_window=None):
        super(graficos, self).__init__(previous_window)
        uic.loadUi("UI/graficos.ui", self)
        self.datos = registro_datos()
        self.show()

        self.crear_grafico_barra()
        self.crear_grafico_lineal()
        self.crear_grafico_area()
        self.crear_grafico_circular()

        self.previous_window = previous_window
        self.btnvolver.clicked.connect(self.volver)

    def volver(self):
        self.close()
        if self.previous_window:
            self.previous_window.show()

    def recuperar_datos(self):
        cur = self.datos.conexion.cursor()
        cur.execute("SELECT entrada, salida FROM historial")
        datos = cur.fetchall()
        cur.close()
        return datos

    def crear_grafico_barra(self):
        datos = self.recuperar_datos()
        entradas = [d[0] for d in datos]
        salidas = [d[1] for d in datos]

        figura = Figure()
        eje = figura.add_subplot(111)
        eje.bar(np.arange(len(entradas)), entradas, label='Entrada')
        eje.bar(np.arange(len(salidas)), salidas, label='Salida', alpha=0.5)
        eje.set_ylabel('Cantidad')
        eje.legend()

        canvas = FigureCanvas(figura)
        layout = QtWidgets.QVBoxLayout(self.grafico_uno)
        layout.addWidget(canvas)

    def crear_grafico_lineal(self):
        datos = self.recuperar_datos()
        entradas = [d[0] for d in datos]
        salidas = [d[1] for d in datos]

        figura = Figure()
        eje = figura.add_subplot(111)
        eje.plot(np.arange(len(entradas)), entradas, label='Entrada')
        eje.plot(np.arange(len(salidas)), salidas, label='Salida')
        eje.set_ylabel('Cantidad')
        eje.legend()

        canvas = FigureCanvas(figura)
        layout = QtWidgets.QVBoxLayout(self.grafico_dos)
        layout.addWidget(canvas)

    def crear_grafico_area(self):
        datos = self.recuperar_datos()
        entradas = [d[0] for d in datos]
        salidas = [d[1] for d in datos]

        figura = Figure()
        eje = figura.add_subplot(111)
        eje.fill_between(np.arange(len(entradas)), entradas,
                         color='skyblue', alpha=0.5, label='Entrada')
        eje.fill_between(np.arange(len(salidas)), salidas,
                         color='orange', alpha=0.5, label='Salida')
        eje.set_ylabel('Cantidad')
        eje.legend()

        canvas = FigureCanvas(figura)
        layout = QtWidgets.QVBoxLayout(self.grafico_tres)
        layout.addWidget(canvas)

    def crear_grafico_circular(self):
        datos = self.recuperar_datos()
        entradas_totales = sum(d[0] for d in datos)
        salidas_totales = sum(d[1] for d in datos)
        sizes = [entradas_totales, salidas_totales]
        labels = ['Entradas', 'Salidas']

        figura = Figure()
        eje = figura.add_subplot(111)
        eje.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        eje.axis('equal')

        canvas = FigureCanvas(figura)
        layout = QtWidgets.QVBoxLayout(self.grafico_cuatro)
        layout.addWidget(canvas)
