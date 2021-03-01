# 1)
# создать класс Human(имя и возраст)

# class Human():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# # и два класса Prince и Cinderella которые наследуются от Human
# # у принца должен быть размер туфельки и  метод который принимает лист золушек и выводит какой золушки подошла туфелька
#
# class Cinderella(Human):
#     def __init__(self, name, age, cinderella_size):
#         super().__init__(name, age)
#         self.cinderella_size = cinderella_size
#
#
# cinderellas = [Cinderella('Olha', 24, 38), Cinderella('Mary', 12, 36), Cinderella('Olena', 20, 37)]
#
# class Prince(Human):
#     def __init__(self, name, age, prince_size):
#         super().__init__(name, age)
#         self.prince_size = prince_size
#
#     def find_love(self):
#         for love in cinderellas:
#             if love.cinderella_size == self.prince_size:
#                 print(f'{self.name} - {love.name}')
#
# prince1 = Prince('Max', 23, 36)
# prince2 = Prince('Oleg', 43, 37)
# prince1.find_love()
# prince2.find_love()





# 2)
# Создать класс Rectangle:
# -конструктор принимает две стороны x,y
# -описать арифметические методы:
#   + сума площадей двух экземпляров класса
#   - разница площадей
#   == или площади равны
#   != не равны
#   >, < меньше или больше
#   при вызове метода len() подсчитывать сумму сторон

import math

# class Rectangle:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.area = x * y
#
#     def __add__(self, other):
#         return self.area + other.area
#
#     def __sub__(self, other):
#         return math.fabs(self.area - other.area)
#
#     def __eq__(self, other):
#         return self.area == other.area
#
#     def __ne__(self, other):
#         return self.area != other
#
#     def __gt__(self, other):
#         return self.area > other.area
#
#     def __lt__(self, other):
#         return self.area < other.area
#
#     def __len__(self):
#         return self.x * 2 + self.y * 2
#
# shape1 = Rectangle(3,4)
# shape2 = Rectangle(5,6)
#
# print('Suma: ', shape1 + shape2)
# print('Sub: ', shape1 - shape2)
# print('Equal: ', shape1 == shape2)
# print('Not equal: ', shape1 != shape2)
# print('>: ', shape1 > shape2)
# print('>: ', shape1 < shape2)
# print('suma_shape1: ', len(shape1))
# print('suma_shape2: ', len(shape2))

