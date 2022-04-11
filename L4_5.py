# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

list = [i for i in range(100, 1001, 2)]
print("Список чётных чисел в диапазоне [100-1000]: ", list)
print("Произведение всех элементов списка: ", reduce(lambda x,y: x*y, list))