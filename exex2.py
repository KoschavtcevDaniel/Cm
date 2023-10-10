from decimal import Decimal as Dc, getcontext


def check_n(n):
    if n < 2:
        return False
    return True


def check_m(m, n):
    if m > n:
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
    tmp = []
    for j in range(1, m+1):
        tmp[j-1][0] = a[n-j][j]
        for i in range(1, j):
            tmp[j-1][i] = a[n-1][i]
    return tmp


with open('input.txt', 'r', encoding='utf-8') as f_in:
    n = int(f_in.readline())

    a = [[0] * (n+1) for i in range(n)]
    for i in range(n):
        temp = [Dc(k) for k in f_in.readline().split()]
        a[i][0] = temp[0]
        a[i][1] = temp[1]

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

        bubble_sort(tmp, n)
        print('res2:    ')
        res2 = interpol(tmp, n)
        for l in res2:
            print(*l, sep=' ')

        print("Input m-values: ")
        m = int(input())
        while not(check_m(m, n)):
            print('m-values incorrect')
            m = int(input())
        ans1 = result(res1, m)
        ans2 = result(res2, m)

    else:
        print('The task condition is not met')
