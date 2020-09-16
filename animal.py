wordcount = {'dog':5, 'cat':7, 'tiger':9}
print(wordcount['tiger'])
wordcount['tiger'] += 1
word = input("Word : ")
print(wordcount[word])
for k in wordcount.keys():
    print(k)
for v in wordcount.values():
    print(v)
for k, v in wordcount.items():
    print(k,v)