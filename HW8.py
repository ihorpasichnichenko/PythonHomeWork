# Дано два множества A и B
# В множестве А находятся имена должников за Сентябрь
# В множестве B находятся имена должников за Октябрь
# Найти:
# * Вывести имена людей которые должны за Сентябрь и Октябрь
# * Вывести должников за Октябрь у которых нет долга за Сентябрь


A_september = {'Corey Tailor', 'Matt Heafy', 'Vitya Tsoi' , 'Jacoby Shaddix' , 'John Frusciante' , 'Winston McCall','Yan Gillan'}
B_october = {'Nazareth' , 'Yan Gillan' , 'Denis' , 'Corey Tailor' , 'Matt Heafy', 'Jacoby Shaddix' }
print(A_september & B_october)
print(B_october - A_september)


