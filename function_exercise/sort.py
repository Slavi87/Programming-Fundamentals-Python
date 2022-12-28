def sorted_numbers(nums):
    sorted_nums = sorted(nums)
    return sorted_nums


numbers = [int(el) for el in input().split()]
print(sorted_numbers(numbers))



# def sorted_numbers(numbers):
#     sorted_numbers_lst = []
#     for i in numbers:
#         sorted_numbers_lst.append(int(i))
#     sorted_numbers_lst.sort()
#     return sorted_numbers_lst
#
#
# nums = input().split()
# print(sorted_numbers(nums))
