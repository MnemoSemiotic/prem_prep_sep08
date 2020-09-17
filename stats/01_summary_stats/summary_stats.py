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

print(sorted(lst1_odd))
print(sorted(lst2_even))

