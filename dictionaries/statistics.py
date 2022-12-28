data = input()
products = {}
while data != 'statistics':
    product, quantity = data.split(': ')
    if product not in products:
        products[product] = int(quantity)
    else:
        products[product] += int(quantity)
    data = input()
print("Products in stock:")
for key, value in products.items():
    print(f'- {key}: {value}')
print(f'Total Products: {len(products)}')
print(f'Total Quantity: {sum(products.values())}')