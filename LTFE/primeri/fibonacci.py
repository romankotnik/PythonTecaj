n = 15  # Kateri Fibonaccijev člen


fibonacci = [1, 1]

# Fibonaccijevo zaporedje rešeno z WHILE zanko
while len(fibonacci) < n:
    novi = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(novi)


print(fibonacci)
print(len(fibonacci))


fibonacci = [1, 1]

# Fibonaccijevo zaporedje rešeno s FOR zanko
for i in range(n - 2):
    novi = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(novi)

print(fibonacci)
print(len(fibonacci))


# Fibonaccijevo zaporedje rešeno rekurzivno. (Funkicija kliče samo sebe)
fibonacci = [1, 1]
def calc_fib():
    if len(fibonacci) < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
        calc_fib()

calc_fib()
print(fibonacci)
print(len(fibonacci))
