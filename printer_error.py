'''
In a factory a printer prints labels for boxes. For one kind of boxes the printer has to use colors which, for the sake of simplicity, are named with letters from a to m.

The colors used by the printer are recorded in a control string. For example a "good" control string would be aaabbbbhaijjjm meaning that the printer used three times color a, four times color b, one time color h then one time color a...

Sometimes there are problems: lack of colors, technical malfunction and a "bad" control string is produced e.g. aaaxbbbbyyhwawiwjjjwwm with letters not from a to m.

You have to write a function printer_error which given a string will return the error rate of the printer as a string representing a rational whose numerator is the number of errors and the denominator the length of the control string. Don't reduce this fraction to a simpler expression.

The string has a length greater or equal to one and contains only letters from ato z.
'''

def printer_error(s):
    
    correct_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
    error_list = []
    list_s = []
    
    for l_s in s:
        list_s.append(l_s)
    
    for n in list_s:
        if n not in correct_list:
            error_list.append(n)
    
    return f'{ len(error_list) }/{ len(list_s) }'

s="aaaxbbbbyyhwawiwjjjwwm"
print(printer_error(s))