row = int(input('Enter a number : '))
for i in range(row):
    for j in range(row):
        if j <= i :
            print('*', end='')
    print()
print()