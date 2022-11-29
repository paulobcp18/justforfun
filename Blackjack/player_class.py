import itertools, random

deck = list(itertools.product(range(1,14), 
        ['Spade', 'Hearts', 'Diamond', 'Club']))
deck = list(itertools.chain.from_iterable(itertools.repeat(x, 8) for x in deck))

class Player:
    def __init__(self, num, for_bet, score=0, bet=0):
        self.number = num
        self.initial_amount = for_bet
        self.score = 0
        self.hand = [random.choice(deck), random.choice(deck)]
        self.bet = 0

    def welcome(self):
        print('Welcome, Player', self.number)

    def print_hand(self):
        print(self.hand)

    def hand_update(self):
        self.hand.append(random.choice(deck))
        self.print_hand()

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

        print('Player\'s score is: ', self.score)
        return self.score

    def player_bet(self):
        init_bal = self.initial_amount
        print("you have {}, how much do you wanna bet?".format(init_bal))
        self.bet = int(input())
        if self.bet > init_bal:
            print('bet amount bigger than current balance')
            print('current balance: ', self.initial_amount)
            print("how much do you wanna bet?")
            self.bet = int(input())
        else:
            return self.bet
        

class Dealer:
    def __init__(self, for_bet=0, score=0, bet=0):
        self.initial_amount = 0
        self.score = 0
        self.hand = [random.choice(deck), random.choice(deck)]
        self.bet = 0

    def print_hand(self):
        print(self.hand[0])

    def hand_update(self):
        self.hand.append(random.choice(deck))
        self.print_hand()

    def ace_value_choice(self):
        print('Ace equals to 1 or 11?')
        ace_choice = int(input())
        return ace_choice

    def dealer_score(self):
        
        for i in range(len(self.hand)):
            if (self.hand[i][0] == 1 or self.hand[i][0] == 14):
                self.score += self.ace_value_choice()
            elif (self.hand[i][0] < 10):
                self.score += self.hand[i][0]
            else:
                self.score += 10

        print('Player\'s score is: ', self.score)
        return self.score

    def game_destiny(self):
        if self.dealer_score() < 17:
            self.hand_update()
            if self.dealer_score() > 21:
                print('Dealer Bust!')
            else:
                self.dealer_score()
        elif self.dealer_score > 16:
            self.print_hand()
            self.dealer_score()
        

    def balance(self):
        init_bal = self.initial_amount


Paulo = Player(1, 1000)
dealer = Dealer()


class Blackjack:
    def __init__(self):
        pass
    
    def game_start(self):
        print('Place your bets')        
        Paulo.player_bet()
        print('Cards will be drawn!')
        dealer.print_hand()
        Paulo.print_hand()
        Paulo.players_score()

    def hit_me(self):
        print('Do you want another card?')
        hit_me = input()

        if hit_me == 'yes':
            Paulo.hand_update()
            Paulo.print_hand()
            
            total = Paulo.players_score()
            if total > 21:
                print('bust')
                dealer.bet = Paulo.bet
                Paulo.player_bet[0] = 0
                
            elif total == 21:
                print('You win!')
                Paulo.player_bet[0] = Paulo.player_bet[0] * 2.5

        else:
            print('stay')
            dealer = dealer.dealers_score()
            total = Paulo.players_score()
            if dealer >= 17:
                if total > dealer:
                    print('you win!')
                    Paulo.player_bet[0] = Paulo.player_bet[0] * 2
                else:
                    print('you lose!')
                    dealer.bet = Paulo.player_bet[0]
                    Paulo.player_bet[0] = 0
                
            else:
                dealer.hand_update()
                total_now = dealer.dealers_score()
                if total_now > 21:
                    print('dealer bust!')
                    Paulo.player_bet[0] = Paulo.player_bet[0] * 2
                else:
                    total = Paulo.players_score()
                    if total_now > total:
                        ('dealer wins!')
                        dealer.bet = Paulo.player_bet[0]
                        Paulo.player_bet[0] = 0
                    else:
                        ('you win!')
                        Paulo.player_bet[0] = Paulo.player_bet[0] * 2
                        
                




# Paulo = Player(1, 1000)
# # Paulo.print_hand()
# # Paulo.players_score()

# dealer = Dealer()
# dealer.print_hand()

game_try = Blackjack()

game_try.game_start()
game_try.hit_me()


