'''
You are given a node that is the beginning of a linked list. This list always contains a tail and a loop.

Your objective is to determine the length of the loop.

For example in the following picture the tail's size is 3 and the loop size is 11.

'''

def loop_size(node):
    
    temp = {}
    n = 0
    
    while True:
        temp[node] = n
        node = node.next
        n += 1
        if node in temp:
            return len(temp) - temp[node]
            break
