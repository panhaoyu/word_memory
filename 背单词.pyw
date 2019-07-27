from lib.application import Window
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
widget = Window()
widget.show()
sys.exit(app.exec_())
