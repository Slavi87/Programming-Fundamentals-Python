string = input()
for el in range(len(string)):
    if string[el] == ':':
        print(f':{string[el + 1]}')


#
# text = input()
# for char in range(len(text)):
#     symbol = ''
#     if text[char] == ':':
#         symbol = text[char + 1]
#         print(f':{symbol}')