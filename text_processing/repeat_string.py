sequence = input().split()
final_string = ''
for el in sequence:
    final_string += el * len(el)
print(final_string)