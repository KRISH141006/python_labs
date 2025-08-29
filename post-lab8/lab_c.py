import math

def evaluate_functions(x):
    f = math.cos(2 * x)
    f_prime = -2 * math.sin(2 * x)
    f_double_prime = -4 * math.cos(2 * x)
    return f, f_prime, f_double_prime

# Evaluate at x = π
x = math.pi
results = evaluate_functions(x)
print(f"f(x) = {results[0]}")
print(f"f'(x) = {results[1]}")
print(f"f''(x) = {results[2]}")
