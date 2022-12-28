string = input()
digits = ''
letters = ''
others = ''
for el in string:
    if el.isdigit():
        digits += el
    elif el.isalpha():
        letters += el
    else:
        others += el
print(digits)
print(letters)
print(others)
