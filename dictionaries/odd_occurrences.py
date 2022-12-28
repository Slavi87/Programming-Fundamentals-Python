sequence = input().split()
my_dict = {}
for el in sequence:
    el_lower = el.lower()
    if el_lower not in my_dict:
        my_dict[el_lower] = 0
    my_dict[el_lower] += 1
for key, value in my_dict.items():
    if value % 2 != 0:
        print(key, end=' ')