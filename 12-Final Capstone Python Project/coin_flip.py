'''
Coin Flip Simulation
simulates flipping a single coin however many times the user decides.
'''
import random
from collections import Counter as cnt

class Coin():

    def __init__(self):
        self.sides = {0:'Heads', 1:'Tails'}

    def flip_coin(self,n):
        outcomes = []
        
        for flip in range(n):
            flip = random.randint(0,1)
            outcomes.append(self.sides[flip])

        outcomes = cnt(outcomes)
        return print(f"Flipped the coin {n} times\nTails occured {outcomes['Tails']} times.\nHeads occured {outcomes['Heads']} times.")

while True:
    try:
        number_of_flips = int(input('How many times do you want to Flip the Coin? '))
    except ValueError:
        print('Please input an integer.')
    except:
        print('An unknown error occured. Please try again.')
    else:
        coin = Coin()
        coin.flip_coin(number_of_flips)
        try:
            flip_again = str(input('Would you like to flip the coin again? Y/N: ')).lower()
        except ValueError:
            print('Please enter a string value')
        except:
            print('An unknown error occured. Please try again.')
        else:
            if flip_again[0] == 'y':
                continue
            else:
                break



