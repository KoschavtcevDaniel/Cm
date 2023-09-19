from decimal import Decimal as Dc, getcontext

getcontext().prec = 6

def is_pos_def(matrix):
    for k in range(1, n+1):
        submatrix = [row[:k] for row in matrix[:k]]
        determinant = 1
        for i in range(k):
            determinant *= submatrix[i][i]
            for j in range(i+1, k):
                ratio = submatrix[j][i] / submatrix[i][i]
                for l in range(i, k):
                    submatrix[j][l] -= ratio * submatrix[i][l]
        if determinant <= 0:
            return False
    return True

def copy_a(a, n):
    t = []
    for i in range(n):
        t.append(a[i].copy())
    return t

def check(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j] != a[j][i]:
                return False
    return True

def new_cond(a, b, n):
    tran = [[None] * n for i in range(n)]
    tempa = [[None] * n for i in range(n)]
    tempb = [None] * n
    for i in range(n):
        for j in range(n):
            tran[j][i] = a[i][j]
    for i in range(n):
        s2 = 0
        for j in range(n):
            s1 = 0
            for k in range(n):
                s1 += tran[j][k] * a[k][i]
            s2 += tran[i][j] * b[j]
            tempa[i][j] = s1
        tempb[i] = s2
    return tempa, tempb

def create(a, n):
    u = [[0] * n for l in range(n)]
    for i in range(0, n):
        for j in range(n):
            s1 = Dc('0')
            s2 = Dc('0')
            for k in range(i):
                if i == j:
                    s1 += Dc(u[k][i] ** 2)
                else:
                    s2 += Dc(u[k][i] * u[k][j])
            if j > i:
                if u[i][i] != 0:
                    u[i][j] = Dc((a[i][j] - s2)) / Dc(u[i][i])
                else:
                    return False
            elif j < i:
                u[i][j] = Dc('0')
            elif i == j:
                u[i][i] = Dc((a[i][i] - s1)) ** Dc('0.5')
        print(*u[i])
    return u

def shuffling(a, n):
    for i in range(n-1):
        a[i], a[i+1] = a[i+1], a[i]
    return a

def create_y(u, b, n):
    y = [0] * n
    for i in range(n):
        s = 0
        for k in range(i):
            s += Dc(u[k][i] * y[k])
        y[i] = Dc(b[i] - s) / Dc(u[i][i])
    print('y    ', *y)
    return y

def create_x(u, y, n):
    x = [0] * n
    for i in range(n - 1, -1, -1):
        s = 0
        for k in range(i + 1, n):
            s += Dc(u[i][k] * x[k])
        x[i] = Dc(y[i] - s) / Dc(u[i][i])
    print('x    ', *x)
    return x

with open('input.txt', 'r', encoding='utf-8') as f_in, open('output.txt', 'w', encoding='utf-8') as f_out:
    n = int(f_in.readline())
    a = [] * n

    for i in range(n):
        temp = [int(k) for k in f_in.readline().split()]
        a.append(temp)

    b = [Dc(k) for k in f_in.readline().split()]
    print(*a, sep='\n')
    s = ''
    ac = copy_a(a, n)
    if is_pos_def(ac):
        if not(check(ac)):
            ac, b = new_cond(ac, b, n)
            print('ac:  ', *ac, sep='\n')
            print('b:   ', *b, sep='\n')
        u = create(ac, n)
        while not(u):
            ac = copy_a(shuffling(a, n), n)
            u = create(ac, n)
        y = create_y(u, b, n)
        x = create_x(u, y, n)
        s = ' '.join(map(str, x))
    else:
        s = 'Not symmetric matrix'
    print(s)
    f_out.writelines(s)
