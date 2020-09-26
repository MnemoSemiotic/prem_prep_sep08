'''
Factorial determines cardinality/magnitude of a set of outcomes
'''

def factorial(num):
    prod = 1
    for n in range(2, (num+1)) :
        prod *= n
    return prod 



'''
Factorial Breakout Slide 10

There are ten people standing in a line for beignets at the world famous cafe du monde in New Orleans. How many different ways could the ten people be arranged in the queue?
>> 10! = 3628800

Given that the line was formed organically (i.e, people got into line as they arrived without any organization or coordination), what is the probability that they are standing in the queue in alphabetical order. Assume everyone has a different last name?
>> 1 / 10!
'''



'''
Permutations
P(n, k) = n! / (n - k)!
nPk
'''

'''
You have 10 students and you are conducting a science fair where 4 students will win 1st, 2nd, etc. How many different arrangements of those 4 winners is possible?

P(10, 4) = 10! / (10 - 4)!

10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
= --------------------------------------
                 6 * 5 * 4 * 3 * 2 * 1

10 * 9 * 8 * 7  = 5040

'''

'''
Code the permutations(n, k) function.

P(n, k) = n! / (n - k)!
'''
def perm(n, k):
    return int(factorial(n) / factorial(n-k))

# print(perm(10, 4))


'''Computationally better permutations func'''
# def perm(n, k):
# 	perm = 1
# 	for i in range(n, n-k, -1):
# 		perm *= i
# 	return perm


'''
Permutations intuition

Five pets, and you have 5 pet beds. What are all the ways that you arrange those five pets in their beds.
'''

base_5 = ['bat', 'cat', 'frog', 'eel', 'hamster']

animals_counting = []

for an1 in base_5:
    for an2 in base_5:
        for an3 in base_5:
            for an4 in base_5:
                for an5 in base_5:
                    animals_counting.append([an1,an2, an3, an4, an5])

# for an_number in animals_counting:
#     print(an_number)

animals_perms = []

for an_number in animals_counting:
    perm = True

    for an in an_number:
        if an_number.count(an) > 1:
            perm = False
            break
    
    if perm == True:
        animals_perms.append(an_number)


# for an_number in animals_perms:
#     print(an_number)

# print(len(animals_perms))

'''
Breakout Slide 15

There are ten participants in a road race. Gold, silver, and bronze medals will be given to first, second, and third place finishers. How many possible ways could the medals be handed out? 
10*9*8...
--------
7 * 6 * 5 ...



'''
# print(perm(10, 3)) # 720

'''

Given that the outcome of the race is determined by chance, and each runner has a unique bib number between one and ten; what is the probability that the runners with bib numbers 1, 2, and 3 finish first, second, and third, respectively?
'''
# print(1 / 720)

'''
Assume that there is a world-record holder amongst the runners in the race which is guaranteed to win, how many permutations are there for the silver and bronze medals?

9 * 8 ...
----
7 * 6 ...

72
'''

# print(perm(9, 2))



'''
Combinations
- use if order doesn't matter
- think of this as a subset of permutations

nCk = n! / ((n - k)! k!)
'''

'''
Code the comb(n, k)
'''
def comb(n, k):
    return int(factorial(n) / ((factorial(n-k) * factorial(k))))

''' how many 5 card combinations from a 52 card deck '''
# print(comb(52, 5)) # 2598960


'''
Given that there are 120 attendees at a combinatorics convention, 10 attendees will be randomly chosen to take a survey to determine the location of the following year’s convention. How many possible combinations of survey takers are there in the group of 120 attendees?
'''
# print(comb(120, 10))


