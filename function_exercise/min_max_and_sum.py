def min_number(nums):
    min_num = min(nums)
    print(f"The minimum number is {min_num}")
    # return f"The minimum number is {min_num}"


def max_num(nums):
    max_num = max(nums)
    print(f"The maximum number is {max_num}")
    # return f"The maximum number is {max_num}"


def sum_nums(nums):
    total_sum = sum(nums)
    print(f"The sum number is: {total_sum}")
    # return f"The sum number is: {total_sum}"


numbers = [int(el) for el in input().split()]
min_number(numbers)
max_num(numbers)
sum_nums(numbers)
# print(min_number(numbers))
# print(max_num(numbers))
# print(sum_nums(numbers))





# import sys
#
#
# def min_number(number):
#     min_num = sys.maxsize
#     for i in number:
#         if int(i) < min_num:
#             min_num = int(i)
#     return f"The minimum number is {min_num}"
#
#
# def max_number(number):
#     max_num = -sys.maxsize
#     for i in number:
#         if int(i) > max_num:
#             max_num = int(i)
#     return f"The maximum number is {max_num}"
#
#
# def sum_numbers(number):
#     sum_nums = 0
#     for i in number:
#         sum_nums += int(i)
#     return f"The sum number is: {sum_nums}"
#
#
# numbers = input().split()
# print(min_number(numbers))
# print(max_number(numbers))
# print(sum_numbers(numbers))
