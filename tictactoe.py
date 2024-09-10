def display(board):
    #making the board
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()
  


def player_input():
   
    #asking player one to pick a marker
    Player1 = input("Player 1 please pick your marker, either X or O: ")

    #if player one pick X player to is O
    if Player1 == 'X':
        Player2 = 'O'
    #vice versa
    elif Player1 == 'O':
        Player2 = 'X'
    #if niether are picked reset
    else: 
        print("Invalid input. Please choose X or O.")
    
    print("Player 1 is", Player1, "player 2 is", Player2)
    return Player1, Player2

def win_check(board, mark):
    
   #checking rows to see if they winxe
    return (
        (board[0] == board[1] == board[2] == mark) or
        (board[3] == board[4] == board[5] == mark) or
        (board[6] == board[7] == board[8] == mark) or
        (board[0] == board[3] == board[6] == mark) or
        (board[1] == board[4] == board[7] == mark) or
        (board[2] == board[5] == board[8] == mark) or
        (board[0] == board[4] == board[8] == mark) or
        (board[2] == board[4] == board[6] == mark)
    )

def play_game():

    board = [' '] * 9  # Initialize the board with empty spaces
    Player1, Player2 = player_input()
    curr_player = Player1

    for i in range(9):
        display(board)
        
        while True:
            try:
                move = int(input(f"Player {curr_player}, make your move (1-9): ")) - 1
                if move < 0 or move > 8 or board[move] != ' ':
                    print("Invalid move. The cell is either out of range or already taken.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")
        
        # Make the move for the current player
        board[move] = curr_player
        
        # Check if the current player has won
        if win_check(board, curr_player):
            display(board)
            print(f"Player {curr_player} wins!")
            return  # Exit the function if there's a winner
        
        # Switch the player
        curr_player = Player1 if curr_player == Player2 else Player2
    
    # If the loop ends and no winner, it's a tie
    display(board)
    print("It's a tie!")

# Start the game
play_game()