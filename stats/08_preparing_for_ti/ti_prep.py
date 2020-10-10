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
# print(binomial_pmf(n=10, k=5, p=(7/22)))
# 0.121

'''
** watch for keywords: ALL, NONE, AT LEAST/LESS THAN

If on average 20 of 50 counties in California experience wildfires during any given year, what is the prob that all 50 counties will see a wildfire in a single year?
Constraint: massive invisible/fireproof wall betw each county

p = 20/50
n = 50
k = 50
'''
# print(binomial_pmf(n=50, k=50, p=(20/50)))
# print((20/50)**50)
# # 1.2676506002282329e-20



'''
you are at the bus stop and 4 out of every 15 buses that pass by have a subway add, if you watch 30 buses pass by what are the chances that 12 of them will have a subway add?

p = 4/15
n = 30
k = 12
'''
# print(binomial_pmf(n=30, k=12, p=(4/15)))
# 0.042


'''
Walking your dog on any given day, on average 2 out of 5 dogs you pass are golden retrievers. If you see 17 dogs on one particular day, what is the probability that 8 of them are golden retrievers?

p = 2/5
n = 17
k = 8

'''
# print(binomial_pmf(n=17, k=8, p=(2/5)))


'''
You are looking for the stray cats (no name tag cats) in your neighborhood. On average, three out of every 20 cats have no name tags walk through your house. What is the probability that, in one particular set of observations, five no name tag cats out of 10 cats walk by your house?

p = 3/20
n = 10
k = 5
'''

# print(binomial_pmf(n=10, k=5, p=(3/20)))



'''

Poisson textbook problems
'''
from math import e
def poisson_pmf(lmbda, k):
    return lmbda**k * e**(-lmbda) / factorial(k)


'''
Forty stray cats walk by your porch every 2 hours at night. What is the probability that fifty stray cats walk by in 3 hours on a given night?
Constraints: time of night, seasonality, prior cats doesn't affect rate

'''
# lmbda = 60 # 40 * 3/2
# k = 50

# print(poisson_pmf(lmbda, k))
# # 0.023


'''
if on average 3 mosquitos bite you every 30 min while you’re fishing, what is the probability that 7 mosquitos bite you in 3 hours?
'''
# lmbda = 3 * 6
# k = 7
# print(poisson_pmf(lmbda, k))
# # 0.00185

'''
you eat (on avg) 10 chocolates per hour.  what is the probably you eat 20 chocolates in 45 minutes from your 10 boxes of chocolates
'''
# lmbda = 10 * (3/4)
# k = 20
# print(poisson_pmf(lmbda, k))
# # 7.209282379462172e-05


'''
You go for a walk every day at noon. On a 30 minute walk, on avg, you see 3 magpies. If you go for a walk that is an hour and 15 minutes, what is the probably that you will see 11 magpies?
'''
# lmbda = 3 * 2.5
# k = 11
# print(poisson_pmf(lmbda, k))
# # 0.0585

'''
10 dogs are saved from the shelter every 8 hours on average. What is the probability that 25 dogs would be saved in 16 hours?
'''
lmbda 10 * 2
k = 25
print(poisson_pmf(lmbda, k))

'''

Random Variables

'''


'''

Coding Mathematical Formulations

'''


'''

Analysis using Dictionaries

'''