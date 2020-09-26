'''
Bernoulli trial (aka distribution)

single event with a binary outcome, with a set probability

If you have a coin that on average turns up heads in 90% of its flips, what is the probability that you'll get heads?
0.9
what is the probability that you'll get tails?
0.1
'''

from random import random
def bernoulli(p_success=0.5):
    draw = random()
    
    if draw < p_success:
        return True
    else:
        return False

print(bernoulli(p_success=0.1))