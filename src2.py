import sys

from PyQt5.QtWidgets import QDialog,QFormLayout,QApplication,QLineEdit,QDialogButtonBox,QVBoxLayout,QWidget

app = QApplication(sys.argv)

class MyDialog(QDialog):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setWindowTitle("MyDialog")
        self.setGeometry(200,200,200,200)
        self.mainLayout = QVBoxLayout()

        self.mainLayout.addWidget(self.setUpForm())

        self.setLayout(self.mainLayout)


    def setUpForm(self):
        formWidget = QWidget()
        formLayout = QFormLayout()
        formLayout.addRow("Name :",QLineEdit())
        formLayout.addRow("Email :",QLineEdit())
        formLayout.addRow("Phone :",QLineEdit())
        formLayout.addRow("City :",QLineEdit())
        formWidget.setLayout(formLayout)
        return formWidget




window = MyDialog()

window.show()

if __name__ == "__main__":
    sys.exit(app.exec_())
