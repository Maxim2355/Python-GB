# Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.

def my_func(x, y):
    return x ** y

print(f'Результат: '
      f'{my_func(int(input("Основание степени Х: ")), int(input("Показатель степени Y: ")))}')