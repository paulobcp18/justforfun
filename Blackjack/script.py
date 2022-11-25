import itertools, random
import numpy as np


# create decks
deck = list(itertools.product(range(1,14), 
        ['Spade', 'Hearts', 'Diamond', 'Club']))

# if player wants to choose the number of decks

# print('How many decks?')
# num_decks = input()
# deck = list(itertools.chain.from_iterable(itertools.repeat(x, int(num_decks)) for x in deck))

deck = list(itertools.chain.from_iterable(itertools.repeat(x, 8) for x in deck))

random.shuffle(deck)
# print(deck)

# place bets

print('How much do you wanna bet?')
bet_value = input()
bets = [int(bet_value)]
# print(bets)


# receive cards

players_cards = [random.choice(deck), random.choice(deck)]
dealers_cards = [random.choice(deck), random.choice(deck)]

print('Player\'s Hand: {} and {}'.format(players_cards[0], players_cards[1]))
print('Dealer\'s visible card: {}'.format(dealers_cards[0]))

# checking scores

def players_score():
    score = 0
    for i in range(len(players_cards)):
        if (players_cards[i][0] == 1 or players_cards[i][0] == 14):
            print('Ace equals to 1 or 11?')
            ace_choice = int(input())
            score += ace_choice
        elif (players_cards[i][0] < 10):
            score += players_cards[i][0]
        else:
            score += 10

    print('Player\'s score is: ', score)
    return score

    
players_score()
def you_win():
    player = players_score()
    if (player == 21):
        print('You win!')
        bets[0] = bets[0] * 2.5

you_win()



def dealers_score():
    score = 0
    for i in range(len(dealers_cards)):
        if (dealers_cards[i][0] == 1):
            print('Dealer, Ace equals to 1 or 11?')
            print(dealers_cards)
            ace_choice = int(input())
            score += ace_choice
        elif (dealers_cards[i][0] < 10):
            score += dealers_cards[i][0]
        else:
            score += 10

    print('Dealer\'s score is: ', score)
    return score


# dealers_score()

def hit_me():
    for i in range(10):
        
        print('Do you want another card?')
        hit_me = input()
        
        if hit_me == 'yes':
            players_cards.append(random.choice(deck))
            print(players_cards)
            total = players_score()
            if total > 21:
                print('bust')
                bets[0] = 0
                break
            elif total == 21:
                print('You win!')
                bets[0] = bets[0] * 2.5

        else:
            print('stay')
            dealer = dealers_score()
            total = players_score()
            if dealer >= 17:
                if total > dealer:
                    print('you win!')
                    bets[0] = bets[0] * 2
                else:
                    print('you lose!')
                    bets[0] = 0
                break
            else:
                dealers_cards.append(random.choice(deck))
                total_now = dealers_score()
                if total_now > 21:
                    print('dealer bust!')
                    bets[0] = bets[0] * 2
                else:
                    total = players_score()
                    if total_now > total:
                        ('dealer wins!')
                        bets[0] = 0
                    else:
                        ('you win!')
                        bets[0] = bets[0] * 2
                        break
                break

hit_me()

print(bets)



