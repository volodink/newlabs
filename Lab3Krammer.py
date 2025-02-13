from sympy import Matrix, Symbol
import time

start = time.time()

a=Symbol('a')
b=Symbol('b')

A=Matrix([[50, -32], [24,18]])
B=Matrix([[61, -75], [2,17]])
C=Matrix([[-3, 5], [-8,3]])
D=Matrix([a,b])

delta1 = C.copy()
delta2 = C.copy()

delta1[:,0] = D
delta2[:,1] = D

if C.det() != 0:
    x = delta1.det()/C.det()
    y = delta2.det()/C.det()
    print('\nx =', x, '\ny =', y)
    x = x.subs(a, A)
    x = x.subs(b, B)
    y = y.subs(a, A)
    y = y.subs(b, B)
    print('\nx =', x, '\ny =', y)
else:
    print('det(C) = 0, решения нет')

end = time.time()
print(f'Время выполнения - {end - start}')
