# # 1

# import sympy as sp
# # Define symbols
# n, z, a = sp.symbols('n z a')
# # Define the signal x[n] = a^n * u[n]
# x_n = a**n
# # Compute the Z-transform
# X_z = sp.summation(x_n * z**(-n), (n, 0, sp.oo))
# # Print the result
# print("Z-transform of x[n] = a^n u[n]:")
# sp.pprint(X_z, use_unicode=True)

# # 2

# import sympy as sp
# # Define symbols
# n, z, a = sp.symbols('n z a')
# # Define the signal x[n] = a^n * u[n]
# x_n = 2**n
# # Compute the Z-transform
# X_z = sp.summation(x_n * z**(-n), (n, 0, sp.oo))
# # Print the result
# print("Z-transform of x[n] = a^n u[n]:")
# sp.pprint(X_z, use_unicode=True)

# # 3

# import sympy as sp
# # Define symbols
# n, z = sp.symbols('n z')
# # Define the unit step signal u[n]
# u_n = 1
# # Compute the Z-transform
# U_z = sp.summation(u_n * z**(-n), (n, 0, sp.oo))
# # Print the result
# print("Z-transform of the unit step signal u[n]:")
# sp.pprint(U_z, use_unicode=True)

# # 4

# import sympy as sp
# # Define symbols
# n, z, alpha = sp.symbols('n z alpha')
# # Define the signal x[n] = exp(alpha * n) * u[n]
# x_n = sp.exp(alpha * n)
# # Compute the Z-transform
# X_z = sp.summation(x_n * z**(-n), (n, 0, sp.oo))
# # Print the result
# print("Z-transform of x[n] = exp(alpha * n) u[n]:")
# sp.pprint(X_z, use_unicode=True)

# # 5

# import sympy as sp
# # Define symbols
# n, z = sp.symbols('n z')
# # Define the finite sequence x[n] = {1, 2, 3}
# x_n = [1, 2, 3]
# # Compute the Z-transform manually
# X_z = sum(x_n[i] * z**(-i) for i in range(len(x_n)))
# # Print the result
# print("Z-transform of the finite sequence {1, 2, 3}:")
# sp.pprint(X_z, use_unicode=True)

# 6

import sympy as sp
# Define symbols
n, z, omega = sp.symbols('n z omega')
# Define the sinusoidal sequence x[n] = sin(omega * n) * u[n]
x_n = sp.sin(omega * n)
# Compute the Z-transform
X_z = sp.summation(x_n * z**(-n), (n, 0, sp.oo))
# Print the result
print("Z-transform of x[n] = sin(omega * n) u[n]:")
sp.pprint(X_z, use_unicode=True)
