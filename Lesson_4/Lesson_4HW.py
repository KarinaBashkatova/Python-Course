# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]


import random
list1=[random.randint(-45,45) for _ in range (20)]
print('Случайный список %s' %list1)
list_sqrt=[el**2 for el in list1]
print('Случайный список в квадрате %s' %list_sqrt)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruits1=['banana', 'orange', 'apple']
fruits2=['pineapple', 'watermelon', 'orange', 'apple']
common=[fruit for fruit in fruits1 if fruit in fruits2]
print(common)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный


import random
list2=[random.randint(-100,200) for _ in range (20)]
print('Случайный список %s' %list2)
krat3=[el for el in list2 if el%3==0]
print('Cписок кратных 3 {}'.format(krat3))
polozh=[el for el in list2 if el>0]
print('Список из положительных элеметров {}'.format(polozh))