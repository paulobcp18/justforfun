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

        

class Blackjack:
    def __init__(self) -> None:
        pass

    def game_start():
        print('Place your bets')        
        Player.player_bet()
        print('Cards will be drawn!')
        Dealer.print_hand()
        Player.print_hand()
        Player.players_score()

    def hit_me():
        print('Do you want another card?')
        hit_me = input()

        if hit_me == 'yes':
            Player.hand_update()
            Player.print_hand()
            
            total = Player.players_score()
            if total > 21:
                print('bust')
                Dealer.bet = Player.player_bet[0]
                Player.player_bet[0] = 0
                
            elif total == 21:
                print('You win!')
                Player.player_bet[0] = Player.player_bet[0] * 2.5

        else:
            print('stay')
            dealer = Dealer.dealers_score()
            total = Player.players_score()
            if dealer >= 17:
                if total > dealer:
                    print('you win!')
                    Player.player_bet[0] = Player.player_bet[0] * 2
                else:
                    print('you lose!')
                    Dealer.bet = Player.player_bet[0]
                    Player.player_bet[0] = 0
                
            else:
                Dealer.hand_update()
                total_now = Dealer.dealers_score()
                if total_now > 21:
                    print('dealer bust!')
                    Player.player_bet[0] = Player.player_bet[0] * 2
                else:
                    total = Player.players_score()
                    if total_now > total:
                        ('dealer wins!')
                        Dealer.bet = Player.player_bet[0]
                        Player.player_bet[0] = 0
                    else:
                        ('you win!')
                        Player.player_bet[0] = Player.player_bet[0] * 2
                        
                




Paulo = Player(1, 1000)
# Paulo.print_hand()
# Paulo.players_score()

dealer = Dealer()
# dealer.print_hand()

Blackjack.game_start()
Blackjack.hit_me()


