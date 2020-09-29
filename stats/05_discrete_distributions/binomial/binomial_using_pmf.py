def factorial(n):
    prod = 1

    for num in range(1, n+1):
        prod *= num

    return prod

# print(factorial(5))

def combinations(n, k):
    return int(factorial(n) / (factorial(n - k) * factorial(k)))



'''
PMF: Probability Mass Function
- giving us the probability of a certain specific outcome.
- can answer the binomial question:
- 3 params:
    n : number of trials
    k : represents the number of successes
    p : is the probability of success of a single trial
'''

def binomial_pmf(n, k, p=0.5):
    return combinations(n, k) * (p**k) * (1-p)**(n-k)

'''
"What is the probability in 12 coin flips of a fair coin, that you get 7 heads?"
'''
binomial_pmf(12, 7, p=0.5)


'''
"You have 14 components in a circuit. At any given time, there is a 95% chance that a given component is functioning. What is the probability that 12 components are functioning?"
'''