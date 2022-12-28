number_of_rooms = int(input())
free_chairs = 0
difference = 0
room_number = 0
chairs_not_enough = False
for room in range(number_of_rooms):
    chairs, people = input().split()
    difference += len(chairs) - int(people)
    diff = 0
    if len(chairs) < int(people):
        room_number = room
        diff += abs(len(chairs) - int(people))
        chairs_not_enough = True
        print(f'{diff} more chairs needed in room {room_number + 1}')
if not chairs_not_enough:
    print(f"Game On, {difference} free chairs left")









#
# for i in range(len(chairs)):
#     if len(chairs[0]) > people[0]:
#         free_chairs += 1
#     elif len(chairs[0]) < people[0]:
#         used_chairs += 1
# print(free_chairs)





#
# for i in range(len(chairs)):
#     if len(chairs[0]) > people[0]:
#         free_chairs += 1
#     elif len(chairs[0]) < people[0]:
#         used_chairs += 1
# print(free_chairs)
