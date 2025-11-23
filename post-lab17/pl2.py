import sympy as sp

n, z, omega = sp.symbols('n z omega')

x_n = sp.cos(omega * n)

X_z = sp.summation(x_n * z**(-n), (n, 0, sp.oo))

print("Z-transform of x[n] = cos(ωn) u[n]:")
sp.pprint(X_z, use_unicode=True)
