quantity_of_food = float(input()) * 1000
quantity_hay = float(input()) * 1000
quantity_cover = float(input()) * 1000
pig_weight = float(input()) * 1000
days = 30
for i in range(1, days + 1):
    quantity_of_food -= 300
    if i % 2 == 0:
        quantity_hay -= (quantity_of_food * 0.05)
    if i % 3 == 0:
        quantity_cover -= (pig_weight * 1/3)
if quantity_of_food >= 0 and quantity_hay >= 0 and quantity_cover >= 0:
    print(f'Everything is fine! Puppy is happy! Food: {quantity_of_food/1000:.2f}, Hay: {quantity_hay/1000:.2f}, Cover: {quantity_cover/1000:.2f}.')
else:
    print("Merry must go to the pet store!")