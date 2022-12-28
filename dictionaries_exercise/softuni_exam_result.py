command = input()
my_dict = {}
while command != 'exam finished':
    data = command.split('-')
    username = data[0]
    language = data[1]
    points = data[2]
    if language not in my_dict:
        my_dict[language] = [username]


    command = input()



