

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

print(union_mult_sets(list1, list2, list3))