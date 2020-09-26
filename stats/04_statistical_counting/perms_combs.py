'''
Factorial determines cardinality/magnitude of a set of outcomes
'''

def factorial(num):
    prod = 1
    for n in range(2, (num+1)) :
        prod *= n
    return prod 

