from decimal import Decimal as Dc, getcontext
def func1(a, b):
    x = [0] * n
    for k in range(n-1):
        for i in range(k+1, n):
            if a[k][k] == 0:
                return False
            t = Dc(a[i][k]) / Dc(a[k][k])
            b[i] = b[i] - t * b[k]
            for j in range(k, n):
                a[i][j] = a[i][j] - t * a[k][j]
    for k in range(n - 1, -1, -1):
        s = Dc(0)
        for j in range(k + 1, n):
            s += Dc(a[k][j] * x[j])
        x[k] = Dc((b[k] - s)) / Dc(a[k][k])
    return x
def reverse(a):
    temp = a[0]
    for k in range(1, n):
        a[k-1], a[k] = a[k], a[k-1]
    a[n-1] = temp
    return a

with open('input4.txt', 'r', encoding='utf-8') as f_in, open('output4.txt', 'w', encoding='utf-8') as f_out:
    n = int(f_in.readline())
    a1 = [] * n

    for i in range(n):
        temp = [Dc(k) for k in f_in.readline().split()]
        a1.append(temp)

    b = [Dc(k) for k in f_in.readline().split()]
    l = a1.copy()
    print(l)
    getcontext().prec = 6
    x = func1(l, b)
    print(l)
    print(a1)
    print(x)
    while not(x):
        t = reverse(a1)
        x = func1(t, b)

    f_out.writelines(' '.join(map(str, x)))
