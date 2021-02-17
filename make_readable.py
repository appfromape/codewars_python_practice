'''
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
'''

import math

def make_readable(seconds):
    
    h = math.floor(seconds / 3600)
    m = math.floor((seconds-(h*3600)) / 60)
    s = seconds % 60
    
    if 9 < h < 100:
        h = math.floor(seconds / 3600)
    else:
        h = f'0{ math.floor(seconds / 3600) }'
        
    if 9 < m < 60:
        m = math.floor((seconds-(h*3600)) / 60)
    else:
        m = f'0{ math.floor((seconds-(h*3600)) / 60) }'
        
    if 9 < s < 60:
        s = seconds % 60
    else:
        s = f'0{ math.floor(seconds % 60) }'
    
    return f"{ h }:{ m }:{ s }"


print(make_readable(86399))
