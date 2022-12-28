data = input()
courses_dict = {}
members_counter = 0
while data != 'end':
    courses_info = data.split(' : ')
    course = courses_info[0]
    name = courses_info[1]
    if courses_info[0] not in courses_dict:
        courses_dict[course] = []
    courses_dict[course].append(name)
    data = input()
for key, value in courses_dict.items():
    print(f"{key}: {len(value)}")
    for v in range(len(value)):
        print(f"-- {value[v]}")


# command = input()
# courses = {}
# while command != 'end':
#     current_command = command.split(' : ')
#     course = current_command[0]
#     student_name = current_command[1]
#     if course not in courses:
#         courses[course] = [student_name]
#     else:
#         courses[course].append(student_name)
#     command = input()
# for key, value in courses.items():
#     print(f'{key}: {len(courses[key])}')
#     for v in range(len(value)):
#         print(f'-- {value[v]}')