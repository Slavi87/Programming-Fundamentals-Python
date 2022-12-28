# employees_happiness = input().split()
employees_happiness = [int(el) for el in input().split()]
factor = int(input())
employees_happiness = ([i * factor for i in employees_happiness])
sum_happiness = sum(employees_happiness)
average = sum_happiness / len(employees_happiness)
counter = 0
for employee in employees_happiness:
    if employee >= average:
        counter += 1
if counter >= (len(employees_happiness) / 2):
    print(f'Score: {counter}/{len(employees_happiness)}. Employees are happy!')
else:
    print(f'Score: {counter}/{len(employees_happiness)}. Employees are not happy!')

