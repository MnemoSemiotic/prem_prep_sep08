

'''
Random Experiments
'''

from random import choice

def coin_flip():
    flip = choice(['H', 'T'])
    return flip

# 20 flips
twenty_flips = []

for _ in range(20):
    twenty_flips.append(coin_flip())

# print(twenty_flips.count('H'))
# print(twenty_flips.count('T'))


def die_roll(sides=6):
    return choice(range(1, sides+1))

# sum of 20 die rolls
twenty_rolls = []
for _ in range(20):
    twenty_rolls.append(die_roll())

# print(sum(twenty_rolls))


'''
For the moment, consider the set() type in python to be a way to remove duplicates
from lists
'''

# list/set trick for deduping (doesn't maintain order)
# s1 = list(set([7,8,9,0,1,2,3,4,7,8,9,0]))
# s2 = list(set([7,8,9,0,2,3]))

# print(s1)
# print(s2)

# Sets do not maintain order
[0, 1, 2, 3, 4, 7, 8, 9]
[0, 2, 3, 7, 8, 9]


# maintain order with a dedupe function
s1 = [7,8,9,0,1,2,3,4,7,8,9,0]
s2 = [7,8,9,0,2,3]

def dedupe(lst):
    deduped_inorder = []
    for element in lst:
        if element not in deduped_inorder:
            deduped_inorder.append(element)
    return deduped_inorder

# print(dedupe(s1))
# print(dedupe(s2))

# maintained order
[7, 8, 9, 0, 1, 2, 3, 4]
[7, 8, 9, 0, 2, 3]



'''
Star (*) Args

'''
def star_args(*args):
    for item in args:
        print(item)
    return None

# star_args('hi', 56, int, [1,2,34,5,6])



'''
Union
'''

list1 = ['bear', 'cat', 'dog', 'dolphin', 'weasel']
list2 = ['bear', 'dog', 'elephant', 'weasel', 'mink', 'mountain lion']
list3 = ['bear', 'whale', 'sea cucumber', 'mink', 'eagle', 'dog']


def union(set1, set2):
    set_union = set1.copy()
    for item in set2:
        if item not in set_union:
            set_union.append(item)
    return set_union

# print(union(list1, list2))
['bear', 'cat', 'dog', 'dolphin', 'weasel', 'elephant', 'mink', 'mountain lion']


def union_mult_sets(*args):
    set_union = []

    for lst in args:
        for item in lst:
            if item not in set_union:
                set_union.append(item)
    return set_union

# print(union_mult_sets(list1, list2, list3))
['bear', 'cat', 'dog', 'dolphin', 'weasel', 'elephant', 'mink', 'mountain lion', 'whale', 'sea cucumber', 'eagle']



'''
Breakout Slide 8

'''

# Write out the sample space for the random experiment which is defined as sequentially completing the following steps:
# First, rolling a fair four-sided die
# Then, flipping a coin
# And finally, flipping the coin a second time
# 	{1HH, 1HT, 1TH ...

four_sided = [1,2,3,4]
fair_coin = ['H', 'T']

samp_space = []

for roll in four_sided:
    for flip1 in fair_coin:
        for flip2 in fair_coin:
            samp_space.append([roll, flip1, flip2])

# for outcome in samp_space:
#     print(outcome)


# List the sample points in the following events:
# A = The event in which the die roll results in exactly one pip showing
A = []
for outcome in samp_space:
    if outcome[0] == 1:
        A.append(outcome)

# print(A)
[[1, 'H', 'H'], [1, 'H', 'T'], [1, 'T', 'H'], [1, 'T', 'T']]


# B = The event in which at least one of the coin flips results in heads
B = []
for outcome in samp_space:
    if outcome.count('H') >= 1:
        B.append(outcome)
# print(B)
[[1, 'H', 'H'], [1, 'H', 'T'], [1, 'T', 'H'], [2, 'H', 'H'], [2, 'H', 'T'], [2, 'T', 'H'], [3, 'H', 'H'], [3, 'H', 'T'], [3, 'T', 'H'], [4, 'H', 'H'], [4, 'H', 'T'], [4, 'T', 'H']]

# List the sample points which are in the Union of events A and B from above
# print(union(A, B))
[[1, 'H', 'H'], [1, 'H', 'T'], [1, 'T', 'H'], [1, 'T', 'T'], [2, 'H', 'H'], [2, 'H', 'T'], [2, 'T', 'H'], [3, 'H', 'H'], [3, 'H', 'T'], [3, 'T', 'H'], [4, 'H', 'H'], [4, 'H', 'T'], [4, 'T', 'H']]




'''
Intersection
shared, not mutually exclusive elements
'''

list1 = ['bear', 'cat', 'dog', 'dolphin', 'weasel']
list2 = ['bear', 'dog', 'elephant', 'weasel', 'mink', 'mountain lion']
list3 = ['bear', 'whale', 'sea cucumber', 'mink', 'eagle', 'dog']


def intersection(set1, set2):
    set_intersect = []

    for item in set1:
        if item in set2:
            set_intersect.append(item)

    return set_intersect

# print(intersection(list1, list2))


def intersection_mult(*args):
    set_intersect = []

    if len(args) > 0:
        for item in args[0]:
            flag = True
            for set_ in args[1:]:
                if item not in set_:
                    flag = False
                    break
            if flag == True:
                set_intersect.append(item)
        return set_intersect
    else:
        return set_intersect

# print(intersection_mult())
[]  

# print(intersection_mult(list1, list2, list3))
['bear', 'dog']


