import sys

from PyQt5.QtWidgets import (QApplication,QMainWindow,QMessageBox)
from PyQt5.QtSql import QSqlDatabase,QSqlQuery


class MainWindow(QMainWindow):

    def __init__(self,parent=None):
        super().__init__(parent)
        self.setGeometry(100,100,400,400)
        self.setWindowTitle("Database GUI App")
        self.createDbConnection()


    def createDbConnection(self):
        self.con = QSqlDatabase.addDatabase("QSQLITE")
        self.con.setDatabaseName("test2.sqlite")
        if not self.con.open():
            QMessageBox.critical(None,"Database Error!",f"{con.lastError().databaseText()}")
            sys.exit()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
