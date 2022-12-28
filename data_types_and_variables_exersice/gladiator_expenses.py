lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet = 0
sword = 0
shield = 0
armor = 0
shield_count = 0
for current_fight in range(1, lost_fights_count + 1):
    if current_fight % 2 == 0:
        helmet += helmet_price
    if current_fight % 3 == 0:
        sword += sword_price
    if current_fight % 2 == 0 and current_fight % 3 == 0:
        shield += shield_price
        shield_count += 1
        if shield_count % 2 == 0:
            armor += armor_price
total_expenses = helmet + sword + shield + armor
print(f'Gladiator expenses: {total_expenses:.2f} aureus')
