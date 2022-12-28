wagons = int(input())
train = [0] * wagons
command = input()
while command != 'End':
    current_command = command.split()
    if current_command[0] == 'add':
        train[-1] += int(current_command[1])
    elif current_command[0] == 'insert':
        index = int(current_command[1])
        num_people = int(current_command[2])
        train[index] += int(num_people)
    elif current_command[0] == 'leave':
        index = int(current_command[1])
        num_people = int(current_command[2])
        train[index] -= int(num_people)
    command = input()
print(train)