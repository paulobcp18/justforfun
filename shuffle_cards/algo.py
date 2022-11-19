import itertools, random

deck = list(itertools.product(range(1,14), 
        ['Spade', 'Hearts', 'Diamond', 'Club']))

print('How many cards?')

num_cards = int(input())

random.shuffle(deck)

print("You got:")
for i in range(num_cards):
    print(deck[i][0], "of", deck[i][1])