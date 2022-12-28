array = [int(el) for el in input().split()]
command = input()

while command != 'end':
    current_command = command.split()
    if current_command[0] == 'swap':
        first_index = int(current_command[1])
        second_index = int(current_command[2])
        array[first_index], array[second_index] = array[second_index], array[first_index]
    elif current_command[0] == 'multiply':
        first_index_m = int(current_command[1])
        second_index_m = int(current_command[2])
        array[first_index_m] = array[first_index_m] * array[second_index_m]
    elif current_command[0] == 'decrease':
        array = [el - 1 for el in array]
    command = input()
print(* array, sep=', ')