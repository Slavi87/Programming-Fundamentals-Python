waiting_people = int(input())
current_state_of_lift = input().split()
no_people_left = False
for el in range(len(current_state_of_lift)):
    space = int(current_state_of_lift[el])
    while space < 4:
        space += 1
        waiting_people -= 1
        if waiting_people == 0:
            no_people_left = True
            break
    current_state_of_lift[el] = str(space)
    if no_people_left:
        break
if no_people_left and sum(list(map(int, current_state_of_lift))) == len(current_state_of_lift) * 4:
    print(f'{" ".join(current_state_of_lift)}')
elif no_people_left:
    print("The lift has empty spots!")
    print(* current_state_of_lift, sep=' ')
else:
    print(f"There isn't enough space! {waiting_people} people in a queue!")
    print(* current_state_of_lift, sep=' ')

