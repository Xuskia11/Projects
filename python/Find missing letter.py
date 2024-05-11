import string
def find_missing_letter(chars):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    
    Lower = []
    Upper = []
    for i in chars:
        if i.islower():
            Lower.append(lower.index(i))
    for i in chars:
        if i.isupper():
            Upper.append(upper.index(i))
            
    if len(Upper) != 0:
        for i in range(Upper[0],Upper[-1]):
            if i not in Upper:
                return upper[i]
            
    if len(Lower) != 0:
        for i in range(Lower[0],Lower[-1]):
            if i not in Lower:
                return lower[i]
            
print(find_missing_letter(['a','b','c','d','f']))
print(find_missing_letter((['O','Q','R','S'])))
print(find_missing_letter((['b','d'])))

            