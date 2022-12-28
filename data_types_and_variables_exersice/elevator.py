from math import ceil

number_people = int(input())
capacity = int(input())
number_of_courses = ceil(number_people / capacity)
print(number_of_courses)

