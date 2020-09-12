'''
lists are indexed collections of items
'''

animal_lst = ['dog', 'cat', 'bear']
#               0      1      2 

# print(animal_lst[0])
# print(animal_lst[1])
# print(animal_lst[2])

zero, one, two = animal_lst

# print(zero)
# print(one)
# print(two)

'''
range()
get us a series of numbers from x to z (not inclusive)
'''
x = 7
z = 25
print(list(range(7, 25)))
# [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

'''
print out a list of the numbers from 24 to 364
'''
low = 24
high_incl = 364
high_excl = 365

# print(list(range(low, high_incl+1))) # communicates inclusion
# print(list(range(low, high_excl)))


'''
Generate a list of numbers from 10 to 20 (inclusive). Get the 6th item out of that list.
'''

