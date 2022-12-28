def even_numbers(num):
    if num % 2 == 0:
        return True


numbers = [int(el) for el in input().split()]
even_num = filter(even_numbers, numbers)
print(list(even_num))



# def even_numbers(number):
#     if number % 2 == 0:
#         return True
#
#
# numbers = list(map(int, input().split()))
# even_number = filter(even_numbers, numbers)
# print(list(even_number))
#

