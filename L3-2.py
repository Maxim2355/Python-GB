# Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

def user_data(name, surname, yob, city, email, phone):
    return print(f'Имя: {name}, Фамилия: {surname}, Год рождения: {yob}, '
                 f'Город проживания: {city}, Email: {email}, Телефон: {phone}.')

print('Введите данные: ')
user_data(
    name=input('Имя: '),
    surname=input('Фамилия: '),
    yob=input('Год рождения: '),
    city=input('Город проживания: '),
    email=input('email: '),
    phone=input('phone: '),
)