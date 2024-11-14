"""Файл работает с площадью и периметром прямоугольника"""
def area(a,b):
	'''Функция принимает на вход стороны прямоугольника a,b
	Вычисляет площадь и возвращает ее
	Пример использования:
	area(10,5)
	output: 50
	'''
	if a<0 or b<0:
		raise ValueError("Стороны прямоугольника должны быть больше 0!")
	if not isinstance(a, int) or not(isinstance(b,int)):
		raise TypeError("Стороны должны быть integer")
	if a > 1_000_000_000 or b > 1_000_000_000:
		raise ValueError("Такие большие значения не поддерживаются")
	if a < -1_000_000_000 or b < -1_000_000_000:
		raise ValueError("Такие маленькие значения не поддерживаются")
	return a * b
def perimeter(a, b):
	'''Функция принимает на вход стороны прямоугольника a,b
	Вычисляет периметр и возвращает его
	Пример использования: 
	perimeter(10,5)
	output: 30
	'''
	if a<0 or b<0:
		raise ValueError("Стороны прямоугольника должны быть больше 0!")
	if not isinstance(a, int) or not(isinstance(b,int)):
		raise TypeError("Стороны должны быть integer")
	if a > 1_000_000_000 or b > 1_000_000_000:
		raise ValueError("Такие большие значения не поддерживаются")
	if a < -1_000_000_000 or b < -1_000_000_000:
		raise ValueError("Такие маленькие значения не поддерживаются")
	return (a + b) * 2


