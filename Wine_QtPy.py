# 조건을 입력하면 와인을 추천해주는 GUI 설계

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from wine_filter_function import MyWines #필터링 함수 불러옴


###### 키워드 검색 창
class SearchDialog(QDialog):

    def __init__(self):
        super().__init__()
        self.setupUI()
        # 입력받을 변수들 초기화
        self.food = None     #메인 메뉴의 종류
        self.price = None    #가격대
        self.rate = None     #평점
        self.celeb = None    #기념일 여부

    def setupUI(self):
        #기본적인 레이아웃 설정
        self.setGeometry(1100, 200, 400, 400)
        self.setWindowTitle("원하는 와인의 조건을 입력하세요.")
        self.setWindowIcon(QIcon("wine.png"))

        # 입력받을 변수들을 위한 라벨
        label1 = QLabel("메인 메뉴 종류: ")
        label2 = QLabel("가격대 선택: ")
        label3 = QLabel("최소 평점: ")
        label4 = QLabel("기념일 여부: ")

        # 변수를 입력할 창/버튼의 종류 설정
        self.lineEdit1 = QLineEdit() #메인 메뉴
        self.lineEdit2 = QLineEdit() #가격대
        self.lineEdit3 = QLineEdit() #평점
        self.lineEdit4 = QLineEdit() #기념일
        self.lineEdit5 = QLineEdit() #비선호

        self.pushButton1 = QPushButton("검색") #검색 버튼 클릭
        self.pushButton1.clicked.connect(self.pushButtonClicked)

        #화면 레이아웃 설정
        layout = QGridLayout()

        layout.addWidget(label1,0,0)
        layout.addWidget(self.lineEdit1,0,1)

        layout.addWidget(label2,1,0)
        layout.addWidget(self.lineEdit2,1,1)

        layout.addWidget(label3,2,0)
        layout.addWidget(self.lineEdit3,2,1)

        layout.addWidget(label4,3,0)
        layout.addWidget(self.lineEdit4,3,1)

        layout.addWidget(self.pushButton1,5,1)
        self.setLayout(layout)

    def pushButtonClicked(self):
        self.food = self.lineEdit1.text()
        self.price = self.lineEdit2.text()
        self.rate = self.lineEdit3.text()
        self.celeb = self.lineEdit4.text()

        self.close()

class MyWindow(QWidget): #처음 띄울 창(검색 시작하기)
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self): #화면 구조 설계
        self.setGeometry(800, 200, 600, 400)
        self.setWindowTitle("와인 추천 프로그램 v0.1")
        self.setWindowIcon(QIcon('wine.png'))

        self.pushButton = QPushButton("와인 추천받기")
        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.pushButton)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def pushButtonClicked(self):
        #와인필터링함수 임포트 혹은 작성
        dlg = SearchDialog()
        dlg.exec_()
        #와인추천받는코드
        food = str(dlg.food)
        price = str(dlg.price)
        rate = int(dlg.rate)
        celeb = str(dlg.celeb)
        mywines5 = MyWines(food, price, rate, celeb)
        #결과 보여줄 코드
        self.label.setText('**조건에 맞게 검색한 결과**\n\n{}'.format(mywines5))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()