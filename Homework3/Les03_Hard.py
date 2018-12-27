# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

def multidrob(s):
	if '+' in s:
		n=s.split('+')
		drob1=n[0]
		drob2=n[1]
	else:
		n=s.split('-',maxsplit=1)
		drob1=n[0]
		drob2=n[1]

	if '/' in drob1:
		n=drob1.split('/')
		chisl1=int(n[0])
		znam1=int(n[1])
	else:
		chisl1=int(drob1)
		znam1=1

	if '/' in drob2:
		n=drob2.split('/')
		chisl2=int(n[0])
		znam2=int(n[1])
	else:
		chisl2=int(drob2)
		znam2=1

	if znam1==znam2:
		obschznam=znam1
		summa1=chisl1+chisl2
	else:
		obschznam=(znam1*znam2)
		summa1=(chisl1*znam2+chisl2*znam1)

	celayachast=int(summa1/obschznam)
	chislitog=summa1-(celayachast*obschznam)
	if celayachast==0:
		celayachast=''
	
	for i in range(2,9):
		if chislitog%i==0 and obschznam%i==0:
			chislitog=int(chislitog/i)
			obschznam=int(obschznam/i)
	if chislitog==0:
		otvet=('Ответ: {}!'.format(celayachast))
	else:
		otvet=('Ответ: {} {}/{}'.format(celayachast,chislitog,obschznam))
	return otvet
s=input('Введите пример:')
print(multidrob(s))