number_of_electrons = int(input())
shell_lst = []
shell_list_fill = False

for num in range(1, number_of_electrons + 1):
    shell_lst.append(2 * num ** 2)
    diff = abs(sum(shell_lst) - shell_lst[-1] - number_of_electrons)
    if sum(shell_lst) == number_of_electrons:
        break
    if sum(shell_lst) > number_of_electrons:
        shell_lst.pop()
        shell_lst.append(diff)
        shell_list_fill = True
        break
print(shell_lst)
