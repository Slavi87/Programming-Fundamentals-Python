sequence_of_numbers = input().split()
left_racer = sequence_of_numbers[:int(len(sequence_of_numbers) / 2)]
right_racer = sequence_of_numbers[int(len(sequence_of_numbers) / 2) + 1:]
right_racer.reverse()
left_racer_lst = []
right_racer_lst = []
for j in left_racer:
    left_racer_lst.append(int(j))
for k in right_racer:
    right_racer_lst.append(int(k))
sum_left_racer = 0
sum_right_racer = 0
for element in left_racer_lst:
    if element == 0:
        sum_left_racer *= 0.8
    else:
        sum_left_racer += element
for element in right_racer_lst:
    if element == 0:
        sum_right_racer *= 0.8
    else:
        sum_right_racer += element
if sum_left_racer < sum_right_racer:
    print(f'The winner is left with total time: {sum_left_racer:.1f}')
else:
    print(f'The winner is right with total time: {sum_right_racer:.1f}')