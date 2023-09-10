from decimal import Decimal as Dc, getcontext
from math import fabs

with open('input.txt', 'r', encoding='utf-8') as f_in, open('output.txt', 'w', encoding='utf-8') as f_out:
    n = int(f_in.readline())
    a = [] * n

    for i in range(n):
        temp = [Dc(k) for k in f_in.readline().split()]
        a.append(temp)

    b = [Dc(k) for k in f_in.readline().split()]

    x = [0] * n
    y = [0] * n
    u = [[0] * n for i in range(n)]

    getcontext().prec = 6
    copa = a.copy()
    copb = b.copy()

    for i in range(0, n):
        s1 = 0
        s2 = 0
        for j in range(0, n):
            for k in range(i):
                if i == j:
                    s1 += Dc(u[k][i] ** 2)
                else:
                    s2 += Dc(u[k][i] * u[k][j])
            if j > i:
                if u[i][i] != 0:
                    u[i][j] = Dc(fabs(a[i][j] - s2)) / Dc(u[i][i])
                else:
                    u[i][j] = 0
            elif j < i:
                u[i][j] = Dc('0')
            elif i == j:
                u[i][i] = Dc(fabs(a[i][i] - s1)) ** Dc('0.5')

    for i in range(n):
        s = 0
        for k in range(i):
            s += Dc(u[k][i] * y[k])
        y[i] = Dc(b[i] - s) / Dc(u[i][i])

    for i in range(n-1, -1, -1):
        s = 0
        for k in range(i+1, n):
            s += Dc(u[i][k] * x[k])
        x[i] = Dc(y[i] - s) / Dc(u[i][i])

    for i in range(n):
        s = 0
        for j in range(n):
            s += copa[i][j] * x[j]
        print(s, copb[i])

    f_out.writelines(' '.join(map(str, x)))

