sequence_of_numbers = [int(el) for el in input().split()]
average_number = sum(sequence_of_numbers) / len(sequence_of_numbers)
lst = []
for el in sequence_of_numbers:
    if el > average_number:
        lst.append(el)
        lst.sort()
        lst.reverse()
if len(lst) == 0:
    print('No')
elif len(lst) > 5:
    while len(lst) > 5:
        lst.pop(5)
    print(* lst, sep=' ')
else:
    print(* lst, sep=' ')