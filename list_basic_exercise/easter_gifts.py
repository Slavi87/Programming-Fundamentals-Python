name_of_gifts = input().split()
command = ''
command_lst = []
while command != "No Money":
    command = str(input()).split()
    if 'OutOfStock' in command:
        command_lst.append(command)
        removing_gift = command_lst[1]
        for element in range(len(name_of_gifts)):
            if name_of_gifts[element] == removing_gift:
                name_of_gifts[element] = 'None'
    if "Required" in command:
        command_lst.append(command)
        if len(command_lst) == 3 and isinstance(int(command_lst[2]), int):
            replace_gift = command_lst[1]
            name_of_gifts[2] = replace_gift
    if "JustInCase" in command:
        command_lst.append(command)
        replace_gift_value = command_lst[1]
        name_of_gifts[-1] = replace_gift_value

if 'None' in name_of_gifts:
    name_of_gifts.remove('None')
print(name_of_gifts)

