'''
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.
'''

# import math

def persistence(n):
    
    str_num = str(n)
    count = 0
    
    def mathprod(list):
        product = 1
        for x in list:
            product *= x
        return product
    
    def check(input_num):
        numbers = []
        for num in str_num:
            numbers.append(int(num))
            result = mathprod(numbers)
        return str(result)
    
    while int(str_num) not in range(0,9):
        count += 1
        str_num = check(str_num)
        persistence(int(str_num))
    
    if n in range(0,9):
        return 0
    else:
        # return int(str_num)
        return count

print(persistence(999))