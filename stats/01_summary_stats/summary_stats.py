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

house_prices = [590, 615, 575, 608, 350, 1285, 408, 540, 555, 679]

# print(sorted(house_prices))

# print(f'mean {mean(house_prices)}')
# print(f'median {median(house_prices)}')


'''
Mode
'''

def mode(lst):
    most_occurring = lst[0]

    for item in lst[0:]:
        if lst.count(item) > lst.count(most_occurring):
            most_occurring = item

    return most_occurring

mode_lst = ['writing', 'writing', 'hiking', 'painting', 'skating', 'skating', 'writing', 'macromet']

# print(mode(mode_lst))



'''
Five Number Summary
Interquartile Range
Detect Outliers
'''

def five_num_summary(lst):
    min_ = min(lst)
    max_ = max(lst)

    med = median(lst)

    sorted_lst = sorted(lst)

    print(sorted_lst)


    if len(lst) % 2 == 1:
        # [[1, 2, 5, 6, 7], 9, [12, 15, 18, 19, 27]]
        #  
        lower_half = sorted_lst[0: int(len(lst) / 2)]
        upper_half = sorted_lst[int(len(lst) / 2)+1:]
        
    else:
        # [[1, 4, 6, 7, 10, 14, 16,] [22, 24, 46, 48, 51, 54, 56]]
        #  0                   6+1 6+1                     
        lower_half = sorted_lst[0:int(len(lst) / 2)]
        upper_half = sorted_lst[int(len(lst) / 2):]

    print(lower_half)
    print(upper_half)
    q1 = median(lower_half)
    q3 = median(upper_half)

    return min_, q1, med, q3, max_

a = [15,2,9,5,6,7,27,12,18,19,1]
b = [6,1,4,51,7,16,10,14,46,22,24,56,48,54]

print(five_num_summary(a))
print(five_num_summary(b))
