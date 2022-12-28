def inventory(items):
    while True:
        input_string = input()
        if input_string == 'Craft!':
            break
        command, item = input_string.split(' - ')
        if command == 'Collect':
            if item not in items:
                items.append(item)
        elif command == 'Drop':
            if item in items:
                items.remove(item)
        elif command == 'Combine Items':
            old_item, new_item = item.split(':')
            if old_item in items:
                old_item_index = items.index(old_item)
                items.insert(old_item_index + 1, new_item)
            else:
                continue
        elif command == 'Renew':
            items.remove(item)
            items.append(item)
    return items


string = input().split(', ')
print(', '.join(inventory(string)))
