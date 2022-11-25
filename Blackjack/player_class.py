import itertools, random

deck = list(itertools.product(range(1,14), 
        ['Spade', 'Hearts', 'Diamond', 'Club']))
deck = list(itertools.chain.from_iterable(itertools.repeat(x, 8) for x in deck))

class Player:
    def __init__(self, num, for_bet, score, hand):
        self.number = num
        self.initial_amount = for_bet
        self.score = 0
        self.hand = [random.choice(deck), random.choice(deck)]

    def welcome(self):
        print('Welcome, Player', self.number)

    def hand_update(self):
        self.hand.append(random.choice(deck))

    def ace_value_choice(self):
        print('Ace equals to 1 or 11?')
        ace_choice = int(input())
        return ace_choice

    def players_score(self):
        
        for i in range(len(self.hand)):
            if (self.hand[i][0] == 1 or self.hand[i][0] == 14):
                self.score += self.ace_value_choice()
            elif (self.hand[i][0] < 10):
                self.score += self.hand[i][0]
            else:
                self.score += 10

        # print('Player\'s score is: ', score)
        return self.score
