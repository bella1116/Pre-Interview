from math import factorial as fact

def factorial(numStr):
    try:
        n = int(numStr)
        r = str(fact(n))
    except:
        r = 'Error!'
    return r

def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r


def decToRoman(n):
    try:
        # 정수 아닌거 x
        n = int(n)
    except:
        return 'error'
    # 양의정수 아니거나 4000넘는 수 x
    if n <= 0 or n >= 4000:
        return 'error'
    result = ''

    # romans.keys()는 키값들의 리스트, 그걸 역순으로 정렬
    for value in sorted(romans.keys(), reverse=True):
        while n >= value:
            result += romans[value]
            n -= value
    return result


def romanToDec(n):
    ro = n
    result = 0
    # 더해지는 value들 리스트에
    valuelist = []
    valuecount = {}
    for value in sorted(romans.keys(), reverse=True):
        # value 바뀔때마다 count 0으로 초기화
        count = 0
        # 키값(로마문자)이 스트링의 제일 처음에 있으면 계속 while loop
        while ro.find(romans[value]) == 0:
            length = len(romans[value])
            ro = ro[length:]
            valuelist.append(value)
            result += value

    count_459 = 0  # 4,5,9 세기
    count_4590 = 0  # 40,50,90 세기
    count_45900 = 0  # 400, 500, 900 세기

    # value들이 몇번씩 더해졌는지
    for value in valuelist:
        if value in valuecount:
            valuecount[value] += 1
        else:
            valuecount[value] = 1

    for value, count in valuecount.items():
        # 4번이상 나오면 에러
        if value in [1, 10, 100, 1000] and count >= 4:
            return 'error'

        elif value in [4, 5, 9]:
            count_459 += count
        elif value in [40, 50, 90]:
            count_4590 += count
        elif value in [400, 500, 900]:
            count_45900 += count

    # 셋중에 하나라도 2 이상이면 에러
    if count_459 >= 2 or count_4590 >= 2 or count_45900 >= 2:
        return 'error'
    # 같은자리수가 중복으로 나온것도 에러
    elif valuecount[1] != 0 and count_459 != 0:
        return 'error'
    elif valuecount[10] != 0 and count_4590 != 0:
        return 'error'
    elif valuecount[100] != 0 and count_45900 != 0:
        return 'error'

    # 로마문자를 작은자리수부터 쓰면 for문에 걸리지도 않고 끝남. 이런경우 에러처리.
    elif ro != '':
        return 'error'
    else:
        return str(result)


romans = {
    1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
    100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
    10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
}
