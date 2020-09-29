from random import choice, random

'''
Random Variable
* results of some experiment
    * consider every potential outcome of an experiment
    * imagine running that experiment quasi-infinite number of times
        * should arrive at some set of parameters that define the distribution of the outcomes of that Random Variable
        * flip a coin an infinite - 1 number of times, if you divide the number of outcomes of Heads by infinite - 1, then you should have ~0.5

'''

'''
Consider a random variable Y.
    Y represents the outcome of a single roll of a 6-sided die
    Y = {1, 2, 3, 4, 5, 6}

What is the probability that Y has an even outcome?
0.5
'''

# roll a die
die_possibilities = [1,2,3,4,5,6]

Y_1 = choice(die_possibilities) # <- single experiment
Y_2 = choice(die_possibilities)
Y_3 = choice(die_possibilities)

# print(Y_1)
# print(Y_2)
# print(Y_3)

'''
X is a random variable that follows these rules:
X = 1 if the roll of a 6-sided die has an even count of pips
X = 0 if the roll of a 6-sided die has an odd count of pips
'''
def get_X():
    if choice(die_possibilities) % 2 == 0:
        return 1
    else:
        return 0



'''
Bernoulli trial (aka distribution)

single event with a binary outcome, with a set probability

If you have a coin that on average turns up heads in 90% of its flips, what is the probability that you'll get heads?
0.9
what is the probability that you'll get tails?
0.1
'''

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

The Binomial Distribution Question:
If you have n Bernoulli trials in a row, what is the probability that k of them are successful?

You flip a coin 20 times. What is the probability that get 14 heads out of 20 flips?
0000001111111111111...
1111111100000000.....
...

'''