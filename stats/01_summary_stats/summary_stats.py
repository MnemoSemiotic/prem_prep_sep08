
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
        return sum(lst_sorted) / len(lst_sorted)
    return sum(lst) / len(lst)

b = [1,2,3,4,5,6,7,8,9]
# print(mean(b))
# print(mean(b, trim_by=1))

'''
Mean Breakout
'''

urban = 6.0, 5.0, 11.0, 33.0, 4.0, 5.0, 80.0, 18.0, 35.0, 17.0, 23.0
farmhouse = 4.0, 14.0, 11.0, 9.0, 9.0, 8.0, 4.0, 20.0, 5.0, 8.9, 21.0, 9.2, 3.0, 2.0, 0.3

# print(f'Urban endotoxin mean: {mean(urban)}')
# print(f'Farmhouse endotoxin mean: {mean(farmhouse)}')

# print(f'Urban endotoxin mean trimmed(1): {mean(urban, trim_by=1)}')
# print(f'Farmhouse endotoxin mean trimmed(1): {mean(farmhouse, trim_by=1)}')

'''
Median
x_med = ?
'''

