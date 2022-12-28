command = input()
number_of_coffees = 0
while command != 'END':
    if command.lower() == "coding"\
        or command.lower() == 'dog'\
        or command.lower() == 'cat'\
        or command.lower() == 'movie':
        if command.islower():
            number_of_coffees += 1
        else:
            number_of_coffees += 2
    command = input()
if number_of_coffees > 5:
    print(f"You need extra sleep")
else:
    print(number_of_coffees)

