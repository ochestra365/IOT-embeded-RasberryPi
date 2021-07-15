## QT5 베이스 프레임 소스
import sys
from PyQt5.QtWidgets import *

#윈도우 클래스 선언
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

app = QApplication(sys.argv)

#button=QPushButton("Click me")
#button.show()#C#의 모든 클래스의 부모는 object이다. 
#모든 위젯들의 부모는 Qwidget이다. 이것을 상속받아서 만들었다.
# 클릭이벤트를 만들어서 작성하기 전에 내용들을 작성해줘야 한다. 위젯들이 어떤 게 있는 지 확인필
label=QLabel("Hello QT5")
label.show()
win=MyWindow()
win.show()
app.exec_()