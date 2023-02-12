import logging
from typing import Union


# Номер 1
"""створити файл library.py
В ньому написати функції
Написати функцію, яка отримує ціле число і повертає слово "копійка" у вірній формі: 1 -- копійка, 2 -- копійки, 25 -- копійок"""
#
#
def get_national_ua_coins(number: int) -> str:
    lust_number = int(str(number)[-1])
    if number == 0 or number in range(5,21) or lust_number in [0,5,6,7,8,9]:
        result = 'копеек'
    elif number == 1 or lust_number == 1:
        result = 'копейка'
    elif number in [2,3,4,5,6,7,8,9] or lust_number in [2,3,4]:
        result = 'копейки'
    else:
        result = 'копеек'
    return result
#
#
# print(get_national_ua_coins(457))
#
#
# Номер 2
"""Написати функцію, яка отримує ціле число і повертає слово "гривня" у вірній формі: 1 -- гривня, 2 -- гривні, 25 -- гривень"""
#
#
def get_national_ua_money(number: int) -> str:
    lust_number = int(str(number)[-1])
    if number == 0 or number in range(5,21) or lust_number in [0,5,6,7,8,9]:
        result = 'гривень'
    elif number == 1 or lust_number == 1:
        result = 'гривня'
    elif number in [2,3,4,5,6,7,8,9] or lust_number in [2,3,4]:
        result = 'гривни'
    else:
        result = 'гривень'
    return result
#
#
# Номер 3
"""Функцію, яка приймає число і повертає список, в якому перший елемент - стрічка з цілою частиною числа + слово 'гривня' у вірному відмінку,
 другий елемент - стрічка з мантісою (значення після коми), + слово 'копійка' у вірній формі. 
наприклад - 1 -- ['1 гривня', "0 копійок"]; 10.1 -- ['10 гривень', "10 копійок"]; 2.01 -- ['2 гривні', "1 копійка"]. 
В даній функції для створення форм слів гривня та копійка використати результат роботи функцій, описаних вище."""
#
#
def get_user_numbers_for_list(num):
    res3 = str(float(num))
    temp_list = res3.split('.')
    result = [int(temp_list[0]), int(temp_list[1])*10]
    if result[1] != 0:
        result[1] = int(str(result[1])[:2])
    return result
#
#
#
#
#
# Номер 4
"""Напишіть функцію is_hot_today, яка отримує параметр температури (число, за замовчуванням 30), 
і в залежності від величини повідомляє, чи сьогодні жарко, чи холодно (більше 25 - жарко, інакше холодно). 
Перевірку на -155555555555 градусів чи +555555555555 не проводимо,
 просто відштовхуємося від отриманого значення. Подумайте, який тип даних має повертати функція"""
#
#
temrature = 30

def is_hot_today(temprature: int|float)-> str:
    if temprature >= 25:
        result = 'The weather is hot today!'
        return result
    else:
        result = 'The weather is cold today!'
    return result



my_list = [lambda temp:temp != 25]
#
#
# Номер 5
#
#
"""створіть функцію, яка приймає логічне значення, і якщо воно позитивне, то повертає лямбда-функцію, яка в свою чергу отримує один аргумент (число),
 і повертає його абсолютну величину (воно буде завжди позитивним), в іншому випадку, повертається лямбда функція, яка отримує один аргумент (число), 
 і завжди повертає його з мінусом"""


def get_bool_from_user(need_positive: bool = True):
    if need_positive:
        return lambda number: abs(number)
    return lambda number: -abs(number)




#
#
# Номер 6
#
#
"""Cтворіть функцію, яка отримує від користувача число і повертає його як число (як варіант - доопрацюйте аналогічну функцію з лекції). проте!!!
   Якщо користувач ввів не вірні дані, які не можна конвертувати в число ("шість"), заставте користувача ввести валідні дані (цикли вам в допомогу).
   Результатом в будь-якому випадку має бути число. зауважте - функція має прийняти один не обовязковий стрічковий аргумент - месседж, за замовчуванням - "Введіть число"""
#

def get_user_numbers(message: str = 'Введите сумму депозита...', need_int = False) -> Union[float,int]:
    while True:
        user_input = input(message)
        try:
            result = float(user_input)
            if need_int:
                return int(result)
            return result

        except ValueError:
                print('Вы не можете ввести эти данные! Попробуйте еще раз.')
# #
# print(get_user_numbers())
