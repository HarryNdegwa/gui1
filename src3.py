import sys

from PyQt5.QtWidgets import QMainWindow,QApplication

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window App")
        self.setGeometry(100,100,800,800)
        self._createMenu()

    def _createMenu(self):
        self.menu = self.menuBar()
        self.menu.addMenu("&Menu")
        self.menu.addAction("&Exit",self.close)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())