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
        # self.secureInsertToContact()
        self.fetchContactRecords()


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

    

    def secureInsertToContact(self):
        query = QSqlQuery()
        query.prepare("""
             INSERT INTO contacts (
                name,
                job,
                email
            )
            VALUES (?, ?, ?)
        """)

        data = [
            ("Joe", "Senior Web Developer", "joe@example.com"),
            ("Lara", "Project Manager", "lara@example.com"),
            ("David", "Data Analyst", "david@example.com"),
            ("Jane", "Senior Python Developer", "jane@example.com"),
        ]

        for name,job,email in data:
            query.addBindValue(name)
            query.addBindValue(job)
            query.addBindValue(email)
            query.exec()

    def fetchContactRecords(self):
        query = QSqlQuery()
        query.exec("SELECT id,name, job, email FROM contacts")
        while query.next():
            id,name,job,email = range(4)
            data = f"{query.value(id)}->{query.value(name)}->{query.value(job)}->{query.value(email)}"
            print(data)
        query.finish()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


