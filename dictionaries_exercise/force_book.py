command = input()
my_dict = {}
while command != 'Lumpawaroo':
    if '|' in command:
        data = command.split(' | ')
        side = data[0]
        user = data[1]
        if side not in my_dict:
            my_dict[side] = []
        for value in my_dict.values():
            if user in my_dict[side]:
                break
            else:
                my_dict[side].append(user)
    elif '->' in command:
        data = command.split(' -> ')
        side = data[1]
        user = data[0]
        if side not in my_dict:
            my_dict[side] = []
        for value in my_dict.values():
            if user in value:
                value.remove(user)
        my_dict[side].append(user)
        print(f"{user} joins the {side} side!")
    command = input()
for key, value in my_dict.items():
    if len(my_dict[key]) == 0:
        continue
    else:
        print(f"Side: {key}, Members: {len(value)}")
        for v in value:
            print(f'! {v}')