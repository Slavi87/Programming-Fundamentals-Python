number = int(input())
my_dict = {}
for i in range(number):
    word = input()
    synonym = input()
    if word not in my_dict:
        my_dict[word] = [synonym]
    else:
        my_dict[word].append(synonym)
for key, value in my_dict.items():
    print(f'{key} - {", ".join(value)}')