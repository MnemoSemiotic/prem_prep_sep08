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

