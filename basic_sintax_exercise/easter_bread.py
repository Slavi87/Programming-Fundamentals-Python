budget = float(input())
price_flour = float(input())
price_for_pack_eggs = price_flour * 0.75
price_milk = price_flour * 1.25 / 4
value_of_one_loaf = price_milk + price_flour + price_for_pack_eggs
colored_eggs = 0
current_bread_count = 0
while budget >= value_of_one_loaf:
    budget -= value_of_one_loaf
    current_bread_count += 1
    colored_eggs += 3
    if current_bread_count % 3 == 0:
        colored_eggs -= current_bread_count - 2

print(f"You made {current_bread_count} loaves of Easter bread!\
 Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
