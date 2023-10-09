from decimal import Decimal as Dc, getcontext


def bubble_sort(nums, n):
    swapped = True
    while swapped:
        swapped = False
        for i in range(n - 1):
            if nums[i][0] > nums[i+1][0]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True


def interpol(a, n):
    for j in range(2, n-1):
        for i in range(n-1):
            a[i][j] = (a[i+1][j-1] - a[i][j-1]) / (a[i+1][0] - a[i][0])
    return a


with open('input.txt', 'r', encoding='utf-8') as f_in:
    x0 = Dc(f_in.readline())
    n = int(f_in.readline())

    a = [[0] * n for i in range(n)]
    for i in range(n):
        temp = [Dc(k) for k in f_in.readline().split()]

        a[i][0] = temp[0]
        a[i][1] = temp[1]

    t = []
    for k in range(n):
        t.append(a[k].copy())

    res = interpol(a, n)
    for j in res:
        print(*j, sep=' ')

    bubble_sort(t, n)
    print()
    res2 = interpol(t, n)
    for l in res2:
        print(*l, sep=' ')
