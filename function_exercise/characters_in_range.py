def characters(firs, second):
    characters_lst = []
    for i in range(ord(first_chr) + 1, ord(second_char)):
        characters_lst.append(chr(i))
    return characters_lst


first_chr = input()
second_char = input()
final_result = characters(first_chr, second_char)
print(*final_result)
# print(*characters(first_chr,second_char))


# def characters(first, second):
#     lst = []
#     first_ch = ord(first)
#     second_ch = ord(second)
#     for el in range(first_ch + 1, second_ch):
#         lst.append(chr(el))
#     return lst
#
#
# first_char = input()
# second_char = input()
# print(' '.join(characters(first_char, second_char)))