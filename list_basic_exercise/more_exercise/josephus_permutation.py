input_lst = input().split(' ')
kill_counter = int(input())
lst_people = []
final_lst = []
counter = 0
index = 0
for i in input_lst:
    lst_people.append(int(i))
while len(lst_people) > 0:
    counter += 1
    if counter % kill_counter == 0:
        final_lst.append(lst_people.pop(index))
    else:
        index += 1
    if index >= len(lst_people):
        index = 0
print(str(final_lst).replace(', ', ','))