targets_values = [int(el) for el in input().split()]

command = input()
new_lst = [-1]

while command != 'End':
    value = 0
    for element in targets_values:
        value = targets_values[0]
        if element == targets_values[1]:
            new_lst.append(element - value)
            targets_values.pop(1)

    command = input()
print(new_lst)


NOT
