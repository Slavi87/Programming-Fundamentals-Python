sequence_of_elements = [int(el) for el in input().split()]
command = input()

moves_count = 0
while command != 'end':
    current_command = command.split()
    moves_count += 1
    middle = len(sequence_of_elements) / 2
    first_index = int(current_command[0])
    second_index = int(current_command[1])
    if sequence_of_elements[first_index] == sequence_of_elements[second_index]:
        print(f"Congrats! You have found matching elements - {first_index}!")
        sequence_of_elements.pop(first_index)
        sequence_of_elements.pop(second_index)
    elif sequence_of_elements[first_index] != sequence_of_elements[second_index]:
        print('Try again!')
    elif first_index == second_index or first_index < 0 or first_index > len(sequence_of_elements)\
        or second_index < 0 or second_index > len(sequence_of_elements):
        print("Invalid input! Adding additional elements to the board")
        sequence_of_elements.insert(int(middle), moves_count)
    command = input()



