'''
Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true

0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore, the input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).

'''

def valid_parentheses(string):
    
    count = 0
    
    for s in string:
        
        if s == '(':
            count += 1
            
        if s == ')':
            count -= 1
            
        if count < 0: 
            return print(False)
    
    if count == 0:
        print(True)
    
    else:
        print(False)

valid_parentheses("()()")