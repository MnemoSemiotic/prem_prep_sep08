'''
Geometric Distribution
- models the number of failures up to the first success
    - two formulas
        - up to but not including the first success
        - up to and including the first success

k will represent the # of failures (inclusive or exclusive of the first success)

0000001
001
0000000000001

You are handing out fliars for a show. The probability of someone accepting a fliar is 0.65. What is the probability that the first person who accepts a fliar is the 3rd person you offer a fliar?
'''


'''
Write the geometric_pmf function. 
This will 3 parameters:
p : probability
k : number of failure (inclusive or exclusive of the 1st success)
inclusive=True : whether or not to use the inclusive or exclusive form
'''
def geometric_pmf(p, k, inclusive=True):
    if inclusive:
        return p * (1-p)**(k-1) 
    else:
        return p * (1-p)**k 

'''
You are flipping a fair coin. What is the probability that
you get your first heads on the 7th flip?
'''
# print(geometric_pmf(0.5, 7, inclusive=True))
# print(geometric_pmf(0.5, 6, inclusive=False))


'''
A roofer hits their thumb with a hammer 1/1000 times when they swing the hammer. What is the probability that the roofer will first hit their thumb after swinging the hammer 37 times (hits on the 38th)?
'''
# print(geometric_pmf((1/1000), 38, inclusive=True))
# print(geometric_pmf((1/1000), 37, inclusive=False))

