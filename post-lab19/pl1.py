import sympy as sp

n, z = sp.symbols('n z', positive=True)

u = 1  # unit step for n >= 0

X = sp.summation(u * z**(-n), (n, 0, sp.oo))

print("Z-transform of u[n]:")
sp.pprint(X, use_unicode=True)
