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

        self.nameEdit = QLineEdit()
        self.ageEdit = QLineEdit()
        self.scoreEdit = QLineEdit()
        self.amountEdit = QLineEdit()
        self.keyEdit = QComboBox()

        self.keyEdit.addItem('Name')
        self.keyEdit.addItem('Age')
        self.keyEdit.addItem('Score')

        add = QPushButton('Add')
        delete = QPushButton('Del')
        find = QPushButton('Find')
        inc = QPushButton('Inc')
        show = QPushButton('Show')
        self.data = QTextEdit()

        grid = QGridLayout()

        grid.setSpacing(10)
        grid.addWidget(name, 1, 0)
        grid.addWidget(self.nameEdit, 1, 1)
        grid.addWidget(age, 1, 2)
        grid.addWidget(self.ageEdit, 1, 3)
        grid.addWidget(score, 1, 4)
        grid.addWidget(self.scoreEdit, 1, 5)
        grid.addWidget(amount, 2, 2)
        grid.addWidget(self.amountEdit, 2, 3)
        grid.addWidget(key, 2, 4)
        grid.addWidget(self.keyEdit, 2, 5)
        grid.addWidget(add, 3, 1)
        grid.addWidget(delete, 3, 2)
        grid.addWidget(find, 3, 3)
        grid.addWidget(inc, 3, 4)
        grid.addWidget(show, 3, 5)
        grid.addWidget(result, 4, 0)
        grid.addWidget(self.data, 5, 0, 10, 6)

        add.clicked.connect(self.addClicked)
        delete.clicked.connect(self.delClicked)
        inc.clicked.connect(self.incClicked)
        find.clicked.connect(self.findClicked)
        show.clicked.connect(self.showScoreDB)

        self.setLayout(grid)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('ScoreDB')
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


    def addClicked(self):
        record = {'Name': self.nameEdit.text(), 'Age': int(self.ageEdit.text()), 'Score': int(self.scoreEdit.text())}
        self.scoredb += [record]
        self.showScoreDB()


    def delClicked(self):
        for s in range(len(self.scoredb)):
            for p in self.scoredb:
                if p['Name'] == self.nameEdit.text():
                    self.scoredb.remove(p)
        self.showScoreDB()


    def findClicked(self):
        self.findsort = []
        for p in self.scoredb:
            if p['Name'] == self.nameEdit.text():
                self.findsort += [p]
        self.findDB()


    def incClicked(self):
        for p in self.scoredb:
            if p['Name'] == self.nameEdit.text():
                p['Score'] = str(int(p['Score']) + int(self.amountEdit.text()))
        self.findClicked()

    # write the data into person db
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