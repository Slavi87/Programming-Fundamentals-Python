deck_of_cards = input().split()
number_of_shuffles = int(input())
for shuffle in range(number_of_shuffles):
    final_deck_lst = []
    middle_deck = len(deck_of_cards) // 2
    left_part = deck_of_cards[0: middle_deck]
    right_part = deck_of_cards[middle_deck::]
    for index in range(len(left_part)):
        final_deck_lst.append(left_part[index])
        final_deck_lst.append(right_part[index])
    deck_of_cards = final_deck_lst
print(deck_of_cards)