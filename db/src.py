import sys

from PyQt5.QtWidgets import QWidget,QMessageBox,QLabel,QVBoxLayout,QApplication
from PyQt5.QtSql import QSqlDatabase,QSqlQuery


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,200,200)
        self.setWindowTitle("Test DB connections")
        self.con = QSqlDatabase.addDatabase("QSQLITE")
        self.con.setDatabaseName("test.sqlite")
        if not self.con.open():
            QMessageBox.critical(None,"Test,Error!",f"Database error {self.con.lastError().databaseText()}")
            sys.exit(1)


        self.setLayout(self.createLayout())
        self.createContactTable()


    def createLayout(self):
        layout = QVBoxLayout()
        label = QLabel(text="Welcome, you made it!")
        layout.addWidget(label)
        return layout

    def checkIfTableExists(self,tableName):
        tables = self.con.tables()
        return tableName in tables

    def createContactTable(self):
        createTableQuery = QSqlQuery()
        if not self.checkIfTableExists("contacts"):
            createTableQuery.exec(
                """
                CREATE TABLE contacts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                    name VARCHAR(40) NOT NULL,
                    job VARCHAR(50),
                    email VARCHAR(40) NOT NULL
                )
                """
            )

        

    def insertContact(self):
        name = "Harrison Ndegwa"
        job = "Lead Developer"
        email = "harrisonndegwa65@gmial.com"

        queryString = f"""
            INSERT INTO contacts (name,job,email) VALUES ('{name}','{job}','{email}')
        """

        query = QSqlQuery()
        query.exec(queryString)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


