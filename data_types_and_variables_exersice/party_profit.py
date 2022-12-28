people_in_group = int(input())
days = int(input())
coins = 0
for current_day in range(1, days + 1):
    if current_day % 10 == 0:
        people_in_group -= 2
    if current_day % 15 == 0:
        people_in_group += 5
    if current_day % 3 == 0:
        coins -= 3 * people_in_group
    if current_day % 5 == 0:
        coins += 20 * people_in_group
        if current_day % 3 == 0:
            coins -= 2 * people_in_group
    coins += 50
    coins -= 2 * people_in_group
coins_for_person = int(coins // people_in_group)
print(f'{people_in_group} companions received {coins_for_person} coins each.')
