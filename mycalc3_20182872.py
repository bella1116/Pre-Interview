from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout


class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class Calculator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Display Window
        self.display = QLineEdit('')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        # Digit Buttons
        self.digitButton = [x for x in range(0, 10)]

        #self.digitButton[0] = Button('0')
        #self.digitButton[1] = Button('1')
        #self.digitButton[2] = Button('2')
        #self.digitButton[3] = Button('3')
        #self.digitButton[4] = Button('4')
        #self.digitButton[5] = Button('5')
        #self.digitButton[6] = Button('6')
        #self.digitButton[7] = Button('7')
        #self.digitButton[8] = Button('8')
        #self.digitButton[9] = Button('9')

        #num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.digitButton = [x for x in range(10)]
        for i in range(10):
            self.digitButton[i] = Button(str(i), self.buttonClicked)

        # . and = Buttons
        self.decButton = Button('.', self.buttonClicked)
        self.eqButton = Button('=', self.buttonClicked)

        # Operator Buttons
        self.mulButton = Button('*', self.buttonClicked)
        self.divButton = Button('/', self.buttonClicked)
        self.addButton = Button('+', self.buttonClicked)
        self.subButton = Button('-', self.buttonClicked)

        # Parentheses Buttons
        self.lparButton = Button('(', self.buttonClicked)
        self.rparButton = Button(')', self.buttonClicked)

        # Clear Button
        self.clearButton = Button('C', self.buttonClicked)

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 2)

        numLayout = QGridLayout()

        #numLayout.addWidget(self.digitButton[0], 3, 0)
        #numLayout.addWidget(self.digitButton[1], 2, 0)
        #numLayout.addWidget(self.digitButton[2], 2, 1)
        #numLayout.addWidget(self.digitButton[3], 2, 2)
        #numLayout.addWidget(self.digitButton[4], 1, 0)
        #numLayout.addWidget(self.digitButton[5], 1, 1)
        #numLayout.addWidget(self.digitButton[6], 1, 2)
        #numLayout.addWidget(self.digitButton[7], 0, 0)
        #numLayout.addWidget(self.digitButton[8], 0, 1)
        #numLayout.addWidget(self.digitButton[9], 0, 2)

        for i in range(1,10):
            row = int(((9 - i) / 3 ) + 1)
            col = ((i - 1) % 3)
            numLayout.addWidget(self.digitButton[i], row, col, 1, 1)

        numLayout.addWidget(self.digitButton[0], 4, 0)
        numLayout.addWidget(self.decButton, 4, 1)
        numLayout.addWidget(self.eqButton, 4, 2)

        mainLayout.addLayout(numLayout, 1, 0)

        opLayout = QGridLayout()

        opLayout.addWidget(self.mulButton, 0, 0)
        opLayout.addWidget(self.divButton, 0, 1)
        opLayout.addWidget(self.addButton, 1, 0)
        opLayout.addWidget(self.subButton, 1, 1)

        opLayout.addWidget(self.lparButton, 2, 0)
        opLayout.addWidget(self.rparButton, 2, 1)

        opLayout.addWidget(self.clearButton, 3, 0)

        mainLayout.addLayout(opLayout, 1, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle("My Calculator")


    def buttonClicked(self):
        button = self.sender()
        key = button.text()
        operator = ['*', '+', '-', '/', '.']
        if key == '=':
            # = 눌리면 창에입력된 연산 실행하고 결과창에표시
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except:
                self.display.setText('error')

        elif key == 'C':
            self.display.setText("")
        else:
            if self.display.text() == '' and key in operator:
                # 연산기호부터 입력못하도록함
                pass

            elif self.display.text() != '' and self.display.text()[-1] in operator:
                # 가장마지막에 입력된 것이 연산기호 인 경우 **와 //를 제외하고, 연산기호가 연달아 입력되지 못하도록
                if self.display.text()[-1] == '*' and self.display.text()[-2] != '*' and key == '*':
                    self.display.setText(self.display.text() + key)
                    # 가장마지막에 입력된 것이 *이고 *가 또 입력되었을때 이건 입력되게 함. (***는 불가능)
                elif self.display.text()[-1] == '/' and self.display.text()[-2] != '/' and key == '/':
                    self.display.setText(self.display.text() + key)
                    # 가장 마지막에 입력된 것이 / 이고 /가 또 입력되었을때 이것도 입력되게 함. (///는 불가능)
                elif key not in operator:
                    self.display.setText(self.display.text() + key)
                else:
                    pass
            else:
                self.display.setText(self.display.text() + key)

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())

