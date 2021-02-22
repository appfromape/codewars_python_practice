'''
In this kata you have to create all permutations of an input string and remove duplicates, if present. This means, you have to shuffle all letters from the input in all possible orders.

Examples:

permutations('a'); # ['a']
permutations('ab'); # ['ab', 'ba']
permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
'''

from itertools import permutations as pe

def permutations(string):
    
    p = pe(string)
    # print(set(p))
    return ["".join(s) for s in (set(p))]

    # p = pe(string, len(string))
    # x = list(map(lambda x: ''.join(x), p))
    # ans = []
    # for n in range(len(x)):
    #     if x[n] not in ans:
    #         ans.append(x[n])
    
    # return ans

print(permutations("aabb"))