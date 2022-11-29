import itertools, random

deck = list(itertools.product(range(1,14), 
        ['Spade', 'Hearts', 'Diamond', 'Club']))
deck = list(itertools.chain.from_iterable(itertools.repeat(x, 8) for x in deck))


class Blackjack:
    def __init__(self, for_bet):
        self.player_initial_amount = for_bet
        self.player_score = 0
        self.dealer_score = 0
        self.player_hand = [random.choice(deck), random.choice(deck)]
        self.dealer_hand = [random.choice(deck), random.choice(deck)]

    def print_hand(self):
        print(self.player_hand)
        print(self.dealer_hand[0])

    def hand_update(self, who):
        if who == 'player':
            self.player_hand.append(random.choice(deck))
            self.print_hand()
        else:
            self.dealer_hand.append(random.choice(deck))
            self.print_hand()

    def ace_value_choice(self):
        print('Ace equals to 1 or 11?')
        ace_choice = int(input())
        return ace_choice

    # create round variable, so that I wont have to create another module for update the score
    def score(self, who):
        if who == 'player':
            for i in range(len(self.player_hand)):
                if (self.player_hand[i][0] == 1 or self.player_hand[i][0] == 14):
                    self.player_score += self.ace_value_choice()
                elif (self.player_hand[i][0] < 10):
                    self.player_score += self.player_hand[i][0]
                else:
                    self.player_score += 10
            print('Player\'s score is: ', self.player_score)
            return self.player_score
        
        else:
            for i in range(len(self.dealer_hand)):
                if (self.dealer_hand[i][0] == 1 or self.dealer_hand[i][0] == 14):
                    self.dealer_score += self.ace_value_choice()
                elif (self.dealer_hand[i][0] < 10):
                    self.dealer_score += self.dealer_hand[i][0]
                else:
                    self.dealer_score += 10
            print('Dealer\'s score is: ', self.dealer_score)
            return self.dealer_score

    def update_score(self, who):
        if who == 'player':
            
            if (self.player_hand[-1][0] == 1 or self.player_hand[-1][0] == 14):
                self.player_score += self.ace_value_choice()
            elif (self.player_hand[-1][0] < 10):
                self.player_score += self.player_hand[-1][0]
            else:
                self.player_score += 10
            print('Player\'s score is: ', self.player_score)
            return self.player_score
        
        else:
            
            if (self.dealer_hand[-1][0] == 1 or self.dealer_hand[-1][0] == 14):
                self.dealer_score += self.ace_value_choice()
            elif (self.dealer_hand[-1][0] < 10):
                self.dealer_score += self.dealer_hand[-1][0]
            else:
                self.dealer_score += 10
        print('Dealer\'s score is: ', self.dealer_score)
        return self.dealer_score


    def player_bet(self):
        init_bal = self.player_initial_amount
        print("you have {}, how much do you wanna bet?".format(init_bal))
        self.bet = int(input())
        while self.bet > init_bal:
            print('bet amount bigger than current balance')
            print('current balance: ', self.player_initial_amount)
            print("how much do you wanna bet?")
            self.bet = int(input())
        return self.bet
            
    #parei aqui
    def game_destiny(self):
        if self.dealer_score < 17:
            self.hand_update('dealer')
            if self.dealer_score > 21:
                print('Dealer Bust!')
            else:
                print(self.dealer_score)
        elif self.dealer_score > 16:
            self.print_hand()
            self.dealer_score()
        

    def balance(self):
        init_bal = self.initial_amount


    def game_start(self):
        print('Place your bets')        
        self.Player.player_bet()
        print('Cards will be drawn!')
        self.Dealer.print_hand()
        self.Player.print_hand()
        self.Player.players_score()

    def hit_me(self):
        print('Do you want another card?')
        hit_me = input()

        if hit_me == 'yes':
            self.Player.hand_update()
            self.Player.print_hand()
            
            total = Paulo.players_score()
            if total > 21:
                print('bust')
                self.Dealer.bet = self.Player.bet
                self.Player.player_bet[0] = 0
                
            elif total == 21:
                print('You win!')
                self.Player.player_bet[0] = self.Player.player_bet[0] * 2.5

        else:
            print('stay')
            dealer = self.Dealer.dealers_score()
            total = self.Player.players_score()
            if dealer >= 17:
                if total > self.Dealer:
                    print('you win!')
                    self.Player.player_bet[0] = self.Player.player_bet[0] * 2
                else:
                    print('you lose!')
                    self.Dealer.bet = self.Player.player_bet[0]
                    self.Player.player_bet[0] = 0
                
            else:
                dealer.hand_update()
                total_now = self.Dealer.dealers_score()
                if total_now > 21:
                    print('dealer bust!')
                    self.Player.player_bet[0] = self.Player.player_bet[0] * 2
                else:
                    total = self.Player.players_score()
                    if total_now > total:
                        ('dealer wins!')
                        self.Dealer.bet = self.Player.player_bet[0]
                        self.Player.player_bet[0] = 0
                    else:
                        ('you win!')
                        self.Player.player_bet[0] = self.Player.player_bet[0] * 2

    def flow(self):
        self.game_start()
        self.hit_me()
                    
                




# Paulo = Player(1, 1000)
# # Paulo.print_hand()
# # Paulo.players_score()

# dealer = Dealer()
# dealer.print_hand()

game_try = Blackjack(1000)

# game_try.print_hand()

# game_try.score('player')
# game_try.score('dealer')

# game_try.hand_update('player')
# game_try.hand_update('dealer')

# game_try.update_score('player')
# game_try.update_score('dealer')

game_try.player_bet()