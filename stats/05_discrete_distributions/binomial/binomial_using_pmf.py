def factorial(n):
    prod = 1

    for num in range(1, n+1):
        prod *= num

    return prod

# print(factorial(5))

def combinations(n, k):
    return int(factorial(n) / (factorial(n - k) * factorial(k)))

