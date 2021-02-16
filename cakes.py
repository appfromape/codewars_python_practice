'''

Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths. Can you help him to find out, how many cakes he could bake considering his recipes?

Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and returns the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects, can be considered as 0.

# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})

'''

import math

def cakes(recipe, available):
    
    for n in range(len(list(recipe))):
        if list(recipe)[n] not in list(available):
            return 0
    
    dic = []
    
    for n in range(len(list(recipe))):
        dic.append(math.floor(available[list(recipe)[n]]/recipe[list(recipe)[n]]))
        
    return min(dic)

recipe = {'butter': 76, 'oil': 83, 'milk': 16}
available = {'chocolate': 3511, 'oil': 9040, 'apples': 9188, 'eggs': 6152, 'butter': 9352, 'crumbles': 600, 'milk': 2526, 'sugar': 5277, 'pears': 2326, 'flour': 7084}
# : 109 should equal 108

# recipe = {"flour": 500, "sugar": 200, "eggs": 1}
# available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}

# recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
# available = {"sugar": 500, "flour": 2000, "milk": 2000}

print(cakes(recipe, available))