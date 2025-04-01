def arctan_approx(x):
    if not (0 <= x <= 1):
        return "Error!"

    n = 0
    approximation = 0
    error_bound = x / (2 * n + 1)

    while error_bound > 0.0001:
        term = (-1) ** n * x ** (2 * n + 1) / (2 * n + 1)
        approximation += term
        n += 1
        error_bound = x ** (2 * n + 1) / (2 * n + 1)

    return (approximation, n, error_bound)



test_values = [-1, 0, 0.25, 0.5, 0.75, 1]
for val in test_values:
    print(f"arctan_approx({val}) = {arctan_approx(val)}")
