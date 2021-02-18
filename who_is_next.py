'''
Sheldon, Leonard, Penny, Rajesh and Howard are in the queue for a "Double Cola" drink vending machine; there are no other people in the queue. The first one in the queue (Sheldon) buys a can, drinks it and doubles! The resulting two Sheldons go to the end of the queue. Then the next in the queue (Leonard) buys a can, drinks it and gets to the end of the queue as two Leonards, and so on.

For example, Penny drinks the third can of cola and the queue will look like this:

Rajesh, Howard, Sheldon, Sheldon, Leonard, Leonard, Penny, Penny
Write a program that will return the name of the person who will drink the n-th cola.

Input:
The input data consist of an array which contains at least 1 name, and single integer n which may go as high as the biggest number your language of choice supports (if there's such limit, of course).

Output / Examples:
Return the single line — the name of the person who drinks the n-th can of cola. The cans are numbered starting from 1.

who_is_next(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 1) == "Sheldon"
who_is_next(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 52) == "Penny"
who_is_next(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 7230702951) == "Leonard"
'''

def who_is_next(names, r):
    i = 0
    mult = 1
    while True:
        for name in names:
            i += mult
            if i >= r:
                return name
            
        mult *= 2

names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]

print(whoIsNext(names, 52))

# 1, 6,7,   16,17,18,19
# 2, 8,9,   20,21,22,23 
# 3, 10,11, 24,25,26,27
# 4, 12,13, 28,29,30,31
# 5, 14,15, 32,33,34,35