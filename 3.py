# 3. Реализуйте алгоритм перемешивания списка.

# from random import randrange
# print('Введите размерность списка')
# n = int(input())
# a = [randrange(-n, n) for i in range(n)]
# print(a)

import random
lst = [1, 2, 3, 4]
random.shuffle(lst, random.random)
print(lst)
