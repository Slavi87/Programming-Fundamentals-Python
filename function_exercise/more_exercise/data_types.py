def data_type(data, num):
    result = ''
    if data == 'int':
        result = int(num) * 2
    elif data == 'real':
        result = f'{float(num) * 1.5:.2f}'
    elif data == 'string':
        result = f'${num}$'
    return result


data_input = input()
number = input()
print(data_type(data_input, number))

# def types(first, second):
#     text = ''
#     if first == 'int':
#         text += str(int(second) * 2)
#     elif first == 'real':
#         text += f'{float(second) * 1.5:.2f}'
#     elif first == 'string':
#         text = '$' + second + '$'
#     return text
#
#
# first_row = input()
# second_row = input()
# print(types(first_row, second_row))
