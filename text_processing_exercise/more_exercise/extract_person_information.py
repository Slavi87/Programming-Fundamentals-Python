number = int(input())
name_first_index = 0
name_second_index = 0
age_first_index = 0
age_second_index = 0
name = ''
age = ''
for i in range(number):
    sentence = input()
    for el in range(len(sentence)):
        if sentence[el] == '@':
            name_first_index = el
        elif sentence[el] == '|':
            name_second_index = el
        elif sentence[el] == '#':
            age_first_index = el
        elif sentence[el] == '*':
            age_second_index = el
    for el in sentence[name_first_index + 1:name_second_index]:
        name += el
    for el in sentence[age_first_index + 1:age_second_index]:
        age += el
    print(f'{name} is {age} years old.')
    name = ''
    age = ''