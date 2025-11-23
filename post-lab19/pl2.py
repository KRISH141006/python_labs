import sympy as sp

z = sp.symbols('z')

H = 0.5 * (z - 0.7) * (z - 0.9) / ((z - 0.6) * (z - 0.4))

num = sp.simplify(sp.factor(sp.numer(H)))
den = sp.simplify(sp.factor(sp.denom(H)))

zeros = sp.solve(sp.Eq(num, 0), z)
poles = sp.solve(sp.Eq(den, 0), z)

print("Zeros:", zeros)
print("Poles:", poles)

stable = all(abs(p) < 1 for p in poles)

print("\nSystem Stability:", "Stable" if stable else "Unstable")
