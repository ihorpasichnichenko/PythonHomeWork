A = int(input('First number...'))
B = int(input('Second number...'))
C = int(input('Third number...'))
if A > 10 and B > 10 and C > 10 and A% 3 == 0 and B% 3 == 0:
    print('Yes')
else:
    print('No')


a = int(input('First number...'))
b = int(input('Second number...'))
c = int(input('Third number...'))
max_num = a
if b > max_num:
    max_num = b
elif c > max_num:
    max_num = c
print(max_num)