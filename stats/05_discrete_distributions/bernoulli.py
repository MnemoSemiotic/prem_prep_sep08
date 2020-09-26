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

trials = 1000000
# print([bernoulli(p_success=0.5) for _ in range(trials)].count(True) / trials)


'''
A Binomial Distribution is a series of Bernoulli Trials, where we keep a fixed probability p.

How many ways can you arrange 1 1 in 5-bit binary?
00001
00010
00100
01000
10000

How many ways can you arrange 2 1s in 5-bit binary?
00011
00101
01001
10001
00110
01010
...

'''