number_of_lines = int(input())
lst_numbers = []
COMMAND_EVEN = 'even'
COMMAND_ODD = 'odd'
COMMAND_POSITIVE = 'positive'
COMMAND_NEGATIVE = 'negative'
for i in range(number_of_lines):
    current_number = int(input())
    lst_numbers.append(current_number)
command = input()
filtered_numbers = []
for num in lst_numbers:
    filtered_passes = (
        (command == COMMAND_EVEN and num % 2 == 0) or
        (command == COMMAND_ODD and num % 2 != 0) or
        (command == COMMAND_POSITIVE and num >= 0) or
        (command == COMMAND_NEGATIVE and num < 0)
    )
    if filtered_passes:
        filtered_numbers.append(num)
print(filtered_numbers)