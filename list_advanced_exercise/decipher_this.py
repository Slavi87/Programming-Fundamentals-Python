secret_message = input().split()
num_lst, letter_lst = [], []
for word in secret_message:
    num = ''
    letter = ''
    for el in word:
        if el.isdigit():
            num += el
        else:
            letter += el
    num_lst.append(int(num))
    if len(letter) != 1:
        letter = f'{letter[-1]}{letter[1:-1]}{letter[0]}'
    letter_lst.append(letter)
for n, l in zip(num_lst, letter_lst):
    print(f'{chr(n)}{l}', end=' ')



