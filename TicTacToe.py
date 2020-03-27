# Tic Tac Toe game

# Initialize
my_player_X_moves = [True,False,False,False,False,True,False,False,False]
my_player_O_moves = [False,True,False,False,False,False,False,False,False]

def which_symbol(move_X,move_O):
    '''Functiun that returns the symbol to be displayed in a given board location'''
    if move_X:
        return 'X'
    elif move_O:
        return 'O'
    else:
        return ' '

def display_board(player_X_moves,player_O_moves):
    '''Function that displays the Tic Tac Toe Board based on users moves'''
    board_data = [which_symbol(tup[0], tup[1]) for tup in zip(player_X_moves, player_O_moves)]
    # Create a list that will hold X or O in each position of the board
    board_data = [which_symbol(tup[0], tup[1]) for tup in zip(my_player_X_moves, my_player_O_moves)]
    # Create the board based on its data
    board = f"{board_data[6]}|{board_data[7]}|{board_data[8]}\n" \
            f"{board_data[3]}|{board_data[4]}|{board_data[5]}\n" \
            f"{board_data[0]}|{board_data[1]}|{board_data[2]}\n"
    # Print out the board
    print(board)

display_board(my_player_X_moves,my_player_O_moves)