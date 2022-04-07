# # Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
# # но с прописной первой буквой.
# # Например, print(int_func(‘text’)) -> Text.

# Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Используйте написанную ранее функцию int_func().

def int_func(text):
    return text.title()



def my_title(text):
    listed_text = list(text)
    listed_text[0] = listed_text[0].upper()
    return ''.join(listed_text)

output_1 = []
output_2 = []
for word in input('Введите строку, слова в которой разделены пробелами: ').split(' '):
    output_1.append(int_func(word))
    output_2.append(my_title(word))

print(f'Вариант1 Строка получается вот такая: {" ".join(output_1)}')
print(f'Вариант2 Строка получается вот такая: {" ".join(output_2)}')

