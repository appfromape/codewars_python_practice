string = "How can mirrors be real if our eyes aren't real"

def to_jaden_case(string):
    ans = []
    for n in string.split():
        ans.append(n.capitalize())
    return " ".join(ans)

print(to_jaden_case(string))