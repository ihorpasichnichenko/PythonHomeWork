

print('Задание № 1')
N = int(input('Введите ширину треугольника '))
for i in range(N, 0, -1):
    print("*" * i)

print('Задание № 2')
N = int(input('Введите ширину треугольника '))
for i in range(N+1):
    print("*" * i)

print('Задание № 3')
N = int(input('Введите ширину треугольника '))
for i in range(N,0, -1):
    print(("*" * i).rjust(N))

print('Задание № 4')
N = int(input('Введите ширину треугольника '))
for i in range(N+1):
    print(("*" * i).rjust(N))