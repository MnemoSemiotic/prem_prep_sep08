

'''
Random Experiment
'''

from random import choice

def coin_flip():
    flip = choice(['H', 'T'])
    return flip

print(coin_flip())