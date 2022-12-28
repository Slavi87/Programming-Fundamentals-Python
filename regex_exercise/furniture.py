import re

furniture_bought = []
total_money = 0
pattern = r">>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"
command = input()
while command != 'Purchase':
    match = re.search(pattern, command)
    if match:
        furniture, price, quantity = match.groups()
        furniture_bought.append(furniture)
        total_money += float(price) * int(quantity)
    command = input()
print("Bought furniture:")
for el in furniture_bought:
    print(el)
print(f"Total money spend: {total_money:.2f}")
