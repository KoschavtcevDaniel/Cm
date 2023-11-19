from sympy import sympify, solve, symbols, diff, Float
from math import fabs
from time import sleep
eps = 1e-4
ls = ['x', 'y', 'z']


def check(func, func_0):
    for l in ls:
        s = 0
        for var in func:
            s += abs(((diff(var, l).subs(ls[0], func_0[0])).subs(ls[1], func_0[1])).subs(ls[2], func_0[2]))
            print(diff(var, l))
        print('s -', s)
        if s >= 1:
            return False
    return True


def processing(func, mass):
    ind = 0
    res = []
    for tmp in mass:
        pow_ = 1
        if (ls[ind]+'^') in tmp:
            pow_ = tmp[tmp.find(ls[ind]+'^') + 2]
        if pow_ == 1:
            res.append(solve(func[ind], ls[ind])[0])
        else:
            res.append(solve(func[ind], ls[ind]+'**'+pow_)[0]**(1/int(pow_)))
        ind += 1
    return res


def method(funct, x1, f_0):
    while True:
        x2 = x1.copy()
        res = []
        flag = True
        for ind in range(3):
            for j_ind in range(3):
                x2[ind] = (x2[ind].subs(ls[j_ind], f_0[j_ind]))
            res.append(x2[ind])
        print(res)
        for i_2 in range(3):
            if fabs(res[i_2] - f_0[i_2]) > eps:
                flag = False
                break
            if fabs((funct[i_2].subs(ls[0], res[0])).subs(ls[1], res[1]).subs(ls[2], res[2])) > eps:
                flag = False
                break
        f_0 = res
        if flag:
            return res


with open('1input.txt', 'r', encoding='utf-8') as file:
    function = []
    func_str = []
    function_copy = []
    for _ in range(3):
        temp = file.readline()
        func_str.append(temp)
        function.append(sympify(temp))
        function_copy.append(sympify(temp))
    file.readline()
    f0 = [float(k) for k in file.readline().split()]
    print('f_0: ', *f0)
    print('\nSystem is:')
    print('—' * 30)
    for j in range(3):
        print('f{0}|'.format(j + 1), ' ', function[j], '= 0')

    proc = processing(function, func_str)
    print('\nResult: ', *proc)
    if not check(proc, f0):
        print('Wrong date')
    else:
        m_j = method(function_copy.copy(), proc.copy(), f0.copy())
        print('\nAnswer is:')
        print('—' * 30)
        for ind in range(3):
            print(ls[ind], '| ', m_j[ind])

        print('\nCheck answer: ')
        print('—' * 30)
        for t in function:
            chc = ((t.subs('x', m_j[0]).subs('y', m_j[1])).subs('z', m_j[2]))
            if fabs(chc) < eps:
                print(chc)





