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
def binary_sampling_dict(num_bits=8, num_samples=1000):
    d = dict()

    for _ in range(num_samples):
        binary = generate_n_bits(num_bits)
        sum_bits = sum(binary)

        if sum_bits not in d:
            d[sum_bits] = 0
        d[sum_bits] += 1

    return d

''' one trial of 1000 samples '''
d = binary_sampling_dict(num_bits=8, num_samples=1000)

# for k, v in sorted(d.items()):
#     print(f'{k}: {v}')