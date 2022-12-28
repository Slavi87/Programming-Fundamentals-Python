text = input()
final_text = ''
number = 0
for index in range(len(text)):
    if number > 0 and text[index] != '>':
        number -= 1
    elif text[index] == '>':
        final_text += text[index]
        number += int(text[index + 1])
    else:
        final_text += text[index]
print(final_text)


