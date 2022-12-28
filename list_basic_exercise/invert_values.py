numbers = input().split()
opposite_numbers = []
for i in numbers:
    current_numbers = int(i) * -1
    opposite_numbers.append(current_numbers)
print(opposite_numbers)
