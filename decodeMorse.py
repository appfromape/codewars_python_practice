

MORSE_CODE = {
    ".-" : "a",
    "-..." : "b",
    "-.-." : "c",
    "-.." : "d",
    "." : "e",
    "..-." : "f",
    "--." : "g",
    "...." : "h",
    ".." : "i",
    ".---" : "j",
    "-.-" : "k",
    ".-.." : "l",
    "--" : "m",
    "-." : "n",
    "---" : "o",
    ".--." : "p",
    "--.-" : "q",
    ".-." : "r",
    "..." : "s",
    "-" : "t",
    "..-" : "u",
    "...-" : "v",
    ".--" : "w",
    "-..-" : "x",
    "-.--" : "y",
    "--.." : "z",
    "   " : " "
}

# def decodeMorse(morse_code):
#     # ToDo: Accept dots, dashes and spaces, return human-readable message
#     return morse_code.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-']).replace(' ', '')


def decodeMorse(morse_code):
    
    ans = ''
    
    for x in morse_code.strip().split('   '):
        for y in x.split(' '):
            ans += MORSE_CODE[y]
        ans += ' '
    return ans.upper()

print(decodeMorse('.... . -.--   .--- ..- -.. .'))
#should return "HEY JUDE"