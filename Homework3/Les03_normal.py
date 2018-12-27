# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    pass



def fibonacci(n, m):
	"""Возвращает ряд Фибоначии с n-элемента до m-элемента"""

	l=[1,1,2]
	i=3
	while i<m:
		x=l[i-1]+l[i-2]
		l.append(x)
		i=i+1
	return l[n:m]

n=int(input())
m=int(input())
print(fibonacci(n,m))



# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()



def sort_to_max(origin_list):
	"""Сортирует элементы  списка от меньшего к большему"""
	n=1
	while n<len(origin_list):
		for i in range (len(origin_list)-n):
			if origin_list[i]>origin_list[i+1]:
				origin_list[i],origin_list[i+1]=origin_list[i+1],origin_list[i]
		n+=1
	return origin_list

import random
a=random.randint(1,15)
l=[random.randint(-100,100) for i in range(0, a)]
print('Случайный отсортиорванный список {}'.format(sort_to_max(l)))

print('Отсортированный список из задания {}'.format(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter (l)
	filtr=map(lambda x: x>=0,l)
	return filtr
	for filtr(l[i])==True:
		b.append(l[i])

l=[1,2,3,4,50,-1,-21,-56]
print(my_filter(l))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

# Будем исходить из того, что стороны параллелограмма папарно равны. 
# Для проверки в конкретно задаче возьмем некие координаты четырех вершин, которые точно являются вершинами параллелограмма:

A1=(-6,1)
A2=(3,1)
A3=(6,-2)
A4=(-3,-2)
import math

def dlina(a,b):
	"""Высчитывает длину стороны параллелограмма"""
	dlina=float(math.sqrt(sum(map(lambda x, y: (x-y)**2, a, b))))
	return dlina

A1A2=dlina(A1,A2)
A3A4=dlina(A3,A4)
A2A3=dlina(A2,A3)
A1A4=dlina(A1,A4)

'''Для наглядности'''

print('{0},{1},{2},{3}'.format(A1A2, A3A4, A2A3, A1A4))
if A1A2==A3A4 and A2A3==A1A4:
	print('Указанные точки являются вершинами параллелограмма')
else:
	print('Указанные точки не являюися вершинами параллелограмма')