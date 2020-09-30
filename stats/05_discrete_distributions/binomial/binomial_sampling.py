from random import choice

def get_bit():
    return choice([0, 1])

def generate_n_bits(n=8):
    lst = []
    for _ in range(n):
        lst.append(get_bit())

    return lst

# print(generate_n_bits(12))

'''
Write a function called binary_sampling_dict that has two parameters
    num_bits
    num_samples

return a dictionary where the keys represent the number of successes, and the values associated with those keys represent the count of that number of successes occurring
'''