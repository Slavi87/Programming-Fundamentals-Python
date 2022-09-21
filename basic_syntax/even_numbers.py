num = int(input())
for i in range(num):
    current_num = int(input())
    if current_num % 2 != 0:
        print(f'{current_num} is odd!')
        break
else:
    print(f'All numbers are even.')


