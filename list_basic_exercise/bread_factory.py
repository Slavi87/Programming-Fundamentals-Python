day_event = input().split('|')
initial_energy = 100
initial_coins = 100
bread_factory_open = True
for event in day_event:
    event_items = event.split('-')
    type_of_event = event_items[0]
    event_value = int(event_items[1])
    if type_of_event == 'rest':
        current_energy = initial_energy
        initial_energy += event_value
        if initial_energy > 100:
            initial_energy = 100
        gained_energy = initial_energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {initial_energy}.")
    elif type_of_event == 'order':
        if initial_energy >= 30:
            initial_coins += event_value
            initial_energy -= 30
            print(f"You earned {event_value} coins.")
        else:
            initial_energy += 50
            print("You had to rest!")
    else:
        if initial_coins >= event_value:
            initial_coins -= event_value
            print(f"You bought {type_of_event}.")
        else:
            print(f"Closed! Cannot afford {type_of_event}.")
            bread_factory_open = False
            break
if bread_factory_open:
    print("Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")
