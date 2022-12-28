number_letters = int(input())
for i in range(0, number_letters):
    for j in range(0, number_letters):
        for x in range(0, number_letters):
            print(f'{chr(97 + i)}{chr(97 + j)}{chr(97 + x)}')

            