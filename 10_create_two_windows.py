import sys
from PySide2.QtGui import *
from PySide2.QtCore import SIGNAL
from PySide2.QtWidgets import QLineEdit, QLabel, QDialog, QGridLayout, QPushButton, QMessageBox, QApplication, QWidget, QVBoxLayout

class W1(QWidget):
    def __init__(self, parent=None):
        super(W1, self).__init__(parent)
        self.btn = QPushButton('Click1')

        vb = QVBoxLayout()
        vb.addWidget(self.btn)
        self.setLayout(vb)

        self.btn.clicked.connect(self.fireupWindows2)

    def fireupWindows2(self):
        self.w3 = W3()    
        self.w3.show()
class W3(QWidget):
    def __init__(self, parent=None):
        super(W3, self).__init__(parent)
        self.resize(300, 300)
        self.btn = QLabel('The Last Window')

        vb = QVBoxLayout()
        vb.addWidget(self.btn)
        self.setLayout(vb)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = W1()
    w.show()
    sys.exit(app.exec_())
