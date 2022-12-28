def small_number(numbers):
    return min(numbers)


first_num = int(input())
second_num = int(input())
third_num = int(input())
all_numbers = [first_num, second_num, third_num]
min_number = small_number(all_numbers)

print(min_number)