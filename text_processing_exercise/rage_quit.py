text = input()
string = list(text)
current_string = ''
final_string = ''
final = ''
final_sequence = 0
last_symbol_is_num = False
for el in string:
    num = 0
    if el.isdigit():
        index = int(string.index(el))
        if text[-1].isdigit():
            last_symbol_is_num = True
            string.append('a')
            if (string[index + 1]).isdigit():
                second_num = string[index + 1]
                num = int(el + second_num)
            elif not (string[index + 1]).isdigit():
                num = int(el)
        else:
            if (string[index + 1]).isdigit():
                second_num = string[index + 1]
                num = int(el + second_num)
            elif not (string[index + 1]).isdigit():
                num = int(el)
        final_string += current_string * num
        current_string = ''
    elif el.isalpha():
        if el.islower():
            current_string += el.upper()
        else:
            current_string += el
    elif el != el.isdigit() and el != el.isalpha():
        current_string += el
if last_symbol_is_num:
    final_sequence = final_string
else:
    final_sequence = final_string + current_string
for i in final_sequence:
    if i not in final:
        final += i
unique_symbols = len(final)
print(f'Unique symbols used: {unique_symbols}')
print(final_sequence)
