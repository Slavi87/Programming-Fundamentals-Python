command = input()
phonebook = []
name = []
phone_number = []
dict_phonebook = {}
while '-' in command:
    for el in command.split('-'):
        phonebook.append(el)
    command = input()
for i in range(0, len(phonebook), 2):
    name.append(phonebook[i])
    phone_number.append(phonebook[i + 1])
dict_phonebook = dict(zip(name, phone_number))
n = int(command)
for el in range(n):
    searched_name = input()
    if searched_name in dict_phonebook:
        print(f"{searched_name} -> {dict_phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")


# command = input()
# searched_names = []
# phone_book = {}
# while '-' in command:
#     current_command = command.split('-')
#     name = current_command[0]
#     phone_number = current_command[1]
#     if name not in phone_book:
#         phone_book[name] = phone_number
#     else:
#         phone_book[name] = phone_number
#     command = input()
# number = int(command)
# for el in range(number):
#     name = input()
#     searched_names.append(name)
# for el in searched_names:
#     if el in phone_book:
#         print(f'{el} -> {phone_book[el]}')
#     else:
#         print(f"Contact {el} does not exist.")
