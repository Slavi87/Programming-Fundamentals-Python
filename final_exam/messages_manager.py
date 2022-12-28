capacity_of_possible_messages_per_user = int(input())
command = input()
my_dict = {}
while command != 'Statistics':
    current_command = command.split('=')
    if current_command[0] == 'Add':
        name = current_command[1]
        sent_messages = int(current_command[2])
        received_messages = int(current_command[3])
        if name not in my_dict:
            my_dict[name] = []
        my_dict[name] = [sent_messages, received_messages]
    elif current_command[0] == 'Message':
        sender = current_command[1]
        receiver = current_command[2]
        if sender not in my_dict or receiver not in my_dict:
            continue
        else:
            if sender in my_dict:
                my_dict[sender][0] += 1
                for value in my_dict.values():
                    if sum(value) >= capacity_of_possible_messages_per_user:
                        print(f"{sender} reached the capacity!")
                        del my_dict[sender]
                        break
            if receiver in my_dict:
                my_dict[receiver][1] += 1
                for v in my_dict.values():
                    if sum(v) >= capacity_of_possible_messages_per_user:
                        print(f"{receiver} reached the capacity!")
                        del my_dict[receiver]
                        break
    elif current_command[0] == 'Empty':
        user = current_command[1]
        if user == 'All':
            my_dict.clear()
        elif user in my_dict:
            del my_dict[user]
    command = input()
print(f"Users count: {len(my_dict)}")
for key, value in my_dict.items():
    print(f'{key} - {sum(value)}')


