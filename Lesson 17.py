# f = open("test.txt", "w", encoding='utf-8')
# f.write("Слава Україні!")
# f.close()


# f = open("test.txt", "r", encoding='utf-8')
#
# s = f.read()
# # s = f.readline()
# # s = f.readlines()
# print(s)
# f.close()


import random

# arr = [random.randint(1, 20) for i in range(10)]
# print(arr)
# f = open("arr.txt", "w")
# f.write(" ".join([str(i) for i in arr]))
# f.close()


# f = open("arr.txt", "r")
# s = f.read().split()
# # arr = [int(i) for i in s]
# arr = list(map(int, s))
# f.close()
#
# arr2 = [i for i in arr if i % 2 == 0]
# f = open("arr2.txt", "w")
# f.write(" ".join(map(str, arr2)))
# f.close()

# Напишіть програму, яка відкриває файл data.txt, аналізує
# його вміст і створює звіт summary.txt, у якому вказується
# кількість рядків, слів і символів у файлі.

# f = open("test1.txt", "r")
# # s = f.read().count('\n')
# lines = f.readlines()
# s = len(lines)
# print(s)
# words = 0
# symbols = 0
# for l in lines:
#     words += len(l.split())
#     symbols += sum(map(len, l.split()))
# print(words)
# print(symbols)

# def square(a):
#     return a * a
#
# arr = [random.randint(1, 5) for i in range(5)]
# print(arr)
# arr2 = list(map(square, arr))
# print(arr2)


# Напишіть програму, яка читає вміст файлу data.txt,
# замінює кожну літеру на наступну в алфавіті (наприклад, a b, z a),
# а потім записує результат у encrypted.txt.

s = "mama" # nbnb
m = ""
n = 3
for i in s:
    m += chr(ord(i)+n)

print(m)