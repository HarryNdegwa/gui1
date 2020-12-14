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
        self.addTestData()
        self.createCentralWidget()


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

    def addTestData(self):
        data = [
            ("Harrison", "Senior Back-End Developer", "harrisonndegwa65@gmail.com","0799204524",22),
            ("Joe", "Senior Front-End Developer", "joe@example.com","0799001654",21),
            ("Lara", "Project Manager", "jlara@example.com","0710204524",25),
            ("David", "Data Analyst", "david@example.com","0799204500",24),
            ("Jane", "Senior Python Developer", "jane@example.com","0799200520",23),
        ]

        query = QSqlQuery()
        query.prepare("""
            INSERT INTO employee (
                name,
                job,
                email,
                phone,
                age
            )
            VALUES (?, ?, ?, ?, ?)
        """)

        for name,job,email,phone,age in data:
            query.addBindValue(name)
            query.addBindValue(job)
            query.addBindValue(email)
            query.addBindValue(phone)
            query.addBindValue(age)
            query.exec()

    
    def createCentralWidget(self):
        self.view = QTableWidget()
        self.view.setColumnCount(6)
        self.view.setHorizontalHeaderLabels(["ID", "Name", "Job", "Email","Phone","Age"])
        
        employeesData = self.fetchEmployees()

        while employeesData.next():
            rows = self.view.rowCount()
            self.view.setRowCount(rows+1)
            self.view.setItem(rows,0,QTableWidgetItem(str(employeesData.value(0))))
            self.view.setItem(rows,1,QTableWidgetItem(employeesData.value(1)))
            self.view.setItem(rows,2,QTableWidgetItem(employeesData.value(2)))
            self.view.setItem(rows,3,QTableWidgetItem(employeesData.value(3)))
            self.view.setItem(rows,4,QTableWidgetItem(employeesData.value(4)))
            self.view.setItem(rows,5,QTableWidgetItem(str(employeesData.value(5))))
        self.view.resizeColumnsToContents()
        self.setCentralWidget(self.view)

    
    def fetchEmployees(self):
        self.employeesQuery = QSqlQuery()
        self.employeesQuery.exec("SELECT id, name, job, email,phone,age FROM employee")
        return self.employeesQuery





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
