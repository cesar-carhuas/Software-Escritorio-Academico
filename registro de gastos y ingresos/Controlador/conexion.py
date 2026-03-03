import mysql.connector


class registro_datos():
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host='localhost', database='restaurante', user='root', password='1234')

    def buscar_user(self, usuario):
        cur = self.conexion.cursor()
        # {} .format(usuario)
        sql = "SELECT * FROM empleado WHERE usuario = %s"
        cur.execute(sql, (usuario,))
        usersx = cur.fetchall()
        cur.close()
        return usersx

    def busca_pass(self, password):
        cur = self.conexion.cursor()
        # {} .format(password)
        sql = "SELECT * FROM empleado WHERE contraseña = %s"
        cur.execute(sql, (password, ))
        passwordx = cur.fetchall()
        cur.close()
        return passwordx
