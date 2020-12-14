import sys

from PyQt5.QtWidgets import QDialog,QFormLayout,QApplication,QLineEdit,QDialogButtonBox,QVBoxLayout,QWidget

class MyDialog(QDialog):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setWindowTitle("MyDialog")
        self.setGeometry(200,200,200,200)
        self.mainLayout = QVBoxLayout()

        self.mainLayout.addWidget(self.setUpForm())

        btns = QDialogButtonBox()

        btns.setStandardButtons(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        self.mainLayout.addWidget(btns)

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




if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MyDialog()

    window.show()

    sys.exit(app.exec())
