numbers = input().split()
number_counter = int(input())
lst_numbers = []
for element in numbers:
    lst_numbers.append(int(element))
for i in range(number_counter):
    lst_numbers.remove(min(lst_numbers))

print(', '.join(str(j) for j in lst_numbers))
