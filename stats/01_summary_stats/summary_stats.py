'''
Mean
'''

def mean(lst, trim_by=0):
    lst_ = lst.copy()
    
    if trim_by > 0:
        lst_ = sorted(lst_)[trim_by:-trim_by]
        print(lst_)
    return sum(lst_) / len(lst_)

# a = [1, 5, 7, 10, 15, 23, 35, 67, 220, 2000]

# print(mean(a, trim_by=1))



'''
Median
'''
lst1_odd = [13, 18, 13, 14, 13, 16, 14, 21, 13]
lst2_even = [15, 14, 10, 8, 12, 8, 16, 13]



def median(lst):
    lst_sorted = sorted(lst)

    # if odd
    if len(lst) % 2 == 1:
        return lst_sorted[int(len(lst) / 2)]
    # if even
    else:
        upper_idx = int(len(lst)/2)
        return mean([lst_sorted[upper_idx - 1], 
                     lst_sorted[upper_idx]])

# print(sorted(lst1_odd))
# print(median(lst1_odd))

# print()

# print(sorted(lst2_even))
# print(median(lst2_even))


'''
Housing Prices Breakout

{ 590, 615, 575, 608, 350, 1285, 408, 540, 555, 679 }

Find the mean value of the homes sold in April

Find the median value of the homes sold in April 

Do you think mean or median is a “better” measure of center for this data? why? 

'''