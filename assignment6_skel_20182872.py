import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication, QLabel, QComboBox, QTextEdit, QLineEdit, QGridLayout)
from PyQt5.QtCore import Qt

class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()

    def initUI(self):
        name = QLabel('Name: ')
        age = QLabel('Age: ')
        score = QLabel('Score: ')
        key = QLabel('Key: ')
        result = QLabel('Result: ')
        amount = QLabel("AMount: ")
        # label widget 만들기

        self.nameEdit = QLineEdit()
        self.ageEdit = QLineEdit()
        self.scoreEdit = QLineEdit()
        self.amountEdit = QLineEdit()
        self.keyEdit = QComboBox()
        # seif를 안붙이면 텍스트 함수로 내용읽어오기 못함.
        self.keyEdit.addItem('Name')
        self.keyEdit.addItem('Age')
        self.keyEdit.addItem('Score')
        # keyEdit 객체에 아이템을 추가하는 함수 'addItem()' 사용

        add = QPushButton('Add')
        delete = QPushButton('Del')
        find = QPushButton('Find')
        inc = QPushButton('Inc')
        show = QPushButton('Show')
        self.data = QTextEdit()
        # 버튼 위젯 만들기

        grid = QGridLayout()

        grid.setSpacing(10)
        grid.addWidget(name, 1, 0)
        grid.addWidget(self.nameEdit, 1, 1)
        grid.addWidget(age, 1, 2)
        grid.addWidget(self.ageEdit, 1, 3)
        grid.addWidget(score, 1, 4)
        grid.addWidget(self.scoreEdit, 1, 5)
        # 첫번째 줄 입력칸 만들기

        grid.addWidget(amount, 2, 2)
        grid.addWidget(self.amountEdit, 2, 3)
        grid.addWidget(key, 2, 4)
        grid.addWidget(self.keyEdit, 2, 5)
        # 두번째 줄 입력칸 만들기

        grid.addWidget(add, 3, 1)
        grid.addWidget(delete, 3, 2)
        grid.addWidget(find, 3, 3)
        grid.addWidget(inc, 3, 4)
        grid.addWidget(show, 3, 5)
        # 기능 버튼들 만들기

        grid.addWidget(result, 4, 0)
        # 결과 보여주는 창 생성하기
        grid.addWidget(self.data, 5, 0, 10, 6)

        add.clicked.connect(self.addBC)
        delete.clicked.connect(self.delBC)
        inc.clicked.connect(self.incBC)
        find.clicked.connect(self.findBC)
        show.clicked.connect(self.showScoreDB)
        # 버튼이 눌릴때마다 슬롯에 연결시키기
        self.setLayout(grid)

        self.setGeometry(600, 400, 350, 300)
        self.setWindowTitle('Assignment6')
        self.show()

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()


    def addBC(self):
        record = {'Name': self.nameEdit.text(), 'Age': int(self.ageEdit.text()), 'Score': int(self.scoreEdit.text())}
        self.scoredb += [record]
        self.showScoreDB()
    # add 버튼 클릭 시 기능 구현

    def delBC(self):
        for s in range(len(self.scoredb)):
            for p in self.scoredb:
                if p['Name'] == self.nameEdit.text():
                    self.scoredb.remove(p)
        self.showScoreDB()
    # del 버튼 클릭 시 기능 구현

    def findBC(self):
        self.findsort = []
        for p in self.scoredb:
            if p['Name'] == self.nameEdit.text():
                self.findsort += [p]
        self.findDB()
    # find 버튼 클릭 시 기능 구현

    def incBC(self):
        for p in self.scoredb:
            if p['Name'] == self.nameEdit.text():
                p['Score'] = str(int(p['Score']) + int(self.amountEdit.text()))
        self.findBC()
    # inc 버튼 클릭 시 기능 구현

    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        self.data.setText("")
        for p in sorted(self.scoredb, key=lambda person: person[self.keyEdit.currentText()]):
            for attr in sorted(p):
                self.data.insertPlainText(attr + "=" + str(p[attr]) + "\t")
                if(attr == 'Score'):
                    self.data.insertPlainText('\n')

    def findDB(self):
        self.data.setText("")
        for p in sorted(self.findsort, key=lambda person: person[self.keyEdit.currentText()]):
            for attr in sorted(p):
                self.data.insertPlainText(attr + "=" + str(p[attr]) + "\t")
                if (attr == 'Score'):
                    self.data.insertPlainText('\n')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
