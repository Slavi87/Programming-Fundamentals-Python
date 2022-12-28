numbers = [int(el) for el in input().split()]
command = input()
lst = []
while command != 'end':
    current_command = command.split()
    if current_command[0] == 'exchange':
        index = int(current_command[1]) + 1
        if index > len(numbers) - 1 or index < 0:
            print("Invalid index")
        else:
            for i in range(index, len(numbers), 1):
                lst.append(numbers[i])
            lst.extend(numbers[:index])
    elif current_command[0] == 'max':
        odd_num_max = []
        even_num_max = []
        for el in range(len(lst)):
            if el % 2 != 0:
                odd_num_max.append(lst[el])
            else:
                even_num_max.append(lst[el])
        if current_command[1] == 'odd':
            odd_num_max = max(odd_num_max)


        elif current_command[1] == 'even':
            even_num_max = max(even_num_max)
    elif current_command[0] == 'min':
        odd_num_min = []
        even_num_min = []
        for el in range(len(lst)):
            if el % 2 != 0:
                odd_num_min.append(lst[el])
            else:
                even_num_min.append(lst[el])
        if current_command[1] == 'odd':
            odd_num_min = min(odd_num_min)
        elif current_command[1] == 'even':
            even_num_min = min(even_num_min)

    command = input()







