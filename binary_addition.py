'''
Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be a string.

'''

def add_binary(a,b):
    int_sum = a + b
    binary_int_sum = int("{0:b}".format(int_sum))
    return str(binary_int_sum)

print(add_binary(1,1))