from random import choice

def coin_flip():
    flip = ['H', 'T']
    return choice(flip)

# print(coin_flip())

'''
Write a function called series_of_flips, that has one parameter, n, which represents the number of coin flips. Return a list of the random coin flips.

['H', 'H', 'T', 'H']
'''