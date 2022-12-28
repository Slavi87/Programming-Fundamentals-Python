number_of_snowballs = int(input())
max_weight = 0
max_time = 0
max_quality = 0
max_value = 0
for i in range(number_of_snowballs):
    weight = int(input())
    time_for_made_snowball = int(input())
    quality = int(input())
    value = int(weight / time_for_made_snowball) ** quality
    if value > max_value:
        max_weight = weight
        max_time = time_for_made_snowball
        max_quality = quality
        max_value = value
print(f'{max_weight} : {max_time} = {int(max_value)} ({max_quality})')
