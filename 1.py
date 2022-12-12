# 1. Напишите программу, которая принимает на вход число
# N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# print('Введите число')
# a = int(input())
# def recur(a):  
#       if (a>0):
#           result =a*recur(a-1)
#           print(result)
#       else:
#           result=1
#       return result 
# recur(a)

from itertools import accumulate
import operator
num = int(input('Введите число: '))
def kit(num):
    return list(accumulate([x for x in range(1, num + 1)], operator.mul))
print(kit(num))
