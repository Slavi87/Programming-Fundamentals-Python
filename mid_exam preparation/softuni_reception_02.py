first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
number_of_students = int(input())
questions_per_hour = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency

hours = 0
while number_of_students > 0:
    hours += 1
    number_of_students -= questions_per_hour
    if hours % 4 == 0:
        hours += 1
print(f'Time needed: {hours}h.')