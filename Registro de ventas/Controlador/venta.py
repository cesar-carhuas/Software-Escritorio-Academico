class venta():
    __codigo = ""
    __descripcion = ""
    __precio = 0.0
    __cantidad = 0

    def __init__(self, codigo, descripcion, precio, cantidad):
        self.__codigo = codigo
        self.__descripcion = descripcion
        self.__precio = precio
        self.__cantidad = cantidad

    def getcodigo(self):
        return self.__codigo

    def getdescripcion(self):
        return self.__descripcion

    def getprecio(self):
        return self.__precio

    def getcantidad(self):
        return self.__cantidad

    def setcodigo(self, codigo):
        self.__codigo = codigo

    def setdescripcion(self, descripcion):
        self.__descripcion = descripcion

    def setprecio(self, precio):
        self.__precio = precio

    def setcantidad(self, cantidad):
        self.__cantidad = cantidad
