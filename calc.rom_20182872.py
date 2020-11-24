from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout

from keypad2 import numPadList, operatorList, constantList, functionList
from calcFunctions import factorial, decToBin, binToDec, decToRoman, romanToDec

class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 25)
        size.setWidth(max(size.width(), size.height()))
        return size


class Calculator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Display Window
        self.display = QLineEdit('')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(25)

        numLayout = QGridLayout()
        opLayout = QGridLayout()
        conLayout = QGridLayout()
        funLayout = QGridLayout()

        buttonGroups = {
            'num': {'buttons': numPadList, 'layout': numLayout, 'columns': 3},
            'op': {'buttons': operatorList, 'layout': opLayout, 'columns': 2},
            'con': {'buttons': constantList, 'layout': conLayout, 'columns': 1},
            'fun': {'buttons': functionList, 'layout': funLayout, 'columns': 1},
        }
        # 사전하나와 for문으로 버튼배열

        self.functiondic = {'factorial (!)': factorial, '-> binary': decToBin,
                            'binary -> dec': binToDec, '-> roman': decToRoman, 'roman -> dec': romanToDec}

        self.constantdic = {'pi': 3.141592, '빛의 이동 속도 (m/s)': 3E+8,
                            '소리의 이동 속도 (m/s)': 340,
                            '태양과의 평균 거리 (km)': 1.5E+8}

        # buttonGroups 가지고 버튼들의 위치배정.
        for label in buttonGroups.keys():
            r = 0
            c = 0
            buttonPad = buttonGroups[label]
            for buttontext in buttonPad['buttons']:
                button = Button(buttontext, self.buttonClicked)
                buttonPad['layout'].addWidget(button, r, c)
                c += 1
                if c >= buttonPad['columns']:
                    c = 0
                    r += 1

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addWidget(self.display, 0, 0, 1, 2)
        mainLayout.addLayout(numLayout, 1, 0)
        mainLayout.addLayout(opLayout, 1, 1)
        mainLayout.addLayout(conLayout, 2, 0)
        mainLayout.addLayout(funLayout, 2, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle("My Calculator")
        # = 버튼이 눌렸는지 확인하기 위한 변수.
        self.equalPressed = False

    def buttonClicked(self):
        button = self.sender()
        key = button.text()  # 눌린버튼이름
        txt = self.display.text()
        operator = ['*', '+', '-', '/', '.']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        # 에러메시지 뜬 상태로 아무버튼 누르면 리셋.
        if txt == 'error':
            self.display.setText('')

        # = 눌리면 창에입력된 연산 실행하고 결과창에표시
        elif key == '=':
            try:
                # 예외처리..
                result = str(eval(txt))
                self.display.setText(result)
                # equalPressed가 True인 상태에선 앞에 숫자가있을때 숫자를 못누름
                self.equalPressed = True
            except:
                self.display.setText('error')

        elif key == 'C':
            self.display.setText("")
            # 초기화 하면서 equalPressed도 다시 False로 초기화.
            self.equalPressed = False
        # 함수버튼 클릭
        elif key in functionList:
            n = txt
            self.display.setText(self.functiondic[key](n))
        # 상수버튼 클릭
        elif key in constantList:
            self.display.setText(txt + str(self.constantdic[key]))
        # 연산자 클릭
        elif key in operator:
            # 처음부터 연산기호를 입력하려 할때
            if txt == '':
                pass

            # 연산기호를 두번연속 누르려 할때
            elif txt[-1] in operator:
                # *와 /만 2번연속으로 입력되는것은 허용함. (3번은불가능)
                if txt[-1] in ['*', '/'] and txt[-2] != txt[-1] and key == txt[-1]:
                    self.display.setText(txt + key)
                # 나머지는 안돼
                else:
                    pass
            # 숫자뒤에 연산기호 누르려할때.(정상동작)
            else:
                self.display.setText(txt + key)
                # 만약 = 버튼 누른뒤에 연산기호를 입력했다면. equalPressed를 False로 초기화해야함
                # 그렇지않으면 = 누르고 연산기호 누르고 나서 숫자를 2개이상 쓸수없음
                self.equalPressed = False

        elif key in numbers:
            # = 이 눌리고 난 바로뒤엔 숫자부터 쓸수없음 (append안되야함)
            if self.equalPressed == True:
                pass
            else:
                self.display.setText(txt + key)
        elif key == "(":
            # 1.빈 창일때 입력 가능
            # 2.연산기호뒤에, 또는 "(" 뒤에 입력가능
            # 3.단, "."뒤에는 입력불가
            if txt == '' or txt[-1] == "(" or (txt[-1] in operator and txt[-1] != '.'):
                self.display.setText(txt + key)
        elif key == ")":
            # 2.( ) 를 연달아 입력할수 없음
            # 3.연산기호 뒤에 쓸수 없음.
            # 4.입력창에 있는" ( "의 개수를 넘을 수 없음

            # 입력창에 있는 ( 의 갯수
            count_1 = 0
            # 입력창에 있는 ) 의 갯수
            count_2 = 0
            for i in range(len(txt)):
                if txt[i] == "(":
                    count_1 += 1
            for i in range(len(txt)):
                if txt[i] == ")":
                    count_2 += 1

            if txt[-1] != "(" and txt[-1] not in operator and count_1 > count_2:
                self.display.setText(txt + key)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())