number_of_chars = int(input())
total_sum = 0
for i in range(number_of_chars):
    letter_per_line = input()
    total_sum += ord(letter_per_line[0])
print(f'The sum equals: {total_sum}')
