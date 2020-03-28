# Tic Tac Toe game ############################################################################

import time

# Overall Scores
player_X_Score = 0
player_O_Score = 0
# Initialize lists to represent the moves of each player
player_X_moves = [False]*9
player_O_moves = [False]*9
# Create a string to manage which of the players (X or O) is to play. Start with X.
current_player = 'X'
# Game status
status = 'In-Progress'
# Template board for explanation
template_board = "7|8|9\n" \
            "4|5|6\n" \
            "1|2|3\n"

# Exception Class to handle the end of the game
class GameDone(Exception): pass

def reset_the_game():
    global player_X_moves,player_O_moves,current_player,status
    player_X_moves = [False] * 9
    player_O_moves = [False] * 9
    current_player = 'X'
    status = 'In-Progress'

def get_player_move():
    '''Function that gets player input and update his/her moves accordingly'''
    # Loop as long as required to get a valid user input
    while True:
        player_input_str = input(f"Player {current_player}:")
        # If the player enters q then raise an exception to quit the game
        if player_input_str == 'q':
            raise GameDone
        else:
            try:
                player_input = int(player_input_str)
                if player_input in range(1,10):
                    print(f"valid input: {player_input}")
                    if (current_player == 'X') and (player_O_moves[player_input-1] == False):
                        player_X_moves[player_input-1] = True
                        break
                    elif (current_player == 'O') and (player_X_moves[player_input-1] == False):
                        player_O_moves[player_input-1] = True
                        break
                    else:
                        print(f'there is already a mark in position: {player_input}')
                else:
                    print(f"invalid input: {player_input_str}")
            except:
                print(f"invalid input: {player_input_str}")

def which_symbol(move_X,move_O):
    '''Functiun that returns the symbol to be displayed in a given board location'''
    if move_X:
        return 'X'
    elif move_O:
        return 'O'
    else:
        return ' '

def display_board():
    '''Function that displays the Tic Tac Toe Board based on users moves'''
    # Create a list that will hold X or O in each position of the board
    board_data = [which_symbol(tup[0], tup[1]) for tup in zip(player_X_moves, player_O_moves)]
    # Create the board based on its data
    board = f"{board_data[6]}|{board_data[7]}|{board_data[8]}\n" \
            f"{board_data[3]}|{board_data[4]}|{board_data[5]}\n" \
            f"{board_data[0]}|{board_data[1]}|{board_data[2]}\n"
    # Print out the board
    print(board)

def alternate_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'
    return current_player

def get_game_status():
    '''Function that returns Won, Null or In-Progress '''
    # Get the current player moves (to evaluate if he won with his last move)
    if current_player == 'X':
        current_player_moves = player_X_moves
    else:
        current_player_moves = player_O_moves

    # Create a condition that will be true if the current player moves have a winning pattern (row, column or diagonal)
    rows_winning_condition = ((current_player_moves[0:3]) == [True]*3) or ((current_player_moves[3:6]) == [True]*3) or ((current_player_moves[6:9]) == [True]*3)
    column1 = current_player_moves[0] and current_player_moves[3] and current_player_moves[6]
    column2 = current_player_moves[1] and current_player_moves[4] and current_player_moves[7]
    column3 = current_player_moves[2] and current_player_moves[5] and current_player_moves[8]
    columns_winning_condition = column1 or column2 or column3
    diagonal1 = current_player_moves[0] and current_player_moves[4] and current_player_moves[8]
    diagonal2 = current_player_moves[2] and current_player_moves[4] and current_player_moves[6]
    diagonals_winning_condition = diagonal1 or diagonal2

    # Check if the current player won
    if rows_winning_condition or columns_winning_condition or diagonals_winning_condition:
        return 'Won'
    # Else if the total number of moves is 9, then the board is full and the game is Null
    elif sum(player_X_moves) + sum(player_O_moves) == 9:
        return 'Null'
    else:
        return 'In-Progress'

def print_score():
    print(f'Player_X / Player_O:        {player_X_Score}/{player_O_Score}')

def manage_game_status():
    '''Function that implements the next step of the game (continue, reset or quit) depending on the game status'''
    global player_X_Score,player_O_Score
    if (status == 'Won') or (status == 'Null'):
        if status == 'Won':
            print(f'Player {current_player} Won!')
            if current_player == 'X':
                player_X_Score += 1
            else:
                player_O_Score += 1
            print_score()
        elif status == 'Null':
            print(f'Game is null')
        # Loop to get a valid user input:
        while True:
            keep_playing_str = input(f'Do you want to keep playing?[y/n]')
            if keep_playing_str == 'y':
                # Reset the game
                reset_the_game()
                break
            elif keep_playing_str == 'n':
                raise GameDone
            else:
                print(f'invalid input: {keep_playing_str}')
    else:
        pass

# Game overall loop (Try, as long as exception GameDone is not thrown via the player input (pressing 'q')
print('------- Tic Tac Toe -------')
print('\nPress num pads to set your marks:')
print(template_board)
time.sleep(5)

# Try statement to catch GameDone exception that will quit the game (exit the while loop)
try:
    # Play as long as the status is In-Progress
    while status == 'In-Progress':
        # Clear the screen
        print('\n' * 20)
        # Display game info
        print_score()
        print('(enter "q" to quit)')
        print('\n')
        # Display the board
        display_board()
        # Get player move
        get_player_move()
        # Display the board
        display_board()
        # Check if game is won, lost or null
        status = get_game_status()
        # If that game is either won or null: display a message and propose to continue playing or quit
        manage_game_status()
        # Alternate user to play next
        alternate_player()
# Handle exception when user wants to quit the game
except GameDone:
    print('\n' * 20)
    print_score()
    print('Goodbye')

