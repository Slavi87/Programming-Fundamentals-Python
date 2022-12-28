first_line = input().split()
second_line = input().split()
third_line = input().split()
firs_player_won = False
second_player_won = False
total_lst = [first_line, second_line, third_line]
if (int(total_lst[0][0]) == int(total_lst[0][1]) == int(total_lst[0][2]) == 1) \
        or (int(total_lst[1][0]) == int(total_lst[1][1]) == int(total_lst[1][2]) == 1) \
        or (int(total_lst[2][0]) == int(total_lst[2][1]) == int(total_lst[2][2]) == 1) \
        or (int(total_lst[0][0]) == int(total_lst[1][0]) == int(total_lst[2][0]) == 1) \
        or (int(total_lst[0][1]) == int(total_lst[1][1]) == int(total_lst[2][1]) == 1) \
        or (int(total_lst[0][2]) == int(total_lst[1][2]) == int(total_lst[2][2]) == 1) \
        or (int(total_lst[0][1]) == int(total_lst[1][1]) == int(total_lst[2][2]) == 1) \
        or (int(total_lst[2][0]) == int(total_lst[1][1]) == int(total_lst[0][2]) == 1):
    firs_player_won = True
    # print("First player won")
elif (int(total_lst[0][0]) == int(total_lst[0][1]) == int(total_lst[0][2]) == 2) \
        or (int(total_lst[1][0]) == int(total_lst[1][1]) == int(total_lst[1][2]) == 2) \
        or (int(total_lst[2][0]) == int(total_lst[2][1]) == int(total_lst[2][2]) == 2) \
        or (int(total_lst[0][0]) == int(total_lst[1][0]) == int(total_lst[2][0]) == 2) \
        or (int(total_lst[0][1]) == int(total_lst[1][1]) == int(total_lst[2][1]) == 2) \
        or (int(total_lst[0][2]) == int(total_lst[1][2]) == int(total_lst[2][2]) == 2) \
        or (int(total_lst[0][1]) == int(total_lst[1][1]) == int(total_lst[2][2]) == 2) \
        or (int(total_lst[2][0]) == int(total_lst[1][1]) == int(total_lst[0][2]) == 2):
    second_player_won = True
    # print("Second player won")
if firs_player_won:
    print("First player won")
elif second_player_won:
    print("Second player won")
else:
    print("Draw!")



