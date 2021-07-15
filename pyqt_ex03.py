## QT5 사용자 윈도우 구성 예제
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

#윈도우 클래스 선언
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #C#의 this와 같다.
        self.setWindowTitle("My QT5 Window") # 제목표시줄
        self.setGeometry(500, 300, 800, 600)# x, y, width, height
        self.setWindowIcon(QIcon('IOT-embeded-RasberryPi/image/chart.png'))
        
        #label add
        self.label=QLabel('메시지: ',self)
        self.label.move(10,10)
        self.label.setFixedWidth(300)
        #button add
        self.btn = QPushButton('Click',self)
        self.btn.move(10,50)

        #signal add
        self.btn.clicked.connect(self.btn_clicked)
        
    #버튼 클릭 시그널(이벤트)
    def btn_clicked(self):
        self.label.clear()
        self.label.setText('메시지: 버튼클릭!!')


app = QApplication(sys.argv)

label=QLabel("Hello QT5")
label.show()

win=MyWindow()
win.show()
app.exec_()