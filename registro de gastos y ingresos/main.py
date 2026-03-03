from PyQt5.QtWidgets import QApplication
from Vista.login import login

if __name__ == '__main__':
    app = QApplication([])
    Window = login()
    app.exec()
