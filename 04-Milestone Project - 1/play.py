# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%
from IPython.display import clear_output

def display_board(board):
    print('#############')
    print('# ' + board[7] + ' # ' + board[8] + ' # ' + board[9] + ' #')
    print('# ' + board[4] + ' # ' + board[5] + ' # ' + board[6] + ' #')
    print('# ' + board[1] + ' # ' + board[2] + ' # ' + board[3] + ' #')
    print('#############')
    return

# %%
# test_board = ['#','X','O','X','O','X','O','X','O','X']
# display_board(test_board)

# %%
def player_input():
    
    marker = ''
    while marker not in ('X', 'O'):
        marker = input('Player 1, do you wish to be Naughts (O) or Crosses (X)? ')
    return marker

# %%
# player_input()

# %%
def place_marker(board, marker, position):
    
    board[position] = marker
    return

# %%
# place_marker(test_board,'O',8)
# display_board(test_board)

# %%
def win_check(board, mark):
    return (board[1] == mark and board[2] == mark and board[3] == mark) or (board[4] == mark and board[5] == mark and board[6] == mark) or (board[7] == mark and board[8] == mark and board[9] == mark) or (board[1] == mark and board[4] == mark and board[7] == mark) or (board[2] == mark and board[5] == mark and board[8] == mark) or (board[3] == mark and board[6] == mark and board[9] == mark) or (board[1] == mark and board[5] == mark and board[9] == mark) or (board[3] == mark and board[5] == mark and board[7] == mark)

# %%
# win_check(test_board,'X')

# %%
import random

def choose_first():
    n = random.randint(1,2)
    print(f'Player {n} goes first!')
    return n


# %%
# choose_first()

# %%
def space_check(board, position):
    ## Returns True if the space is available.
    return board[position] not in ('X', 'O')

# %%
# space_check(test_board,5)

# %%
def full_board_check(board):
    
    # the board is full, unless we can determine there's a free space.
    x = True
    for i in board[1:]:
        if i not in ('X', 'O'):
            x = False
    return x

# %%
# full_board_check(test_board)

# %%
def player_choice(board):
    while True:
        try:
            input_position = int(input('Please choose a position as a number between 1 and 9: '))
            if space_check(board,input_position) == True:
                break
        except ValueError:
            print('Input value was invalid.')
        
    return input_position
# %%
# player_choice(test_board)

# %%
def replay():
    
    answer = input('Do you wish to play again? Y/N: ')
    return answer == 'Y'

# %%
print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    game_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

    # Player 1 chooses their marker, assign the other marker to Player 2.
    player_input()
    player_1 = player_input()
    if player_1 == 'X':
        player_2 = 'O'
    else:
        player_2 = 'X'

    # Determine which player goes first
    turn = choose_first() 

    game_on = True

    while game_on:
        # Player 1 Turn
        while turn == 1:
            print('\n'*100)
            print("Player 1's turn.")
            display_board(game_board)

            marker_position = player_choice(game_board)

            place_marker(game_board, player_1, marker_position)

            
            if win_check(game_board, player_1):
                print('\n'*100)
                print('Player 1 wins!')
                display_board(game_board)
                game_on = False
                break
            
            turn = 2

        # Player2's turn.
        while turn == 2:
            print('\n'*100)
            print("Player 2's turn.")
            display_board(game_board)

            marker_position = player_choice(game_board)

            place_marker(game_board, player_2, marker_position)

            
            if win_check(game_board, player_2):
                print('\n'*100)
                print('Player 2 wins!')
                display_board(game_board)
                game_on = False
                break
            
            turn = 1

    if not replay():
        break

