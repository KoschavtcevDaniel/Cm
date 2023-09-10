from decimal import Decimal as Dc, getcontext

with open('input.txt', 'r', encoding='utf-8') as f_in, open('output.txt', 'w', encoding='utf-8') as f_out:
    n = int(f_in.readline())
    a = [] * n

    for i in range(n):
        temp = [Dc(k) for k in f_in.readline().split()]
        a.append(temp)

    b = [Dc(k) for k in f_in.readline().split()]

    x = [0] * n
    getcontext().prec = 6

    for k in range(n-1):
        for i in range(k+1, n):
            if a[k][k] == 0:
                t = 0
                break
            t = Dc(a[i][k]) / Dc(a[k][k])
            b[i] = b[i] - t * b[k]
            for j in range(k, n):
                a[i][j] = a[i][j] - t * a[k][j]


    f = 1
    for k in range(n-1, -1, -1):
        s = Dc(0)
        if not(f):
            break
        for j in range(k+1, n):
            s += Dc(a[k][j] * x[j])
        if a[k][k] == 0 and b != 0:
            f_out.writelines('No answer')
            f = 0
            break
        elif s == 0 and b == 0:
            x = 0
        x[k] = Dc((b[k] - s)) / Dc(a[k][k])

    if f:
        f_out.writelines(' '.join(map(str, x)))
