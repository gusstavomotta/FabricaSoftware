import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtWidgets import QWidget, QGridLayout, QLineEdit

class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.btn = QPushButton('Clique aqui')
        self.btn.setStyleSheet('font-size: 20px;')
        self.grid.addWidget(self.btn,  0, 0, 1, 1)

        self.btn.clicked.connect(self.acao)

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 5, 5)

        self.setCentralWidget(self.cw)

    def acao(self):
        self.display.setText('Botão clicado')

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec()