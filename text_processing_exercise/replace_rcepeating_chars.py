sequence = input()
new_sequence = ''
last_letter = ''
for i in sequence:
    if i != last_letter:
        new_sequence += i
        last_letter = i


print(new_sequence)