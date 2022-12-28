text = input()
final_text = ''
last_char = ''
for el in text:
    if el != last_char:
        final_text += el
        last_char = el
print(final_text)

