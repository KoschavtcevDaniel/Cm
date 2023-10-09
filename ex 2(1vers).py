from decimal import Decimal as Dc, getcontext
import time
import matplotlib.pyplot as plt
import numpy as np

getcontext().prec = 4


def check(n):
    if n > 1:
        return True
    return False


def newton_coefficient(x, y):
    m = len(x)
    x = np.copy(x)
    a = np.copy(y)
    for k in range(1, m):
        a[k:m] = (a[k:m] - a[k - 1])/(x[k:m] - x[k - 1])
        print(*a[k:m], sep='\t')
    print(*a)
    return a


def newton_polynomial(x, y, a, x0):
    n = len(x) - 1
    p = a[n]
    for k in range(1, n + 1):
        p = a[n - k] + (x0 - x[n - k])*p
    return p


def newton(a, n):
    k = 0
    for j in range(2, n):
        k += 1
        for i in range(n-k):
            a[i][j] = (a[i+1][j-1] - a[i][j-1]) / (a[i+k][0] - a[i][0])



def bubble_sort(nums, n):
    swapped = True
    while swapped:
        swapped = False
        for i in range(n - 1):
            if nums[0][i] > nums[0][i + 1]:
                nums[0][i], nums[0][i + 1] = nums[0][i + 1], nums[0][i]
                nums[1][i], nums[1][i + 1] = nums[1][i + 1], nums[1][i]
                swapped = True


def picture(t, a, l):
    plt.plot(l, 'ro')
    plt.plot(t[0], t[1])
    plt.plot(a, 'ro')
    plt.plot(a)
    plt.show()


with open('input.txt', 'r', encoding='utf-8') as f_in:
    x0 = Dc(f_in.readline())
    n = int(f_in.readline())
    a = [] * n

    for i in range(n):
        temp = [Dc(k) for k in f_in.readline().split()]
        a.append(temp)

    x, y = list(map(lambda p: p[0], a)), list(map(lambda p: p[1], a))

    if check(n):
        # t0 = time.time()
        a = newton_coefficient(x, y)
        res = newton_polynomial(x, y, a, x0)
        # t1 = time.time()
        # print(t1 - t0)
        print('res - ', res)
        t = [x, y]
        ms = [[0] * n for i in range(n)]
        for i in range(n):
            ms[i][0] = x[i]
            ms[i][1] = y[i]
        mx = t[0][0]
        newton(ms, n)
        print('ms - ', *ms)
        bubble_sort(t, n)
        l = newton_coefficient(t[0], t[1])
        res2 = newton_polynomial(t[0], t[1], l, x0)
        picture(t, a, l)
    else:
        print('The task condition is not met')
