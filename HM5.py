# Программа запрашивает у пользователя пароль и записывает в переменную password.
#
# Необходимо посчитать сложность пароля, где за каждую пройденную проверку пароль получает +1 балл к итоговой оценке, максимальное количество баллов - 5
#
# Проверки:
#
# Длина пароля больше или равно 8 символам
# В пароле есть хотя бы одна цифра
# В пароле есть хотя бы одна большая
# В пароле есть хотя бы одна маленькая буква
# В пароле есть хотя бы один спец символ (+, -, /, _, % и т.д. P.S. их на самом деле больше)
# После всех проверок нужно вывести пользователю число - количество баллов за пароль, а так-же рекомендации по улучшению пароля.


password = input('Enter your password...')
score = 0
value = True
SpecialSym = ['!','@','#','$','%','^','&','*','(',')','_','+''=','?','|','/',',',';','"','[',']',':','{','}']

if not len(password) >= 8:
    print('Длина пароля должна быть 8 или больше символов...')
else:
    score +=1
    value = False

if not any(char.isdigit() for char in password):
    print('Пароль должен содержать хотябы одну цифру...')
else:
    score +=1
    value = False

if not any(char.isupper() for char in password):
    print('Пароль должен содержать хотябы одну большую букву...')
else:
    score +=1
    value = False

if not any(char.islower() for char in password):
    print('Пароль должен содержать хотябы одну маленькую букву...')
else:
    score +=1
    value = False

if not any(char in SpecialSym for char in password):
    print('Пароль должен содержать хотябы один спец символ...')
else:
    score +=1
    value = False
print('Ваш пароль оценивается в', score ,'баллов')