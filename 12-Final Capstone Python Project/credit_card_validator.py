'''
Numbers Capstone Project: Credit Card Validator
Takes in a credit card number from a common credit card vendor
and validates it to make sure that it is a valid number

This is acomplished by using the Luhn Algorithm: https://en.wikipedia.org/wiki/Luhn_algorithm
    Step 1 – Starting from the rightmost digit, double the value of every second digit
    Step 2 – If doubling of a number results in a value greater than 9 then add the digits of the product
    Step 3 – Now take the sum of all the digits (including non-doubled)
    Step 4 – If the total modulo 10 is equal to 0 then the number is valid else it is not valid

Example:
    Starting with 79927398713
    We get 79947697723
    Sum is 70
    modulo 10 of 70 equals 0
    79927398713 is valid.

Addition - detection of care type:
    The first digit in your credit-card number signifies the system: 
        3 - travel/entertainment cards (such as American Express and Diners Club)
            37 = American Express
            38 = Diners Club
        4 - Visa
        5 - MasterCard
        6 - Discover Card
'''


class LuhnCheck:

    def __init__(self,credit_card_number):
        # Transform the input credit_card_number string into a list of integers
        self.credit_card_number = []
        for number in credit_card_number:
            self.credit_card_number.append(int(number))
        
        # Create a dictionary for the doubling of specific key values
        self.double_dictionary = {}

    def __str__(self):
        # Used for debugging
        return f'{self.credit_card_number}'

    def double_every_second_digit(self):
        # Starting from the rightmost digit, double the value of every second digit
        index_count = 0
        # double_dictionary = {}

        for number in reversed(self.credit_card_number): # reversed so we begin at the rightmost digit
            if index_count % 2 == 0: # python is zero based which is considered even!
                self.double_dictionary[index_count] = number
            else: # these must be odd (our second digits)
                self.double_dictionary[index_count] = number * 2

                # If doubling of a number results in a value greater than 9 then add the digits of the product
                if self.double_dictionary[index_count] > 9:
                    a,b = str(self.double_dictionary[index_count])
                    self.double_dictionary[index_count] = int(a) + int(b)

            index_count += 1

        return f'{self.double_dictionary}' # debug

    def sum_of_all_digits(self):
        # Now take the sum of all the digits (including non-doubled)
        return sum(self.double_dictionary.values())

    def validate(self):
        # Returns True if the credit_card_number passes the LuhnCheck
        return self.sum_of_all_digits() % 10 == 0

    def card_type(self):
        # Returns the Card Type, if it can be determined
        card_types = {3:{7:'American Express', 8:'Diners Club'}, 4:'Visa', 5:'MasterCard', 6:'Discover Card'}

        if self.credit_card_number[0] == 3 and self.credit_card_number[1] in (7, 8):
            card_type = card_types[self.credit_card_number[0]][self.credit_card_number[1]]
            return f'This appears to be a {card_type}.'
        elif self.credit_card_number[0] in (4, 5, 6):
            card_type = card_types[self.credit_card_number[0]]
            return f'This appears to be a {card_type}.'
        else:
            return f'Unable to determine the card type.'
        
# User inputs a Credit Card Number
while True:
    try:
        input_credit_card = input('Please provide a Credit Card Number: ')
        int(input_credit_card) # Validate that the input string is all numeric
    except ValueError:
        print(f'{input_credit_card} is an invalid input. Please double-check and try again.')
    except:
        print(f'An unknown error occured.')
    else:
        check = LuhnCheck(input_credit_card)
        # Inform the User if the input Credit Card Number is valid or not
        if check.validate():
            print(f'{input_credit_card} is a possibly valid Credit Card Number.')
            print(check.card_type())
            break
        else:
            print(f'{input_credit_card} is not a valid Credit Card Number.')
            break




 






