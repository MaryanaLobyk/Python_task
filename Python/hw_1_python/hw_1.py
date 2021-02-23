# TASK1
l = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
# - найти min число в листе
# l.sort()
# print(l[0])

# - удалить все одинаковые значения
# for i in l:
#     while l.count(i) > 1:
#         l.remove(i)
# print(l)

# - заменить каждое четвертое значение на "Х"
# for i in range(3, len(l), 4):
#     l[i] = 'X'
# print(l)

# - вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов этого же листа

# TASK2
# вывести на экран пустой квадрат из "*" сторона которого указана в переменой:

# side = int(input("Enter side: "))
# for i in range(0, side):
#     if i == 0 or i == side - 1:
#         print(side * '*')
#         continue
#     for j in range (0, side):
#         if j == 0 or j == side - 1:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

# TASK3
# переделать первое задание под меню с помощью цикла
# print('''Available menu:
#     1.Find min value
#     2.Delete double items
#     3.Change every 4 item into "X"
#     4.Show the nearest element to the average list value
#     5.Ex''')
# print('\n')
#
# command = int(input('Enter necessary command: '))
#
# if command == 1:
#     print(min(l))
#
# elif command == 2:
#     for i in l:
#         while l.count(i) > 1:
#             l.remove(i)
#     print(l)
#
# elif command == 3:
#     for i in range(3, len(l), 4):
#         l[i] = 'X'
#     print(l)



# TASK4
# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j, end='\t')
#     print()

# n = int(input('Enter number: '))
# i = 1
# j = 1
# while i <= n:
#     while j <= n:
#         print(i * j, end='\t')
#         j += 1
#     i += 1
#     j = 1
#     print()
