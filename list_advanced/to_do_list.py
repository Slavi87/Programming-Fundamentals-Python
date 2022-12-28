command = input()
notes_lst = ['' for i in range(11)]
while command != 'End':
    lst = command.split('-')
    priority = int(lst[0])
    task = lst[1]
    notes_lst[priority] = task
    command = input()
final_lst = [i for i in notes_lst if i != '']

print(final_lst)
