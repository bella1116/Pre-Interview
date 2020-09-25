import time
import random

arr = []
def iterfibo(n):
    for i in range(n+1):
        if i == 0:
            arr.append(0)
        elif n ==1 or n == 2:
            arr.append(1)
        else:
            arr.append(arr[i-1] + arr[i-2])
    return arr[n]

def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)


while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("IterFibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
