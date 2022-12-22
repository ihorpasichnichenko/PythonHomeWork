print('Задание № 1')
N = int(input('Введите ширину треугольника '))
for N in range(5,0,-1):
    print("*" * N)

print('Задание № 2')

N = int(input('Введите ширину треугольника '))
for N in range(0, 6, 1):
        print("*" * N)

print('Задание № 3')

N = int(input('Введите ширину треугольника '))
for N in range(5,0,-1):
    print(('*' * N).rjust(5))


print('Задание № 4')

N = int(input('Введите ширину треугольника '))
for N in range(0, 6, 1):
        print(("*" * N).rjust(5))