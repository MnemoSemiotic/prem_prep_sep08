def gen_4_bit_binary():
    bin_dct = dict()
    decimal = 0

    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    bin_dct[decimal] = [i,j,k,l]
                    decimal += 1
    return bin_dct

# for dec, bin_ in gen_4_bit_binary().items():
#     print(f'{dec}: {bin_}')


'''
7 minutes!

Code the dec_to_bin function. 
Should take as input 2 things:
    a decimal value (dec)
    a number of bits (n_bits=8)

algorithm
Given a decimal number
    - take the modulus by 2
        - set aside the result
    - floor divide the number by 2
        - until that number is 0
    - reverse the sequence of outcomes

dec_to_bin(43)
--------------
43 % 2     ==> 1
43 // 2 = 21
21 % 2     ==> 1
21 // 2 = 10
10 % 2     ==> 0
10 // 2 = 5
5 % 2      ==> 1
5 // 2  = 2
2 % 2      ==> 0
2 // 2  = 1
1 % 2      ==> 1
1 // 2  = 0

reversed ==> 101011 is the binary representation of 43
'''