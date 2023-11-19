from sympy import sympify, solve, symbols, diff, Float
from math import fabs
from time import sleep
eps = 1e-4
ls = ['x', 'y', 'z']


def method_jacobi(funct, f_0):
    def f(per, tmp, var):
        return tmp.subs(var, per)

    def simplify(x_0, func):
        f_sim = []
        for iterate in range(3):
            for elem in ls:
                if elem == ls[iterate]:
                    continue
                func[iterate] = func[iterate].subs(elem, x_0[ls.index(elem)])
            f_sim.append(func[iterate])
        return f_sim

    def newtons_method(a, b, func, var):
        res = ''
        if f(a, func, var) * f(a, diff(func, var, 2), var) > 0:
            x_1 = a
        else:
            x_1 = b
        x_2 = x_1 - f(x_1, func, var) / f(x_1, diff(func, var), var)
        while fabs(x_2 - x_1) > eps and fabs(f(x_2, func, var)) > eps:
            if f(x_2, func, var) < f(x_1, func, var):
                x_1 = x_2
                x_2 = x_1 - f(x_1, func, var) / f(x_1, diff(func, var), var)
            else:
                x_1 = (x_1 + x_2) / 2
                x_2 = x_1 - f(x_1, func, var) / f(x_1, diff(func, var), var)
        res = Float(x_2)
        return res

    test = False
    f_1 = [0] * 3
    while not test:
        a0 = -20
        b0 = 20
        func_res = simplify(f_0.copy(), funct.copy())
        for pos in range(3):
            f_1[pos] = newtons_method(a0, b0, func_res[pos], ls[pos])

        flag = True
        f_new = simplify(f_1.copy(), funct.copy())
        print(f_new)
        print(f_1)

        for i_2 in range(3):
            if fabs(f_1[i_2] - f_0[i_2]) > eps:
                flag = False
                break
            if fabs(f_new[i_2].subs(ls[i_2], f_1[i_2])) > eps:
                flag = False
                break
        if flag:
            test = True
            break
        else:
            f_0 = f_1.copy()
    return f_1


with open('1input.txt', 'r', encoding='utf-8') as file:
    function = []
    for _ in range(3):
        temp = file.readline()
        function.append(sympify(temp))
    file.readline()
    f0 = [float(k) for k in file.readline().split()]
    print('System is:')
    print('—' * 30)
    for j in range(3):
        print('f{0}|'.format(j+1), ' ', function[j], '= 0')
    print('\n')
    m_j = method_jacobi(function, f0)
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
