char_index_one = int(input())
char_index_two = int(input())
index = ''
for i in range(char_index_one, char_index_two + 1):
    index = chr(i)
    print(index, end=' ')

