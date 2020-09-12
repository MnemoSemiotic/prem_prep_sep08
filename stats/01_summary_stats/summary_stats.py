
'''
Trimmed Mean
'''

a = [1, 5, 7, 10, 15, 23, 35, 67, 220, 2000]

print(sum(a) / len(a)) # 238.3

a_trimmed = a[1:-1]
# print(a_trimmed)
print(sum(a_trimmed) / len(a_trimmed)) # 47.75



