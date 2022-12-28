quantity_of_decoration = int(input())
days_left = int(input())
budget = 0
christmas_spirit = 0
ornament_set = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15
for current_day in range(1, days_left + 1):
    if current_day % 11 == 0:
        quantity_of_decoration += 2
    if current_day % 2 == 0:
        budget += ornament_set * quantity_of_decoration
        christmas_spirit += 5
    if current_day % 3 == 0:
        budget += (tree_skirt + tree_garland) * quantity_of_decoration
        christmas_spirit += 13
    if current_day % 5 == 0:
        christmas_spirit += 17
        budget += tree_lights * quantity_of_decoration
        if current_day % 3 == 0:
            christmas_spirit += 30
    if current_day % 10 == 0:
        christmas_spirit -= 20
        budget += tree_skirt + tree_garland + tree_lights
if days_left % 10 == 0:
    christmas_spirit -= 30
print(f"Total cost: {budget}")
print(f"Total spirit: {christmas_spirit}")
