command = input()
orders_dict = {}
while command != 'buy':
    orders = command.split()
    for i in range(0, len(orders), 3):
        name = orders[i]
        price = float(orders[i + 1])
        quantity = float(orders[i + 2])
        if name not in orders_dict:
            orders_dict[name] = [float(price), float(quantity)]
        else:
            orders_dict[name][0] = float(price)
            orders_dict[name][1] += float(quantity)
    command = input()
for key, value in orders_dict.items():
    print(f"{key} -> {value[0] * value[1]:.2f}")


# command = input()
# orders = {}
# while command != 'buy':
#     current_command = command.split()
#     product = current_command[0]
#     price = float(current_command[1])
#     quantity = float(current_command[2])
#     if product not in orders:
#         orders[product] = []
#         orders[product].append(price)
#         orders[product].append(quantity)
#     else:
#         orders[product][0] = price
#         orders[product][1] += quantity
#     command = input()
# for key, value in orders.items():
#     print(f'{key} -> {value[0] * value[1]:.2f}')