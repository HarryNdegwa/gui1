import sys

from PyQt5.QtWidgets import QWidget,QMessageBox,QLabel,QVBoxLayout,QApplication
from PyQt5.QtSql import QSqlDatabase


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,200,200)
        self.setWindowTitle("Test DB connections")
        con = QSqlDatabase.addDatabase("QSQLITE")
        con.setDatabaseName("test.sqlite")
        if not con.open():
            QMessageBox.critical(None,"Test,Error!",f"Database error {con.lastError().databaseText()}")
            sys.exit(1)
        self.setLayout(self.createLayout())


    def createLayout(self):
        layout = QVBoxLayout()
        label = QLabel(text="Welcome, you made it!")
        layout.addWidget(label)
        return layout


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

