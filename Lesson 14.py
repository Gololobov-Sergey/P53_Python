import random


def printLine(symbol='*', count=10):
    for i in range(count):
        print(symbol, end='')
    print()

def summ(a, b):
    c = a + b
    return c


def isEven(num):
    return num % 2 == 0

def isPositive(num):
    return num > 0


def isKrat(num, a):
    return num % a == 0

# nums = [random.randint(-1000,2000) for i in range(10)]
# print(nums)
# count = 0
# for el in nums:
#     if isPositive(el) and isKrat(el, 5):
#         count += 1
# print(count)


def countSymbolList(_list):
    count = 0
    for el in _list:
        count += len(str(el))
    return count


def printListInLine(_list: list):
    count = len(_list) - 1 + countSymbolList(_list)
    printLine('*', count)
    for el in _list:
        print(el, end=' ')
    print()
    printLine('*', count)


# printListInLine(nums)


# isEven(5)
#
# printLine('*', 20)
# printLine('#', 30)
#
# c = summ(3, 5)
# print(c)
# starLine()
#
# starLine()

# *****************
# 2 3 4 6 7 8 9 0 0
# *****************

# def boo():
#     global a
#     a = 100
#
#
# a = 10
# print(a)
# boo()
# print(a)

# printLine('$', 30)
# printLine('#')
# printLine()

def add(a, b, c=0, d=0):
    return a + b + c + d

# print(add(1,2,3,4))
# print(add(1,2,3))
# print(add(1,2))



a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
d = int(input("d="))
e = int(input("e="))
def chislo():
    if a <= b and a <= c and a <= d and a <= e:
        print(a)

chislo()


def digitCount(number: float):
    num = number
    digit = 0
    while number > 10:
        digit += 1
        number //= 10
    else:
        digit += 1
        if number % 10 == 0:
            digit += 1
    print(f"The amount of digit in {num} is {digit}.")

digitCount(100)