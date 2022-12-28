
tickets_sequence = [el.strip() for el in input().split(', ')]
match_symbol = ''

for ticket in tickets_sequence:
    uninterrupted_match_length_first_half = 0
    uninterrupted_match_length_second_half = 0
    if len(ticket) != 20:
        print("invalid ticket")
    elif len(ticket) == 20:
        if '@' in ticket:
            match_symbol = '@'
        elif '#' in ticket:
            match_symbol = '#'
        elif '$' in ticket:
            match_symbol = '$'
        elif '^' in ticket:
            match_symbol = '^'
        else:
            print(f'ticket "{ticket}" - no match')
            continue
        middle = int(len(ticket) / 2)
        first_half = ticket[:middle]
        second_half = ticket[middle:]
        for i in range(len(first_half)):
            if first_half[i] == match_symbol:
                uninterrupted_match_length_first_half += 1
        for j in range(len(second_half)):
            if second_half[j] == match_symbol:
                uninterrupted_match_length_second_half += 1
        if 6 <= uninterrupted_match_length_first_half < 10 and 6 <= uninterrupted_match_length_second_half < 10:
            print(f'ticket "{ticket}" - {uninterrupted_match_length_first_half}{match_symbol}')
        elif uninterrupted_match_length_first_half == 10 and uninterrupted_match_length_second_half == 10:
            print(f'ticket "{ticket}" - {uninterrupted_match_length_first_half}{match_symbol} Jackpot!')

