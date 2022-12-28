numbers = input().split(', ')
numbers = list(map(int, numbers))
# lst = []
# for i, v in enumerate(numbers):
#     if v % 2 == 0:
#         lst.append(i)

print([index for index in range(len(numbers)) if numbers[index] % 2 == 0])
# for i in range(len(numbers)):
#     if numbers[i] % 2 == 0:
#         lst.append(i)
#


# print(lst)

