"""Файл работает с площадью и периметром треугольника"""

def area(a,h):
	'''Функция принимает на вход сторону треугольника - a и высоту - h
	Вычисляет площадь и возвращает ее
	Пример работы:
	area(40,20)
	output: 400'''
	if a<0 or h<0:
		raise ValueError("Сторона и высота треугольника должна быть больше 0!")
	if not isinstance(a, int) or not(isinstance(h,int)):
		raise TypeError("Сторона и высота должна быть integer")
	if a > 1_000_000_000 or h > 1_000_000_000:
		raise ValueError("Такие большие значения не поддерживаются")
	if a < -1_000_000_000 or h < -1_000_000_000:
		raise ValueError("Такие маленькие значения не поддерживаются")
	return a * h / 2
def perimeter(a , b, c):
	'''Функция принимает на вход стороны треугольника a, b, c
	Вычисляет периметр и возвращает его
	Пример работы:
	area(10,20,30)
	output: 60'''
	if a<0 or b<0 or c<0:
		raise ValueError("Стороны должны быть больше 0!")
	if not isinstance(a, int) or not(isinstance(b,int) or not(isinstance(c,int))):
		raise TypeError("Стороны должны быть integer")
	if a > 1_000_000_000 or b > 1_000_000_000 or c > 1_000_000_000:
		raise ValueError("Такие большие значения не поддерживаются")
	if a < -1_000_000_000 or b < -1_000_000_000 or c < -1_000_000_000:
		raise ValueError("Такие маленькие значения не поддерживаются")
	return a + b + c
