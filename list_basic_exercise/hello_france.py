collection_of_item = input().split('|')
budget = float(input())
total_spend = 0
profit_clothes = 0
profit_shoes = 0
profit_accessories = 0
train_ticket = 150
for item in collection_of_item:
    item_lst = item.split('->')
    name = item_lst[0]
    price = float(item_lst[1])
    if item == 'Clothes':
        if price <= 50:
            budget -= price
            total_spend += price
            profit_clothes += price * 1.4
    if item == 'Shoes':
        if price <= 35:
            budget -= price
            total_spend += price
            profit_shoes += price * 1.4
    if item == 'Accessories':
        if price <= 20.50:
            budget -= price
            total_spend += price
            profit_accessories += price * 1.
total_profit = abs((profit_clothes + profit_shoes + profit_accessories) - total_spend)



print(total_profit)




# if total_budget >= train_ticket:
#     print("Hello, France!")
# else:
#     print('Not enough money.')
