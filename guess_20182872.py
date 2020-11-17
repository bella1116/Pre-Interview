class Guess:

    def __init__(self, word):
        self.numTries = 0
        # 시도횟수
        self.guessedChars = []
        # 제시된 문자들
        self.secretWord = word
        # 비밀단어
        self.indexlist = []
        # 맞춘 문자의 인덱스들
        self.currentStatus = ''
        pass
    # 현재까지의 상황(맞춘글자,실패횟수) 출력
    
    def display(self):
        print("Tries: %d" % self.numTries)
        self.currentStatus = "current:"
        for i in range(len(self.secretWord)):
            if i in self.indexlist:
                self.currentStatus += self.secretWord[i]
            else:
                self.currentStatus += "_"
        print(self.currentStatus)

    def guess(self, character):
        # 일단 제시된 문자를 리스트에 추가
        self.guessedChars.append(character)
        # 문자가 단어에 있으면 리스트에 인덱스를 추가
        # (단어에 문자가 2개이상 있을수 있으니 포문으로)
        for index, char in enumerate(self.secretWord):
            if char == character:
                self.indexlist.append(index)

        # 단어에 없으면 시도횟수 하나 늘림
        else:
            self.numTries += 1
        # 맞춘 문자의 개수가 단어의 길이와 같으면 다 맞춘거니까 True 리턴
        if len(self.indexlist) == len(self.secretWord):
            return True
        else:
            return False
