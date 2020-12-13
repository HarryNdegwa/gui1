import sys

from PyQt5.QtWidgets import QApplication,QLabel,QWidget

app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("PyQT5 basics")

window.setGeometry(100, 100, 280, 280)

window.move(0,0)

helloMsg = QLabel("<h1>Helloo</h1>",parent=window)

helloMsg.move(60,15)

window.show()

if __name__ == "__main__":
    sys.exit(app.exec_())
