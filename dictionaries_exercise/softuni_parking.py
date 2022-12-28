n = int(input())
my_dict = {}
for i in range(n):
    text = input().split()
    if text[0] == 'register':
        user_name = text[1]
        plate_number = text[2]
        if user_name not in my_dict:
            my_dict[user_name] = plate_number
            print(f"{user_name} registered {plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {my_dict[user_name]}")
    elif text[0] == 'unregister':
        user_name = text[1]
        if user_name not in my_dict:
            print(f"ERROR: user {user_name} not found")
        else:
            del my_dict[user_name]
            print(f"{user_name} unregistered successfully")
for key, value in my_dict.items():
    print(f"{key} => {value}")
