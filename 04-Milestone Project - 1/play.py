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
    
    marker = 'null'
    while marker not in ('X', 'O'):
        marker = input('Player 1, do you wish to be Naughts (O) or Crosses (X)?')
    return

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
    return


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
    
    return len(board[1:]) == 9

# %%
# full_board_check(test_board)

# %%
def player_choice(board):
    
    print('Please choose a position as a number of 1 - 9')
    input_position = input('')

    if space_check(board,input_position) == True:
        return input_position        

# %%
# player_choice(test_board)

# %%
def replay():
    
    print('Do you wish to play again? Y/N')
    answer = input('')
    return answer in ('Yes', 'Y')

# %%
print('Welcome to Tic Tac Toe!')

# while True:
#     # Set the game up here
#     game_board = ['#','','','','','','','','','']

#     player_input

#     while game_on:
#         # Player 1 Turn
        
        
#         # Player2's turn.
            
#             pass

#     if not replay():
#         break

