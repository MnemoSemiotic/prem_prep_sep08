from random import random

def bernoulli(p=0.5):
    if random() < p:
        return 1
    return 0


def perform_geometric(p=0.5):
    num_trials = 1

    for _ in range(20000):
        flip = bernoulli(p)
        num_trials += 1
        if flip == 1:
            break
        # print(f'trial: {flip}')
    
    print(f'Success on the {num_trials+1} trial!')

# perform_geometric(p=0.05)


def geometric(p=0.5):
    # num of failures prior to the first success
    lst = []

    for _ in range(1000000000):
        trial = bernoulli(p)
        lst.append(trial)

        if trial == 1:
            break

    return len(lst) - 1

print(geometric(p=0.05))