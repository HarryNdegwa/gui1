from PyQt5.QtWidgets import QPushButton,QHBoxLayout

class MyHLayout(QHBoxLayout):

    def add_widgets(self):
        self.addWidget(QPushButton(text="Button1"))
        self.addWidget(QPushButton(text="Button2"))
        self.addWidget(QPushButton(text="Button3"))
        self.addWidget(QPushButton(text="Button4"))
