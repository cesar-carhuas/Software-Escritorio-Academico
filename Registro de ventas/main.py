# import sys
# from PyQt5 import QtWidgets
# from Vista.ventanaventa import ventanaventa

# if __name__ == 'main__':
#     app = QtWidgets.QApplication(sys.argv)
#     window = ventanaventa()
#     app.exec_()

from PyQt5.QtWidgets import QApplication
from Vista.ventanaventa import ventanaventa

if __name__ == '__main__':
    app = QApplication([])
    Window = ventanaventa()
    app.exec()
