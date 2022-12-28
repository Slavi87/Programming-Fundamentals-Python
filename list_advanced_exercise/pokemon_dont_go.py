sequence_of_numbers = [int(el) for el in input().split()]
result = []
while sequence_of_numbers:
    index = int(input())
    removed_nums = ''
    if index < 0:
        removed_nums = sequence_of_numbers.pop(0)
        sequence_of_numbers.insert(0, sequence_of_numbers[-1])
    elif index >= len(sequence_of_numbers):
        removed_nums = sequence_of_numbers.pop(-1)
        sequence_of_numbers.append(sequence_of_numbers[0])
    if not removed_nums:
        removed_nums = sequence_of_numbers.pop(index)
    result.append(removed_nums)
    for pos, pokemon in enumerate(sequence_of_numbers):
        if pokemon <= removed_nums:
            sequence_of_numbers[pos] += removed_nums
        else:
            sequence_of_numbers[pos] -= removed_nums
print(sum(result))

