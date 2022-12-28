country = [key for key in input().split(', ')]
capitals = [value for value in input().split(', ')]
my_dict = dict(zip(country, capitals))
for key, value in my_dict.items():
    print(f"{key} -> {value}")

