# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
import random

list_random = [random.randint(-10, 10) for i in range(10)]
"""
Формирует список из 10 случайных чисел в диапазоне от -10 до 10
"""

print(list_random)

sqwr = [item*item for item in list_random]
"""
Получаем список из значений в квадрате элементов списка случайных чисел
"""

print(sqwr)


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruits1 = ["apple", "banana", "orange", "grapes", "grapefruit", "watermelon", "melon", "pear", "mango"]
fruits2 = ["tomato", "avocado", "grapes", "melon", "peach", "apricot", "pineapple"]

# формируется список фруктов, который содержит элементы присутствующие в обоих списках

fruitsSelection = [a for a in fruits1 or b for b in fruits2 if a == b]


print(fruitsSelection)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random

# формируем список из 10 случайных чисел в диапазоне от -10 до 10
list_random3 = [random.randint(-10, 10) for i in range(10)]

print(list_random3)

copy_list_random3 = list_random3[:]

# формируем список с элементами исходного списка, которые кратны 3, не кратны 4, положительны
modiflist_random3 = [el for el in copy_list_random3 if el > 0 or el % 3 == 0 or el % 4 != 0]

print(modiflist_random3)
