alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']
text = input().split()
final_sum = 0
for el in text:
    number = int(el[1:-1])
    sum_el = 0
    length_number = len(el) - 2
    if el[0].upper() in alphabet:
        if el[0].isupper():
            letter = el[0]
            alpha_num = alphabet.index(letter) + 1
            sum_el += number / alpha_num
        if el[0].islower():
            letter = el[0]
            alpha_num = alphabet.index(letter.upper()) + 1
            sum_el += number * alpha_num
    if el[-1].upper() in alphabet:
        if el[-1].isupper():
            letter = el[-1]
            alpha_num = alphabet.index(letter) + 1
            sum_el -= alpha_num
        if el[-1].islower():
            letter = el[-1]
            alpha_num = alphabet.index(letter.upper()) + 1
            sum_el += alpha_num
    final_sum += sum_el

print(f'{final_sum:.2f}')
