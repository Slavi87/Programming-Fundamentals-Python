single_string = input().split(',')
lst_numbers = []
zero_lst = []
other_numbers = []
final_lst = []
for element in single_string:
    lst_numbers.append(int(element))
for i in lst_numbers:
    if i == 0:
        zero_lst.append(i)
    else:
        other_numbers.append(i)
for j in other_numbers:
    final_lst.append(j)
for k in zero_lst:
    final_lst.append(k)
# final_lst.append(other_numbers + zero_lst)
print(final_lst)