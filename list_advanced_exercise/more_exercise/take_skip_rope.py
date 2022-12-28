input_string = input()
number_lst = [int(el) for el in input_string if el.isdigit()]
letter_lst = [el for el in input_string if not el.isdigit()]
take_lst = [number_lst[el] for el in range(len(number_lst)) if el % 2 == 0]
skip_lst = [number_lst[el] for el in range(len(number_lst)) if el % 2 != 0]
taken_string = []
skipped_string = []

for t, s in zip(take_lst, skip_lst):
    taken_string.append(letter_lst[0:t])
    taken_value = t
    skipped_value = s
    for i in range(taken_value):
        letter_lst.pop(i)
    take_lst.pop(0)
    skipped_string.append(letter_lst[0:s])
    for j in range(skipped_value):
        letter_lst.pop(j)
    skip_lst.pop(0)



print(taken_string)
print(skipped_string)
print(take_lst)
print(skip_lst)
print(number_lst)
print(letter_lst)
