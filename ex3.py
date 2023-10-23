from sympy import sympify, diff, Float
from math import fabs


def check(c, d):
    if c < d:
        return True
    return False


# def der(f, x, h):
#     return (f(x + h) - f(x - h)) / (2 * h)


def f(per, tmp):
    return tmp.subs('x', per)


def newtons_method(a, b, func):
    eps = 10 ** (-6)
    res = set()
    h = 0.5
    beg = a
    while beg < b:
        end = beg + h
        if f(beg, func) * f(end, func) > 0:
            beg += h
            continue
        if f(beg, diff(func, 'x')) * f(end, diff(func, 'x')) < 0:
            beg += h
            continue
        if f(beg, func) * f(beg, diff(func, 'x', 2)) > 0:
            x_1 = beg
        else:
            x_1 = end
        x_2 = x_1 - f(x_1, func) / f(x_1, diff(func, 'x'))
        while fabs(x_2 - x_1) > eps:
            if f(x_2, func) < f(x_1, func):
                x_1 = x_2
                x_2 = x_1 - f(x_1, func) / f(x_1, diff(func, 'x'))
            else:
                x_1 = (x_1 + x_2) / 2
                x_2 = x_1 - f(x_1, func) / f(x_1, diff(func, 'x'))
        beg += h
        res.add(Float(x_2))
    return sorted(res)


with open('input1.txt', 'r', encoding='utf-8') as file:
    a, b = [int(k) for k in input().split()]
    func = sympify(file.readline().rstrip())

    flag = check(a, b)
    while not(flag):
        print('Incorrect value: a > b')
        a, b = [int(k) for k in input().split()]
        flag = check(a, b)

    print('Answer: ')
    print(*newtons_method(a, b, func), sep='    ')
