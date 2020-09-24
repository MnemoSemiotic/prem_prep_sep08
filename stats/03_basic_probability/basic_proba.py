from random import choice

def coin_flip():
    flip = ['H', 'T']
    return choice(flip)

# print(coin_flip())

'''
Write a function called series_of_flips, that has one parameter, n, which represents the number of coin flips. Return a list of the random coin flips.

['H', 'H', 'T', 'H']
'''
def series_of_flips(n):
    flips = []
    for _ in range(n):
        flips.append(coin_flip())
    return flips

# print(series_of_flips(4))

'''
Write a function called four_flip_sample_space that has no parameters. It should return a list of all possible outcomes for 4 coin flips.

[
    ['H', 'H', 'H', 'H'],
    ['H', 'H', 'H', 'T'],
    ['H', 'H', 'T', 'H']
    ...
    ['T', 'T', 'T', 'T']
]
'''
def four_flip_sample_space():
    flip = ['H', 'T']
    outcomes = []

    for f1 in flip:
        for f2 in flip:
            for f3 in flip:
                for f4 in flip:
                    outcomes.append([f1, f2, f3, f4])
    
    return outcomes


'''
What is the probability that in 4 coin flips, you get 3 heads?

A = THHH
    HTHH
    HHTH
    HHHT

S = len(outcomes)
'''

four_flips = four_flip_sample_space()

three_heads = []

for lst in four_flips:
    if lst.count('H') == 3:
        three_heads.append(lst)

# print(len(three_heads))
# print(len(four_flips))
# print(len(three_heads) / len(four_flips))



'''
What is in one coin flip, that you get a heads?
   P(H) = ?
T
H <--

In two coin flips, what is the P of getting both heads?
TT
TH
HT
HH <--

In three coin flips, what is the P of getting all heads?
TTT
TTH
THT
THH
HTT
HTH
HHT
HHH <--


Suppose you call the function series_of_flips(14). What is the probability that you 
will get all 'H' values?
(1/2)**14

What is the probability of getting this series of outcomes in 6 coin flips:
HTTHTH ?

(1/2)**6

What is the probability of getting 3 heads in 6 coin flips?
(need to either understand the cardinality of the subset and the superset OR, we use the binomial pmf)
'''


'''
In three six-sided dice rolls, what is the probability of getting a sum of the three rolls below 6?
'''

outcomes = []
for r1 in range(1, 6):
    for r2 in range(1, 6):
        for r3 in range(1, 6):
            outcomes.append([r1, r2, r3])

A = []

for rolls in outcomes:
    if sum(rolls) < 6:
        A.append(rolls)

# print(len(A) / len(outcomes)) # 0.08

'''
What is the probability of getting three 6's when rolling 3 6-sided dice?

(1/6)**3
'''



'''
Dependence:

What is the probability of choosing an ace of spades from a 52 card deck?
1/52

Given that the prior event has occurred, what is the P(Queen of Hearts)?
1/51
'''


'''
Multiplication Rule

If you have a series of independent events, say flipping a coin... you can calc a probability of that series of events occurring in a specific order by simply multiplying the probability of each event.

you flip a coin 7 times, what is the probability of getting 
HHTHTTT --> 0.5**7
'''