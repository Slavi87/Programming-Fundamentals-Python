def total_price(product, quantity):
    if product == 'coffee':
        return quantity * 1.5
    elif product == 'water':
        return quantity * 1
    elif product == 'coke':
        return quantity * 1.4
    elif product == 'snacks':
        return quantity * 2


current_product = input()
current_quantity = int(input())
print(f'{total_price(current_product, current_quantity):.2f}')
