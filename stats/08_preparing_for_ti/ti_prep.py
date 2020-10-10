''' TI Style Questions (2020-10-10) '''

'''

TI Skills/Outline

* textbook problems re: Discrete Distrs
    * Recognize and solve problems related to:
        * Binomial
        * Poisson
        * Geometric
        * Uniform
    
    * Understanding counting or binary through the lens of independent trials
        * binary ex: [0,1,1,0,1] <- each "coin flip or bit is independent of the other, if each bit is randomly generated"
        * trinary ex: [0, 1, 1, 2, 0]

    * Coding mathematical formulations

    * Analysis through Dictionaries
        * Pack values into dictionaries
            * Check membership vs not checking membership
        * Transform Dictionary values
        * General analytic approach
            * Create generative process
            * Load results into a dict
            * Interpret
'''



'''
Binomial textbook problems

You are sitting on a dock watching boats go by. On average, two out of every 13 boats that goes by has shipping containers on it. What is the probability that, in one particular set of observations, 10 out of 20 boats have shipping containers on them?

p = 2/13
k = 10
n = 20

binomial_pmf(n=20, k=10, p=(2/13) )
'''
def factorial(n):
    prod = 1
    for num in range(1, 1+n):
        prod *= num
    return prod

def combinations(n, k):
    return int(factorial(n) / (factorial(n-k) * factorial(k)))

def binomial_pmf(n, k, p=0.5):
    return combinations(n, k) * (p**k) * ((1-p)**(n-k))


# print(binomial_pmf(n=20, k=10, p=(2/13)))
# 0.000258


'''
you are sitting on a bench holding ten boxes of chocolates. your boxes of chocolates have 7 caramel, 10 coconut, and 5 toffee in each.  what are the odds you pick 10 chocolates from 10 different boxes of chocolates and get 5 caramel filled chocolates?

total_choc = 22
p_caramel = 7/22
k = 5
n = 10
'''
print(binomial_pmf(n=10, k=5, p=(7/22)))





'''

Poisson textbook problems

'''


'''

Random Variables

'''


'''

Coding Mathematical Formulations

'''


'''

Analysis using Dictionaries

'''