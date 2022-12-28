strings = input().split()
longest_string = ''
shortest_string = ''
total_sum = 0
if len(strings[0]) > len(strings[1]):
    longest_string = strings[0]
    shortest_string = strings[1]
    for i in range(len(shortest_string)):
        total_sum += ord(longest_string[i]) * ord(shortest_string[i])
    longest_string = longest_string[len(shortest_string):]
    for el in longest_string:
        total_sum += ord(el)
elif len(strings[0]) < len(strings[1]):
    longest_string = strings[1]
    shortest_string = strings[0]
    for i in range(len(shortest_string)):
        total_sum += ord(longest_string[i]) * ord(shortest_string[i])
    longest_string = longest_string[len(shortest_string):]
    for el in longest_string:
        total_sum += ord(el)
else:
    shortest_string = strings[0]
    longest_string = strings[1]
    for j in range(len(shortest_string)):
        total_sum += ord(shortest_string[j]) * ord(longest_string[j])
print(total_sum)





#
# strings = input().split()
# first_string = strings[0]
# second_string = strings[1]
# longer_str = ''
# shortest_str = ''
# total_sum = 0
# if len(first_string) > len(second_string):
#     longer_str = first_string
#     shortest_str = second_string
#     for i in range(len(shortest_str)):
#         total_sum += ord(first_string[i]) * ord(second_string[i])
#     longer_str = longer_str[len(shortest_str):]
#
#     for j in range(len(longer_str)):
#         total_sum += ord(longer_str[j])
# elif len(first_string) < len(second_string):
#     longer_str = second_string
#     shortest_str = first_string
#     for p in range(len(shortest_str)):
#         total_sum += ord(first_string[p]) * ord(second_string[p])
#     longer_str = longer_str[len(shortest_str):]
#
#     for s in range(len(longer_str)):
#         total_sum += ord(longer_str[s])
# else:
#     longer_str = first_string
#     for i in range(len(longer_str)):
#         total_sum += ord(first_string[i]) * ord(second_string[i])
#         i += 1
# print(total_sum)
#
