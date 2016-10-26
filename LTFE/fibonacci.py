n = 15  # Kateri Fibonaccijev člen


fibonacci = [1, 1]

# Fibonaccijevo zaporedje rešeno z WHILE zanko
while len(fibonacci) < n:
    novi = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(novi)

        
print(fibonacci)


fibonacci = [1, 1]

# Fibonaccijevo zaporedje rešeno s FOR zanko
for i in range(n - 2):
    novi = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(novi)

print(fibonacci)

print(len(fibonacci))
