import sys

from PyQt5.QtWidgets import QApplication,QLabel,QWidget,QGridLayout # installing required widgets

from layouts.hLayout import MyHLayout
from layouts.vLayout import MyVLayout

app = QApplication(sys.argv)

class MainWindow(QWidget):

    def __init__(self,layout,layout2,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setWindowTitle("Layouts")
        self.setGeometry(100,100,500,500)
        self.mainLayout = QGridLayout()
        self.setLayout(self.mainLayout)
        myWidget = QWidget()
        myWidget.setLayout(layout)
        self.mainLayout.addWidget(myWidget,0,0)
        myWidget2 = QWidget()
        myWidget2.setLayout(layout2)
        self.mainLayout.addWidget(myWidget2,0,1)
        # self.mainLayout.addWidget(QLabel(text="Helooo"),0,0)

    # def add_layouts(self,left_layout,right_layout):
    #     self.add_left_layout(left_layout)
    #     self.add_right_layout(right_layout)

    # def add_left_layout(self,layout):
    #     self.mainLayout.addWidget(layout,0,0)


    # def add_right_layout(self,layout):
    #     self.mainLayout.addWidget(layout,0,1)




hLayout = MyHLayout()

hLayout.add_widgets()


vLayout = MyVLayout()

vLayout.add_widgets()


window = MainWindow(vLayout,hLayout)

# window.add_layouts(vLayout,hLayout)

window.show()



if __name__ == "__main__":
    sys.exit(app.exec_())
