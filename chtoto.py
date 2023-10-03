from decimal import Decimal as Dc, getcontext
import time
getcontext().prec = 6

def check(n):
    if n > 1:
        return True
    return False
def interpol(a, n):
    s = 0
    for i in range(n):
        print(a[i][0])


with open('input.txt', 'r', encoding='utf-8') as f_in, open('output.txt', 'w', encoding='utf-8') as f_out:
    n = int(f_in.readline())
    a = [] * n

    for i in range(n):
        temp = [Dc(k) for k in f_in.readline().split()]
        a.append(temp)

    print(*a, sep='\n')
    s = ''
    
    if check(n):
        interpol(a, n)
        
    else:
        s = 'Not positively defined matrix'
    print(s)
    f_out.writelines(s)
