from random import choice

def coin_flip():
    flip = ['H', 'T']
    return choice(flip)

print(coin_flip())