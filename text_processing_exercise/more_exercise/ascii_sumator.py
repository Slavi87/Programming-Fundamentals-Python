first_char = input()
second_char = input()
text = input()
total_sum = 0
num_first_char = ord(first_char)
num_second_char = ord(second_char)
for el in text:
    if num_first_char < ord(el) < num_second_char:
        total_sum += ord(el)
print(total_sum)