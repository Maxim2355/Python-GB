# Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

list_length = int(input('Выберите длину списка: '))
list_orgnl = []
list_mxd = []
for i in range(1, list_length + 1):
    item = input(f"Введите значение {i}-го элемента: ")
    list_orgnl.append(item)
    if i % 2 == 0:
        list_mxd.append(item)
        list_mxd.append(list_orgnl[i - 2])

if len(list_mxd) != list_length:
    list_mxd.append(list_orgnl[list_length - 1])

print(f"Оригинальный список: {list_orgnl}")
print(f"Перемешаный список: {list_mxd}")
