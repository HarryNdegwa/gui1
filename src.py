import sys

from PyQt5.QtWidgets import QApplication,QLabel,QWidget # installing required widgets

app = QApplication(sys.argv)

window = QWidget() # create the top level window

window.setWindowTitle("PyQT5 basics") # set window title

window.setGeometry(100, 100, 280, 280)

window.move(0,0) # relative to the top left corner of the parent(0,0)

helloMsg = QLabel("<h1>Helloo</h1>",parent=window)

helloMsg.move(60,15)

window.show()

if __name__ == "__main__":
    sys.exit(app.exec_())
