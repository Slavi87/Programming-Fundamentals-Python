command = input()
price_without_taxes = 0
taxes = 0
price_with_taxes = 0
while command != 'special' and command != 'regular':
    current_command = float(command)
    if current_command <= 0:
        print('Invalid price')
        continue
    price_without_taxes += current_command
    command = input()
taxes = (price_without_taxes * 1.20) - price_without_taxes
price_with_taxes = price_without_taxes + taxes
if command == 'special':
    price_with_taxes *= 0.9

if price_with_taxes == 0:
    print('Invalid order!')
else:
    print(f'''Congratulations you've just bought a new computer!
Price without taxes: {price_without_taxes:.2f}$
Taxes: {taxes:.2f}$
-----------
Total price: {price_with_taxes:.2f}$''')





