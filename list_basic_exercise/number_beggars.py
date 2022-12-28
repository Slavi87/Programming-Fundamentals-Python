money = input().split(', ')
beggars = int(input())
money_list = []
index_counter = 0
final_list = []
for element in money:
    money_list.append(int(element))
while index_counter < beggars:
    sum_for_beggar = 0
    for current_index in range(index_counter, len(money_list), beggars):
        sum_for_beggar += money_list[current_index]
    final_list.append(sum_for_beggar)
    index_counter += 1
print(final_list)




