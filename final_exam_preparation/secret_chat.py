hidden_message = input()
command = input()
while command != 'Reveal':
    current_command = command.split(':|:')
    if current_command[0] == 'InsertSpace':
        index = int(current_command[1])
        hidden_message = hidden_message[:index] + ' ' + hidden_message[index:]
    elif current_command[0] == 'Reverse':
        part = current_command[1]
        reversed_part = part[::-1]
        if part in hidden_message:
            hidden_message.replace(current_command[1], current_command[1][::-1])
    elif current_command[0] == 'ChangeAll':
        char_to_remove = current_command[1]
        char_to_insert = current_command[2]
        hidden_message = list(hidden_message)
        for ch in hidden_message:
            if ch == char_to_remove:
                index_char = hidden_message.index(ch)
                hidden_message.remove(ch)
                hidden_message.insert(index_char, char_to_insert)
        hidden_message = ''.join(hidden_message)
    command = input()
print(hidden_message)



