from PyQt5.QtWidgets import QPushButton,QVBoxLayout


class MyVLayout(QVBoxLayout):

    def add_widgets(self):
        self.addWidget(QPushButton(text="Button1"))
        self.addWidget(QPushButton(text="Button2"))
        self.addWidget(QPushButton(text="Button3"))
        self.addWidget(QPushButton(text="Button4"))

    