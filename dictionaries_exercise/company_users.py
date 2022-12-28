command = input()
my_dict = {}
while command != 'End':
    current_command = command.split(' -> ')
    company = current_command[0]
    user_name = current_command[1]
    if company not in my_dict:
        my_dict[company] = []
    if user_name not in my_dict[company]:
        my_dict[company].append(user_name)
    command = input()
for key, value in my_dict.items():
    print(f'{key}')
    for v in range(len(value)):
        print(f'-- {value[v]}')




# command = input()
# my_dict = {}
# while command != 'End':
#     data = command.split(' -> ')
#     course = data[0]
#     employee_id = data[1]
#     if course not in my_dict:
#         my_dict[course] = []
#     if employee_id not in my_dict[course]:
#         my_dict[course].append(employee_id)
#
#     command = input()
# for key, value in my_dict.items():
#     print(key)
#     for v in range(len(value)):
#         print(f'-- {value[v]}')

