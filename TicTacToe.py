# Tic Tac Toe game

# Initialize lists to represent the moves of each player
player_X_moves = [False]*9
player_O_moves = [False]*9

# Create a string to manage which of the players (X or O) is to play. Start with X.
current_player = 'X'

def get_player_move():
    '''Function that gets player input and update his/her moves accordingly'''
    player_input_str = input(f"Player {current_player}:")
    ## Try to cast the player input into an int
    try:
        player_input = int(player_input_str)
        if player_input in range(1,10):
            print(f"valid input: {player_input}")
            if current_player == 'X':
                player_X_moves[player_input-1] = True
            else:
                player_O_moves[player_input-1] = True
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

def alternate_player(player):
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
    return player

for i in range(0,3):
    # Get player move
    get_player_move()
    # Display the board
    display_board()
    # Check if game is won, lost or null
    # If that game is either won, lost or null: display a message and propose to continue playing or quit
    # Alternate user to play next
    current_player = alternate_player(current_player)



