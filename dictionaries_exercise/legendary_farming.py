items = {"shards": 0, "fragments": 0, "motes": 0}
string = input().split()
is_obtained = False
while not is_obtained:
    for index in range(0, len(string), 2):
        value = int(string[index])
        key = string[index + 1].lower()
        if key not in items.keys():
            items[key] = 0
        items[key] += value
        if items["shards"] >= 250:
            print("Shadowmourne obtained!")
            items["shards"] -= 250
            is_obtained = True
        elif items["fragments"] >= 250:
            print("Valanyr obtained!")
            items["fragments"] -= 250
            is_obtained = True
        elif items["motes"] >= 250:
            print("Dragonwrath obtained!")
            items["motes"] -= 250
            is_obtained = True
        if is_obtained:
            break
    if is_obtained:
        break
    string = input().split()
for key, value in items.items():
    print(f"{key}: {value}")






