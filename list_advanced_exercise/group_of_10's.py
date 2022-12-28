sequence_of_numbers = [int(el) for el in input().split(', ')]
numbers_lst = []
for el in range(1, 10 + 1):
    numbers_lst.clear()
    if len(sequence_of_numbers) != 0:
        for i in sequence_of_numbers:
            if i <= (el * 10):
                numbers_lst.append(i)
        for element in numbers_lst:
            sequence_of_numbers.remove(element)
        print(f"Group of {el * 10}'s: {numbers_lst}")

