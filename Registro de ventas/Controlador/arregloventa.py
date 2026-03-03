from Controlador.venta import *


class arregloventa:
    def __init__(self):
        self.dataventas = []  # lista principal de almacenamiento de datos
        self.cargar()  # carga de archivo para la lista principal

    def adicionaVenta(self, objVen):
        self.dataventas.append(objVen)

    def devolverventa(self, pos):
        return self.dataventas[pos]

    def tamañoarregloventa(self):
        return len(self.dataventas)

    def buscarventa(self, codigo):
        for i in range(self.tamañoarregloventa()):
            if codigo == self.dataventas[i].getcodigo():
                return i
        return -1

    def eleminarventa(self, indice):
        del (self.dataventas[indice])

    def modificarVenta(self, objVen, pos):
        self.dataventas[pos] = objVen

    def retornarDatos(self):
        return self.dataventas

    def cargar(self):
        archivo = open("Modelo/venta.txt", "r", encoding="utf-8")
        for linea in archivo.readlines():
            columna = str(linea).split(",")
            codigo = columna[0]
            descripcion = columna[1]
            precio = columna[2]
            cantidad = columna[3].strip()
            objVen = venta(codigo, descripcion, precio, cantidad)
            self.adicionaVenta(objVen)
        archivo.close()

    def grabar(self):
        archivo = open("Modelo/venta.txt", "w+", encoding="utf-8")
        for i in range(self.tamañoarregloventa()):
            p = float(self.devolverventa(i).getprecio())
            c = int(self.devolverventa(i).getcantidad())
            importe = p * c
            impuesto = importe * 0.18
            total = importe + impuesto
            archivo.write(str(self.devolverventa(i).getcodigo()) + ","
                          + str(self.devolverventa(i).getdescripcion()) + ","
                          + str(self.devolverventa(i).getprecio()) + ","
                          + str(self.devolverventa(i).getcantidad()) + "\n")
        archivo.close()
