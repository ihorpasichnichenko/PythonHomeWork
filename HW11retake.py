

def cache_decorator(func):
    slovar = {}

    def qwerty(*args, **kwargs):
        try:
            return slovar[args]
        except KeyError:
            res = func(*args, **kwargs)
            slovar[args] = res
            return res

    return qwerty
@cache_decorator
def swim_l(length):
    if length == 1:
        return 1
    elif length == 2:
        return 2
    elif length == 3:
        return 4
    else:
        return (
                swim_l(length - 3)
                + swim_l(length - 2)
                + swim_l(length - 1)
        )


@cache_decorator
def row_m(a:float) -> float:
    print(f'Вызвана функция qwerty с аргументом {a} ')
    return a*a

print('Результат выполнения swim_l(50):', swim_l(1))
print('Результат выполнения swim_l(50):', swim_l(1))
print('Результат выполнения qwerty(5):', row_m(1))
print('Результат выполнения swim_l(20):', row_m(1))
print('Результат выполнения qwerty(5):', row_m(1))