input_lst = input().split(' ')
lst = []
for i in input_lst:
    current_value = float(i)
    lst.append(abs(current_value))
print(lst)

