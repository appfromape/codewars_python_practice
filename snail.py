'''
Given an n x n snail_map, return the snail_map elements arranged from outermost elements to the middle element, traveling clockwise.

snail_map = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(snail_map) #=> [1,2,3,6,9,8,7,4,5]

For better understanding, please follow the numbers of the next snail_map consecutively:

snail_map = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(snail_map) #=> [1,2,3,4,5,6,7,8,9]

NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d snail_map in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty snail_map inside an snail_map [[]].
'''


def snail(snail_map):
    
    temp_list = []
    
    if len(snail_map) > 1:
        if isinstance(snail_map[0], list):
            temp_list.extend(snail_map[0])
        else:
            temp_list.append(snail_map[0])
            
        snail_map.pop(0)
        
        for lis_index in range(len(snail_map)):
            temp_list.append(snail_map[lis_index][-1])
            snail_map[lis_index].pop(-1)
            
        if isinstance(snail_map[-1], list):
            temp_list.extend(snail_map[-1][::-1])
        else:
            temp_list.append(snail_map[-1])
            
        snail_map.pop(-1)
        
        for lis_index in range(len(snail_map)):
            temp_list.append(snail_map[::-1][lis_index][0])
            snail_map[::-1][lis_index].pop(0)
            
        temp_list.extend(snail(snail_map))
        
        return temp_list
    
    elif snail_map:
        return snail_map[0]
    
    else:
        return []

# snail_map = [
    
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
    
#     ]

snail_map = [
    
    [1,2,3,4],
    [12,13,14,5],
    [11,16,15,6],
    [10,9,8,7]
    
    ]

# snail_map = [
    
#     [1]
    
#     ]

# snail_map = [
    
#     []
    
#     ]

print(snail(snail_map))