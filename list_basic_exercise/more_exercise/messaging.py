sequence_of_numbers = [el for el in input().split()]
string = list(input())
length = len(string)
index = 0
message = ''
for el in sequence_of_numbers:
    for i in el:
        index += int(i)
    if index > len(string):
        diff = index - len(string)
        char = string[diff]
        message += char
        string.pop(diff)
        index = 0
    else:
        char = string[index]
        message += char
        string.pop(index)
        index = 0
print(message)
