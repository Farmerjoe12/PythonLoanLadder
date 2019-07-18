import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

from model.Loan import Loan
from model.RepaymentSchedule import RepaymentSchedule
from view.AmortizationView import AmortizationView


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "Window"
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.statusBar().showMessage('Message in statusbar.')

        button = QPushButton('Button', self)
        button.setToolTip('This is a button')
        button.move(500,400)
        button.clicked.connect(self.on_click)
        

    def addPlot(self, plot):
        p = plot
        p.move(0,0)

    @pyqtSlot()
    def on_click(self):
        print("Button clicked")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec())