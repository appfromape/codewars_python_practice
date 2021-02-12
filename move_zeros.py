'''
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
'''

def move_zeros(array):
    
    new_array = []
    zero_array = []
    
    for n in range(len(array)):
        if str(array[n]) != False and str(array[n]) != "0" and str(array[n]) != "0.0" or array[n] == "0":
            new_array.append(array[n])
        else:
            zero_array.append(array[n])
    
    return new_array + zero_array


print(move_zeros([9, -8, 'a', 1, -6, 0, 0, 0, -10, 2, False, -7, 3, 0, 'x', 9, 'y', 0, 'y', '0', 'y', 0, 9, 3, False, 'string']))