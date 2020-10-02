from geometric_using_pmf import *

'''
Geometric Breakout 1
Suppose you have an unfair coin, with a 68% chance of getting tails. 
What is the probability that the first head will be on the 3rd trial?
'''

print(geometric_pmf(p=0.32, k=3, inclusive=True))