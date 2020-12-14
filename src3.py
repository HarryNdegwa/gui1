import sys

from PyQt5.QtWidgets import QMainWindow,QApplication,QToolBar,QStatusBar,QLabel

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window App")
        self.setGeometry(100,100,800,500)
        self._createMenu()
        self.setCentralWidget(QLabel(text="Central widget..."))
        self._createToolBar()
        self._createStatusBar()

    def _createMenu(self):
        self.menu = self.menuBar()
        self.menu.addMenu("&Menu")
        self.menu.addAction("&Greeting",self.greeting)
        self.menu.addAction("&Exit",self.close)

    def _createToolBar(self):
        toolBar = QToolBar()
        self.addToolBar(toolBar)
        toolBar.addAction("Exit",self.close)


    def _createStatusBar(self):
        statusBar = QStatusBar()
        self.setStatusBar(statusBar)
        statusBar.showMessage("I am the fucking status bar!")

    def greeting(self):
        print("Helloo World")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())