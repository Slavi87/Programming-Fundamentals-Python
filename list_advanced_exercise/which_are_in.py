string_one = input().split(', ')
string_two = input().split(', ')
output_string = []
for el in string_one:
    for second_el in string_two:
        if el in second_el:
            output_string.append(el)
print(output_string)
