import random

cards = {
    'k1': 6,    
    'k2': 7,
    'k3': 8,
    'k4': 9,  
    'k5': 10,
    'B': 10,
    'D': 10,    
    'K': 10,
    'T': 11,
}

suits = ['bubi', 'kresti', 'chervi', 'piki']

all_cards = []

for suit in suits:
    for card_name, card_value in cards.items():
        new_card = {
            'масть': suit,
            'название': card_name,
            'ценность': card_value
        }
        all_cards.append(new_card)

print('Всего карт в колоде:', len(all_cards))

random_card = random.choice(all_cards)

print('\nВыпала карта:')
print(f'Масть: {random_card['масть']}')
print(f'Название: {random_card['название']}')
print(f'Ценность: {random_card['ценность']}')