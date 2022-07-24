cards = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10
}

first_card = input('Enter your first card (enter face cards as A, J, Q, and K): ').title()
second_card = input('Enter your second card (enter face cards as A, J, Q, and K): ').title()
third_card = input('Enter your third card (enter face cards as A, J, Q, and K): ').title()

first_val = cards[first_card]
second_val = cards[second_card]
third_val = cards[third_card]

card_total = first_val + second_val + third_val

#aces can be worth 11; two aces can't both be treated as 11 because that will automatically bust
if first_card == 'A' or second_card == 'A' or third_card == 'A':
    if card_total + 10 <= 21:
        card_total += 10

# Less than 17, advise to "Hit"
if card_total < 17:
    print(f'{card_total} hit')
# Greater than or equal to 17, but less than 21, advise to "Stay"
elif card_total >= 17 and card_total < 21:
    print(f'{card_total} stay')
# Exactly 21, advise "Blackjack!"
elif card_total == 21:
    print(f'{card_total} Blackjack!')
# Over 21, advise "Already Busted"
else:
    print(f'{card_total} already busted')