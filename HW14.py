
# Задание 1
# Дан файл с произвольным текстом, необходимо найти все числа в файле и записать в список numbers




import re
with open("data_2.txt") as file:
    numbers = re.findall(r'\d+', file.read())
    print(list(map(int,numbers)))



# Задание 2
# Запросить у пользователя текст и записать его в файл data.txt

n = input('Введите Ваш текcт...:')
f = open('data.txt','w')
f.write(n)




# Задание 3
# Запросить у пользователя число N и запросить N чисел у пользователя, потом записать их в файл numbers.txt через пробел

x = ' '
a = int(input('Введите количество вводов...:'))
for i in range(a):
    f = open('numbers.txt','a')
    f.write((input('Введите Ваши числа...:') + x))



# Задание 4
# Сгенерировать 100 рандомных чисел и записать их в файл random_numbers.txt, где одна строка = одно число





# import random
#
number = random.choice(list('123456789'))
f = open('random_numbers.txt','w')
for i in range(99):
    numbers = number + random.choice(list('123456789'))
    f.write('\n'.join(numbers))










# Задание 5
# Дан файл с произвольным текстом, нужно найти количество слов в файле и вывести пользователю

f = open('data_2.txt' ,'r')
file = f.read()
words = file.split()
print('Количество слов в файле:',len(words))





# Задание 6
# Дан файл в котором записаны числа через пробел, необходимо вывести пользователю сумму этих чисел

f = open('data_2.txt' ,'r')
file = f.readlines()
summ = 0
for line in file:
    for word in line.split():
        summ += int(word)
print(summ)



# Задание 7
# Дан файл в котором записан текст, необходимо вывести топ 5 строк которые чаще всего повторяются, пример:
# 'в' - 20 раз
# 'привет' - 10 раз
# 'как' - 9 раз
# 'у' - 7
# 'world' - 4



import re
from collections import Counter

with open('data_2.txt') as f:
    data = f.read()
    words = re.findall(r'[\w]+', data)
    result = Counter(words)
    print("\n".join(list(map(str,result.most_common(5)))))




#
#
# import re
# slovo = {}
# f = open('data_2.txt' ,'r')
# file = f.read()
# pattern = re.findall(r'\b[a-z]{1,15}\b', file)
# for word in pattern:
#     count = slovo.get(word, 0)
#     slovo[word] = count + 1
# slovo_list = slovo.keys()
# for words in slovo_list:
#     print(words,'-',slovo[words])




