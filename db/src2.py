import sys

from PyQt5.QtWidgets import (QApplication,QMainWindow,QMessageBox,QTableWidgetItem,QTableWidget)
from PyQt5.QtSql import QSqlDatabase,QSqlQuery


class MainWindow(QMainWindow):

    def __init__(self,parent=None):
        super().__init__(parent)
        self.setGeometry(100,100,400,400)
        self.setWindowTitle("Database GUI App")
        self.createDbConnection()
        self.createEmployeeTable()


    def createDbConnection(self):
        self.con = QSqlDatabase.addDatabase("QSQLITE")
        self.con.setDatabaseName("test2.sqlite")
        if not self.con.open():
            QMessageBox.critical(None,"Database Error!",f"{con.lastError().databaseText()}")
            sys.exit()

    def checkIfTableExists(self,tableName):
        tables = self.con.tables()
        return tableName in tables


    def createEmployeeTable(self):
        if not self.checkIfTableExists("employee"):
            queryString = """
                CREATE TABLE employee (
                    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                    name VARCHAR(40) NOT NULL,
                    job VARCHAR(50),
                    email VARCHAR(40) NOT NULL,
                    phone VARCHAR(20),
                    age INTEGER
                )
            """
            query = QSqlQuery()
            query.exec(queryString)

    
    def createCentralWidget(self):
        self.view = QTableWidget()
        self.view.setColumnCount(6)
        self.view.setHorizontalHeaderLabels(["ID", "Name", "Job", "Email","Phone","Age"])
        query = QSqlQuery("SELECT id, name, job, email,phone,age FROM employee")





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
