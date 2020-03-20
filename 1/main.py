import math


def multiply(x, y):
    s_x = str(x)
    s_y = str(y)
    len_x = len(s_x)
    len_y = len(s_y)
    if len_x == 1 or len_y == 1:
        r = int(x) * int(y)
        return r
    n = len_x
    if len_x > len_y:
        s_y = s_y.rjust(len_x, '0')
        n = len_x
    elif len_y > len_x:
        s_x = s_x.rjust(len_y, '0')
        n = len_y
    m = n % 2
    offset = 0
    even = n
    if m != 0:
        n += 1
        offset = 1
    floor = int(math.floor(n / 2)) - offset
    ceil = int(math.ceil(n / 2)) - offset
    a = s_x[0:floor]
    b = s_x[ceil:n]
    c = s_y[0:floor]
    d = s_y[ceil:n]
    r = ((10 ** n) * multiply(a, c)) + (
            (10 ** (n / 2)) * (multiply(a, d) + multiply(b, c))) + multiply(b, d)
    return int(r)


a = int(input('Введите певрое число для умножения: '))
b = int(input('Введите второе число для умножения: '))
print(f'Результат умножения: {multiply(a, b)}')
