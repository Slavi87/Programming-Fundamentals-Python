import re
final = ''
pattern = r"[@, #]+([a-z]{3,})[@,#]+[!/@#$%^*&]+[/]+([\d]+)[/]+"
string = input()
matches = re.findall(pattern, string)
if matches:
    final = matches
for el in final:
    print(f"You found {el[1]} {el[0]} eggs!")


# word = ''
# for el in matches:
#     for i in el:
#         word += i
#     color = ''
#     number = ''
#     for j in word:
#         if j.isalpha():
#             color += j
#         elif j.isdigit():
#             number += j
#     print(f"You found {number} {color} eggs!")
#     color = ''
#     number = ''
#     word = ''


