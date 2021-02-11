'''
Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.
'''

def descending_order(num):
    
    str_num = list(str(num))
    sort_num = sorted(str_num, key=int, reverse=True)
    join_num = ''.join(str(n) for n in sort_num)
    
    return int(join_num)

print(descending_order(42145))