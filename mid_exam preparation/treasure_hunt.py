def treasure(elements):
    removed_elements = []
    while True:
        input_string = input()

        sum_items = 0
        counter = 0
        if input_string == "Yohoho!":
            break
        command = input_string.split()
        if command[0] == 'Loot':
            command.pop(0)
            for item in command:
                if item not in elements:
                    elements.insert(0, item)
        elif command[0] == 'Drop':
            if 0 <= int(command[1]) < len(elements):
                removed_el = elements.pop(int(command[1]))
                elements.append(removed_el)
        elif command == 'Steal':
            removed_elements = elements[- int(command[1])]
            print(removed_elements)
        for el in elements:
            sum_items += len(el)
            counter += 1


initial_treasure_chest = input().split('|')
print(treasure(initial_treasure_chest))

NOT