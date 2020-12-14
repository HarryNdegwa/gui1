from PyQt5.QtWidgets import QVBoxLayout,QFormLayout,QLineEdit,QPushButton
from functools import partial

class MyCentralLayout(QVBoxLayout):

    def __init__(self):
        super().__init__()
        self.addLayout(self.create_form())
        self.button = QPushButton("Submit")
        self.button.clicked.connect(partial(self.button_click_handler,"Helloo"))
        self.addWidget(self.button)


    def create_form(self):
        self.form = QFormLayout()
        self.form.addRow("name:",QLineEdit())
        return self.form

    def button_click_handler(self,text):
        print(text)