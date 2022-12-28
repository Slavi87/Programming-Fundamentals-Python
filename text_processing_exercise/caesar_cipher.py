text = input()
new_text = ''
for char in text:
    ch = ord(char)
    new_text += chr(ch + 3)
print(new_text)