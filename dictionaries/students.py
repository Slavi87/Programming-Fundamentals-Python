data = input()
courses = {}
while ':' in data:
    student, id, course = data.split(':')
    if course not in courses:
        courses[course] = {}
    courses[course][id] = student
    data = input()
searched_course = data
searched_course_course_name = searched_course.split('_')
searched_course = ' '.join(searched_course_course_name)
for course_name in courses:
    if course_name == searched_course:
        for id, name in courses[course_name].items():
            print(f'{name} - {id}')


