string = input()
command = input()
while command != 'Finish':
    current_command = command.split()
    if current_command[0] == 'Replace':
        string = string.replace(current_command[1], current_command[2])
        print(string)
    elif current_command[0] == 'Cut':
        start_index = int(current_command[1])
        end_index = int(current_command[2])
        if end_index > len(string) or start_index < 0:
            print("Invalid indices!")
        else:
            string = string[:start_index + 1] + string[end_index + 2:]
            print(string)
    elif current_command[0] == 'Make':
        upper_lower = current_command[1]
        if upper_lower == 'Upper':
            string = string.upper()
            print(string)
        elif upper_lower == 'Lower':
            string = string.lower()
            print(string)
    elif current_command[0] == 'Check':
        check_text = current_command[1]
        if check_text in string:
            print(f"Message contains {check_text}")
        else:
            print(f"Message doesn't contain {check_text}")
    elif current_command[0] == 'Sum':
        index_start = int(current_command[1])
        index_end = int(current_command[2])

        if index_end > len(string) or index_start < 0:
            print("Invalid indices!")
        else:
            total_sum = 0
            new_text = string
            new_text = new_text[index_start:index_end + 1]
            for el in new_text:
                total_sum += ord(el)
            print(total_sum)
    command = input()