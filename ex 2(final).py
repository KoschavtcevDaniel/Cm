import matplotlib.pyplot as plt
import numpy as np
from time import time

def check_n(n):
    if n < 2:
        return False
    return True


def check_m(m, n):
    if m > n or m < 0:
        return False
    return True


def bubble_sort(nums, n):
    swapped = True
    while swapped:
        swapped = False
        for i in range(n - 1):
            if nums[i][0] > nums[i+1][0]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True


def interpol(a, n):
    k = 0
    for j in range(2, n+1):
        k += 1
        for i in range(n-k):
            a[i][j] = (a[i+1][j-1] - a[i][j-1]) / (a[i+k][0] - a[i][0])
    return a


def result(a, m):
    tmp = [[0] * (i+1) for i in range(m)]
    for j in range(1, m+1):
        tmp[j-1][0] = a[n-j][j]
        for i in range(1, j):
            tmp[j-1][i] = a[n-i][0]
    return tmp


def create_func(ans, x):
    k = len(ans)
    f = 0
    for i in range(k):
        p = ans[i][0]
        for j in range(1, len(ans[i])):
            p *= (x - ans[i][j])
        f += p
    return f


def points(mass, m):
    k = len(mass)
    res = [[0]*m for i in range(2)]
    ind = 0
    for i in range(k-1, k-m-1, -1):
        res[0][ind] = mass[i][0]
        res[1][ind] = mass[i][1]
        ind += 1
    return res



def draw_pict(ans1, ans2, p1, p2):
    # Создаём экземпляр класса figure и добавляем к Figure область Axes
    fig, ax = plt.subplots()

    # Добавим заголовок графика
    ax.set_title('График функции')
    # Название оси X:
    ax.set_xlabel('x')
    # Название оси Y:
    ax.set_ylabel('y')

    # Начало и конец изменения значения X, разбитое на 100 точек
    x = np.linspace(-10, 10, 1000)

    # Построение функции
    f1 = create_func(ans1, x)
    f2 = create_func(ans2, x)
    # Вывод графика
    ax.plot(x, f1)  # blue
    plt.scatter(p1[0], p1[1])
    ax.plot(x, f2)  # orange
    plt.scatter(p2[0], p2[1])
    plt.show()


with open('input.txt', 'r', encoding='utf-8') as f_in:
    t1 = time()
    n = int(f_in.readline())

    a = [[0] * (n+1) for i in range(n)]
    check = set()
    for i in range(n):
        temp = [float(k) for k in f_in.readline().split()]
        a[i][0] = temp[0]
        a[i][1] = temp[1]
        check.add(tuple(temp))

    if len(check) == n:
        t = []
        for k in range(n):
            t.append(a[k].copy())

        tmp = []
        for k in range(n):
            tmp.append(a[k].copy())

        if check_n(n):
            print('res1:    ')
            res1 = interpol(t, n)
            for j in res1:
                print(*j, sep=' ')

            print()
            bubble_sort(tmp, n)
            print('res2:    ')
            res2 = interpol(tmp, n)
            for l in res2:
                print(*l, sep=' ')
            print()
            print("Input m-values: ", end=' ')

            m = int(input())
            while not(check_m(m, n)):
                print('m-values incorrect, input again: ', end=' ')
                m = int(input())
            p1 = points(t, m)
            p2 = points(tmp, m)
            ans1 = result(res1, m)
            ans2 = result(res2, m)
            print()
            print('ans1:    ', *ans1)
            print('ans2:    ', *ans2)
            t2 = time()
            print(t2 - t1)
            draw_pict(ans1, ans2, p1, p2)
        else:
            print('The task condition is not met')
    else:
        print('Incorrect points')
