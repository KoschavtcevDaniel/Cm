from sympy import sympify
from math import fabs
from time import sleep


def integrate(func, a, b, h):
    sleep(2)

    def f(funct, var):
        return funct.subs('x', var)

    k1 = a + h
    k2 = b
    res = 0
    while k1 < k2:
        res += (f(func, k1-h) + f(func, k1)) / 2 * h
        k1 += h
    return res


with open('input_4.txt', 'r') as file:
    eps = 1e-4
    a_, b_ = [int(k) for k in file.readline().split()]
    function = sympify(file.readline())

    print('Interval: [', a_, ', ', b_, ']', sep='')
    print('Function:', function, end='\n')

    h_ = eps**(1/4)
    n = int((b_ - a_) / h_)
    h_ = (b_ - a_) / n
    while True:
        Ih = integrate(function.copy(), a_, b_, h_)
        I2h = integrate(function.copy(), a_, b_, 2*h_)
        print(Ih - I2h)
        if fabs(Ih - I2h) / 3 <= eps:
            break
        else:
            h_ = h_ / 2
    print('—' * 20)
    print('Result is', Ih)
    print('—' * 20)
