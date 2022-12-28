key = int(input())
number_of_lines = int(input())
message = 0
for current_digit in range(1, number_of_lines + 1):
    digit = input()
    message = ord(digit) + key
    message = chr(message)
    print(message, end="")
