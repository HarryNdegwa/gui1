import sys

from PyQt5.QtWidgets import QApplication,QLabel,QWidget # installing required widgets

from layouts.hLayout import MyHLayout

app = QApplication(sys.argv)

class MainWindow(QWidget):

    def __init__(self,layout,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setWindowTitle("Layouts")
        self.setGeometry(100,100,500,500)
        self.setLayout(layout)

hLayout = MyHLayout()

hLayout.add_widgets()

window = MainWindow(hLayout)

window.show()



if __name__ == "__main__":
    sys.exit(app.exec_())
