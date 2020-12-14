from PyQt5.QtWidgets import QFormLayout,QLineEdit

class MyFormLayout(QFormLayout):

    def add_widgets(self):
        self.addRow("Name : ",QLineEdit())
        self.addRow("Email : ",QLineEdit())
        self.addRow("Subject : ",QLineEdit())
        self.addRow("Message : ",QLineEdit())
