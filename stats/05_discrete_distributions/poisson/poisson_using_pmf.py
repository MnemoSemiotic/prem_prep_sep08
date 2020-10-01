from math import e

'''
You have a coin with which you are 2 times more likely to get a heads than a tails. 
h = 2t
h + t = 1
2t + t = 1
3t = 1
t = 1/3

You flip the coin 100 times. 

What is the probability of getting exactly 25 tails?

In [3]: binomial_pmf(100, 25, (1/3))                                                     
Out[3]: 0.017777490475730268
'''




'''
Poisson Distribution
- we need to know an average number of events for a specified "volume" (time, space, or some discrete thing (number of pages))


Examples of Poisson-like phenomena

Phenomenon:
If you take photos from a camera in space, where you randomly aim the camera into space, the distribution of the counts of stars will follow a Poisson distribution.

Question:
PMF: If on average you see 120 stars clearly in a photo taking taken from a satellite, what is the probability of seeing 90 stars in a given photo?

CDF: If on average you see 120 stars clearly in a photo taking taken from a satellite, what is the probability of seeing 90 stars or less in a given photo?


Phenonemon:
Given an area of grass, it is likely that the distribution of pill bugs follows Poisson.

Question:
PMF: In a square foot of your front yard, on average there are 20 roly polys in residence. What is the probability of seeing 15 roly polys in a square foot of your front yard?


Phenomenon:
Cars passing by an intersection at a certain time of day/year for the duration of a fixed amount of time, will likely follow a Poisson distribution.

Question:
A given intersection will on average have 15 cars pass through in 10 minutes. What is the probability that 20 cars pass through in 15 minutes?


Criteria we need for Poisson:
an average for a given volume
each event needs to be independent
assumption that the rate is consistent
'''


'''
Poisson PMF
- given an average (lmbda) number of events for a given volume, get the probability of some number of events for the same or another given volume
'''

''' Factorial '''
def factorial(n):
    prod = 1

    for num in range(1, n+1):
        prod *= num

    return prod

def poisson_pmf():
    pass