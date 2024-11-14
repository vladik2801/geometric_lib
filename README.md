# Общее описание проекта
Проект geometric_lib представляет из себя библиотеку для работы с геометрическими телами , а именно вычисление их площади и периметра. Библиотека работает с квадратом, треугольником, прямоугольником и окружностью
# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- triangle: a * h / 2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- triangle: a + b + c
## Функция 'area' для треугольника 
[Функция вычисляет площадь треугольника.](https://github.com/vladik2801/geometric_lib/commit/5916e14f51f255d73dc62c9f79d3b33acb58c050#diff-94c956d9e141cbd27489a238ddb0bf4810e9a6cd01f1ebb4a84df2395c1997c7)

### Пример использования:

area(40,20)\
	output: 400

## Функция 'perimeter' для треугольника:

[Функция вычисляет периметр для треуголника](https://github.com/vladik2801/geometric_lib/commit/5916e14f51f255d73dc62c9f79d3b33acb58c050#diff-94c956d9e141cbd27489a238ddb0bf4810e9a6cd01f1ebb4a84df2395c1997c7)

### Пример использования: 

area(10,20,30)\
	output: 60

## Функция 'area' для окружности:

[Функция вычисляет площадь окружности](https://github.com/vladik2801/geometric_lib/commit/5916e14f51f255d73dc62c9f79d3b33acb58c050#diff-0cd40c58d7d2552ad79bfc5cc0a6e0c6dbdb32b874912aac0d18391c5cff6d33)

### Пример использования: 
area(10)\
    output: 314.1592653589793 

## Функция 'perimeter' для окружности:

[Функция вычисялет периметр окружности](https://github.com/vladik2801/geometric_lib/commit/5916e14f51f255d73dc62c9f79d3b33acb58c050#diff-0cd40c58d7d2552ad79bfc5cc0a6e0c6dbdb32b874912aac0d18391c5cff6d33)

### Пример использования: 

perimeter(10)\
    output: 62.83185307179586

## Функция 'area' для квадрата:

[Функция вычисляет площадь квадрата](https://github.com/vladik2801/geometric_lib/commit/5916e14f51f255d73dc62c9f79d3b33acb58c050#diff-563c529e3e75cfb8027e42674ed445489656cfe5b9b77f379d3d529bfcc35a23) 

### Пример использования: 

area(10)\
    output: 100

## Функция 'perimeter' для квадрата:

[Функция считает периметр квадрата](https://github.com/vladik2801/geometric_lib/commit/5916e14f51f255d73dc62c9f79d3b33acb58c050#diff-563c529e3e75cfb8027e42674ed445489656cfe5b9b77f379d3d529bfcc35a23)

### Пример использования: 

area(10)\
    output: 40

# Файл с тестами unittest
- Для создания тестов используется библиотека [unittes](https://docs.python.org/3/library/unittest.html)
- Для каждой функции делается проверка на: 
     valid(соответствует ли выполняемый результат верному значению)
     value(тестируется поведение функции при передаче отрицательного и нулевого значения)
     type(тестируется поведение функции при передаче отличных от integer типов данных)
     large(тестируется поведение функции при передаче значения больше миллиарда)
     smallest(тестируется поведение функции при передаче значения меньше миллиарда)
- Тесты прописаны в файле [test.py](https://github.com/vladik2801/geometric_lib/blob/documentation/test.py)
# История изменений
- [55cea7cb5f38d7a49984df46416bd9787b43ca23: Добавлен новый файл](https://github.com/vladik2801/geometric_lib/commit/55cea7cb5f38d7a49984df46416bd9787b43ca23)
- [b21b25c0a7c379dbbf8820730b04a65ce0e9d23b: Исправлена функция с ошибкой](https://github.com/vladik2801/geometric_lib/commit/b21b25c0a7c379dbbf8820730b04a65ce0e9d23b)
- [63f4f23513916bac21642a5a4b5ae646308e71f7  Внесены конечные корректировки](https://github.com/vladik2801/geometric_lib/commit/63f4f23513916bac21642a5a4b5ae646308e71f7) 
- [5916e14f51f255d73dc62c9f79d3b33acb58c050  Добавлена документация](https://github.com/vladik2801/geometric_lib/commit/5916e14f51f255d73dc62c9f79d3b33acb58c050)
- [42dc26bcdf08d68de42d1875b7d4de2461e10b9c Добавлены unittest-ы](https://github.com/vladik2801/geometric_lib/commit/42dc26bcdf08d68de42d1875b7d4de2461e10b9c)