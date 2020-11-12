from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout

from keypad2 import numPadList, operatorList, constantList, functionList
from calcFunctions import factorial, decToBin, binToDec

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

        self.functiondic = {'factorial (!)': factorial, '-> binary': decToBin, 'binary -> dec': binToDec}

        self.constantdic = {'pi': 3.141592, '빛의 이동 속도 (m/s)': 3E+8, '소리의 이동 속도 (m/s)': 340, '태양과의 평균 거리 (km)': 1.5E+8}
        # 밑에서 버튼이 눌렸을때 버튼이름(키)에 대응되는 함수나 상수를 키값으로 설정.

        for label in buttonGroups.keys():
            # 위에있는 사전의 키들 :label 은 num, op
            r = 0
            c = 0
            buttonPad = buttonGroups[label]
            for buttontext in buttonPad['buttons']:
                #순환
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
        self.equalPressed = False

    def buttonClicked(self):
        button = self.sender()
        key = button.text()
        txt = self.display.text()
        operator = ['*', '+', '-', '/', '.']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        if self.display.text() == 'error':
            self.display.setText('')
            # 에러메시지 뜬 상태로아무버튼 누르면 리셋
        elif key == '=':
            # = 눌리면 창에입력된 연산 실행하고 결과창에 표시
            try:
                result = str(eval(txt))
                self.display.setText(result)
                self.equalPressed = True
            except:
                self.display.setText('error')
        elif key == 'C':
            self.display.setText("")
            self.equalPressed = False
        elif key in functionList:
            # 함수 버튼 입력
            n = txt
            self.display.setText(self.functiondic[key](n))
            # 함수명은 사전에 키, 함수는 키값
        elif key in constantList:
            self.display.setText(txt + str(self.constantdic[key]))
        elif key in operator:
            if txt == '':
                # 처음부터 연산기호를 입력하지 못하도록함
                pass
            elif txt[-1] in operator:
                # 연산기호를 두번연속
                if txt[-1] in ['*', '/'] and txt[-2] != txt[-1] and key == txt[-1]:
                    self.display.setText(txt + key)
                else:
                    pass
                    # 위에있는 case들 제외, 연산기호가 연달아 눌린 경우는 안되게
            else:
                self.display.setText(txt + key)
                self.equalPressed = False
                # 한번 = 를 누른 뒤, 연산기호입력 후 숫자를 2개이상 쓸수있음 비어있지도 않고 연속도 아니면 연산기호를 누를수 있음
        elif key in numbers:
            if self.equalPressed == True:
                # '=' 이 눌렸다면, 연산기호 부터 입력
                pass
            else:
                self.display.setText(txt + key)
        elif key == "(":
            # 앞에 아무것도 없거나 앞에 연산기호 있을 때
            if (txt == '') or (txt[-1] in operator and txt[-1] != '.'):
                self.display.setText(txt + key)
        elif key == ")":
            if "(" in txt and len(txt) != 1 and txt[-1] not in operator:
                # 앞에 ( , () x, 앞에 연산기호
                self.display.setText(txt + key)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())