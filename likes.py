'''
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item. It must return the display text as shown in the examples:

likes([]) # must be "no one likes this"
likes(["Peter"]) # must be "Peter likes this"
likes(["Jacob", "Alex"]) # must be "Jacob and Alex like this"
likes(["Max", "John", "Mark"]) # must be "Max, John and Mark like this"
likes(["Alex", "Jacob", "Mark", "Max"]) # must be "Alex, Jacob and 2 others like this"

'''

def likes(names):
    
    if len(names) == 0:
        return "no one likes this"
        
    elif len(names) == 1:
        name = names[0]
        return f'{ name } likes this'
        
    elif len(names) == 2:
        name1 = names[0]
        name2 = names[1]
        return f'{ name1 } and { name2 } like this'
        
    elif len(names) == 3:
        name1 = names[0]
        name2 = names[1]
        name3 = names[2]
        return f'{ name1 }, { name2 } and { name3 } like this'
        
    else:
        name1 = names[0]
        name2 = names[1]
        return f'{ name1 }, { name2 } and { len(names)-2 } others like this'


print(likes([]))