from sympy import Symbol
x = Symbol('x')
x+x+1

a = Symbol('a')
a+a+1


p = (x+2) * (x + 3)
expand(p)


from sympy import factor, Symbol, expand
x = Symbol('x')
y = Symbol('y')
expr = x**2 - y**2
factors = factor(expr)
expand = expand(factors)
expand

from sympy import factor, Symbol, expand, pprint
x = Symbol('x')
y = Symbol('y')
#id1 = x**3 + 3*x**2*y + 3*x*y**2 + y**3
#fid1 = factor(id1)
fid1 = (x + y)**3
eid1 = expand(fid1)
#eid1
#print(eid1)
pprint(eid1)

chapter4_prog1_list = []
def chapter4_prog1(n):
    x = Symbol('x')
    for i in range(1,n+1):
        chapter4_prog1_list.append(x**i/i)
    return chapter4_prog1_list

a = chapter4_prog1(5)
pprint(a)
sum(a)
sum(a).subs({x:1.2})



from sympy import factor, Symbol, expand, pprint, simplify, sympify
x = Symbol('x')
y = Symbol('y')
expr = x**2 + 2*x*y + y**2
factor(expr)
#result = expr.subs({x:1, y:2})
result1 = expr.subs({x:1-y})
simplify(result1)


simplify(x**2)

expr = x**2 + 3*x + x**3 + 2*x
simplify(expr)
sympify(expr)


from sympy import factor, Symbol, expand, pprint, simplify, sympify, solve
a = Symbol('a')
x = Symbol('x')
b = Symbol('b')
c = Symbol('c')
y = Symbol('y')
expr = a*x**2+b*x+c
solve_x = solve(expr, x, dict = True)
pprint(solve_x)

eqn1 = 2*x + 3*y - 6
eqn2 = 3*x + 2*y - 12
eqn_solve = solve((eqn1, eqn2), dict = True)
pprint(eqn_solve)


from sympy.plotting import plot
from sympy import Symbol
x = Symbol('x')
plot(x**3+4*x**2+5*x+7)











