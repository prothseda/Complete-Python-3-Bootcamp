import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.deck.append(f'{card}')

    def __str__(self):
        return f'{self.deck}'

    def suffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return f'{self.deck.pop(0)}'

class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def __str__(self):
        return f'{self.cards}\nValue: {self.value}'

    def add_card(self, card):
        self.cards.append(card)

        card_string_split = card.split()
        self.value += values[card_string_split[0]]

        if card_string_split[0] == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        if self.value > 21 & self.aces > 0:
            self.value -= (10 * self.aces)


class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def __str__(self):
        return f'You have {self.total} in Chips.'

    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

def place_bet(chips):

    while True:
        try:
            bet = int(input('Place your bet: '))
            if chips.total - bet < 0:
                f'Insufficent chips available.\nBet: {bet}\nAvailable chips: {chips.total}'
                continue
            else:
                chips.bet = bet
                f'You bet {bet}.'
                break
        except TypeError:
            f'{bet} is not a valid bet.'
        except:
            f'An unknown error occured. Please try again.'

def hit(deck,hand):
    card_to_add = deck.deal()
    hand.add_card(card_to_add)
    hand.adjust_for_ace
    print(f'{card_to_add}')

def hit_or_stand(deck,hand):
    global playing

    while True:
        try:
            action = input('Would you like to Hit or Stand? ').capitalize()
            print(f'{action}')
        except:
            f'An error occured. Please try again.'
        else:
            if action in ('Hit', 'Stand'):
                break
            else:
                f'Invalid input. Please try again.'
                
    if action == 'Hit':
        hit(deck,hand)
    else:
        playing = False
    
def show_some_cards(player,dealer):

    print(f"Dealer's hand: <first card is hidden> {dealer.cards[1:]}")
    print(f"Player's hand: {player.cards}\nPlayer's Value: {player.value}")

def show_all_cards(player,dealer):

    print(f"Dealer's hand: {dealer.cards}\nDealer's Value: {dealer.value}")
    print(f"Player's hand: {player.cards}\nPlayer's Value: {player.value}")

def player_busts(chips):
    chips.lose_bet()    
    print(f'Player is bust! Lost {chips.bet}')

def player_wins(chips):
    chips.win_bet()
    print(f'Player wins! Won {chips.bet}')
    
def dealer_busts(chips):
    chips.win_bet()
    print(f'Dealer bust! Player wins {chips.bet}')

def dealer_wins(chips):
    chips.lose_bet()
    print(f'Dealer Wins! Player lost {chips.bet}')

def push():
    print(f'Push! No winning bet.')


while True:
    playing = True
    # Print an opening statement
    print(f'Welcome to Blackjack!')
    input('Please any key to begin.')
    
    # Create & shuffle the deck, deal two cards to each player
    playing_deck = Deck()
    playing_deck.suffle()

    player_hand = Hand()
    dealer_hand = Hand()

    player_hand.add_card(playing_deck.deal())
    dealer_hand.add_card(playing_deck.deal())
    player_hand.add_card(playing_deck.deal())
    dealer_hand.add_card(playing_deck.deal())
        
    # Set up the Player's chips
    player_chips = Chips()
    print(player_chips)
    
    # Prompt the Player for their bet
    place_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some_cards(player_hand,dealer_hand)
    
    while playing:
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(playing_deck,player_hand)
        
        # Show cards (but keep one dealer card hidden)
        show_some_cards(player_hand,dealer_hand)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    while True:
        if dealer_hand.value < 17:
            hit(playing_deck,dealer_hand)

        # Show all cards
        show_all_cards(player_hand,dealer_hand)

        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_chips)
        elif dealer_hand.value >= 17:
            if dealer_hand.value > player_hand.value:
                dealer_wins(player_chips)
                break
            elif dealer_hand.value < player_hand.value:
                player_wins(player_chips)
                break
            else:
                push()
                break
    
    # Inform Player of their chips total 
    print(player_chips)

    # Ask to play again
    while True:
        try:
            play_again = input("Do you wish to play again? Y/N: ").capitalize()
        except:
            f'Invalid input. Please try again.'
        else:
            if play_again in ('Y', 'N'):
                break
            else:
                continue
    if play_again == 'N':
        break









