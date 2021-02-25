# strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому

# st = 'as 23 fdfdg544'
# for i in st:
#     if i.isdigit():
#         print(i, end=',')

#################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі

# st = 'as 23 fdfdg544 34'
# res = ''
# for item in st:
#     if item.isdigit():
#         res += item
#     else:
#         res += '!'
# res = res.strip('!').split('!')
# res = [i for i in res if i]
# res=','.join(res)
# print(res)

#################################################################################

# list comprehension
#
# 1)есть строка:
# greeting = 'Hello, world'
# записать каждый символ в лист поменяв его на верхний регистр
# пример:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

# l = [i for i in greeting.upper()]
# print(l)

# 2) с диапазона от 0-50 записать в лист только не парные числа, при этом возвести их в квадрат
# пример:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

# l = [i**2 for i in range(50) if i % 2 != 0]
# print(l)

# function
#
# - створити функцію яка виводить ліст

# def func(list):
#     print(list)
#
# func([1,5, 89, 67])

# - створити функцію яка приймає три числа та виводить та повертає найменьше.

# def func(one, two, three):
#     min = 0
#     if one <= two and one <= three:
#         min = one
#     elif two <= one and two <= three:
#         min = two
#     elif three <= one and three <= two:
#         min = three
#     return min
#
# print(func(45, 123, 67))

# - створити функцію яка приймає три числа та виводить та повертає найбільше.

# def func(one, two, three):
#     max = 0
#     if one >= two and one >= three:
#         max = one
#     if two >= one and two >= three:
#         max = two
#     if three >= two and three >= one:
#         max = three
#     return max
#
# print(func(356,2,56))

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменше, а виводить найбільше

# def func(*args):
#     print(max(*args))
#     return min(*args)
#
# print(func(9, 10, 7, 4, -10, 0))


# - створити функцію яка повертає найбільше число з ліста

# def func(list):
#     max = list[0]
#     for i in list:
#         if i >= max:
#             max = i
#     return max
#
# print(func([5,23,76,3]))

 # - створити функцію яка повертає найменьше число з ліста

# def func(list):
#     min = list[0]
#     for i in list:
#         if i <= min:
#             min = i
#     return min
#
# print(func([4, 3, 5]))

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.

# def func(list):
#     sum = 0
#     for i in list:
#         sum += i
#     return sum
#
# print(func([4,5,5,6,6]))

# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

# def func(list):
#     sum = 0
#     for i in list:
#         sum += i
#     return sum / len(list)
#
# print(func([6, 7, 8]))

# decorators
# - є функція:
# def pr():
#     return 'Hello_boss_!!!'
#  написати декоратор до цієї функції, який замінює нижні підчеркування на пробіли і повертає це значення

# def decor(func):
#     def wrap():
#         return func().replace('_', ' ')
#     return wrap
#
# @decor
# def pr():
#     return 'Hello_boss_!!!'
#
#
# print(pr())
