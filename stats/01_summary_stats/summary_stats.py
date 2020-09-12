
'''
Trimmed Mean
'''

a = [1, 5, 7, 10, 15, 23, 35, 67, 220, 2000]

# print(sum(a) / len(a)) # 238.3

a_trimmed = a[1:-1]
# print(a_trimmed)
# print(sum(a_trimmed) / len(a_trimmed)) # 47.75


'''
Mean
'''
def mean(lst, trim_by=0):
    if trim_by > 0:
        lst_sorted = sorted(lst)[trim_by:-trim_by]
        sum(lst_sorted[trim_by:-trim_by]) / len(lst_sorted[trim_by:-trim_by])
    return sum(lst) / len(lst)

b = [1,2,3,4,5,6,7,8,9]
print(mean(b))
print(mean(b, trim_by=1))