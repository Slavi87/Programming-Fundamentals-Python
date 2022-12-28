elements = input().split()
bakery = {}
for i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i + 1]
    bakery[key] = int(value)
searched_element = input().split()
for el in searched_element:
    if el in bakery:
        print(f"We have {bakery[el]} of {el} left")
    else:
        print(f"Sorry, we don't have {el}")