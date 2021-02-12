'''

The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 

'''

def duplicate_encode(word):
    
    upper_word = word.upper()
    word_list = []
    new_list = []
    same_list = set([x for x in upper_word if upper_word.count(x) > 1])
    
    for n in upper_word:
        word_list.append(n)
        
    for i in range(len(word_list)):
        
        if word_list[i] in same_list:
            new_list.append(")")
            
        else:
            new_list.append("(")
    
    return "".join(new_list)

print(duplicate_encode("Success"))