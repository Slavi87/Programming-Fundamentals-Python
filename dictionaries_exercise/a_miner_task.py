sequence = input()
my_dict = {}
resource = []
while sequence != 'stop':
    resource.append(sequence)
    sequence = input()
for i in range(0, len(resource), 2):
    key = resource[i]
    value = resource[int(i + 1)]
    if key not in my_dict:
        my_dict[key] = int(value)
    else:
        my_dict[key] += int(value)
for key, value in my_dict.items():
    print(f"{key} -> {value}")


