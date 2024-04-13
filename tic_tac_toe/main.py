import random
import time

print("Welcome to Tic Tac Toe!")

# constant
GAME_BOARD = """
_1_|_2_|_3_
_4_|_5_|_6_
 7 | 8 | 9
"""

# board
board_str = """
___|___|___
___|___|___
   |   |   """

# key:value   k  v   k  v
board_dict = {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: ""}

# position =- index in string
board_positions = {1: 2, 2: 6, 3: 10, 4: 14, 5: 18, 6: 22, 7: 26, 8: 30, 9: 34}

def player_is_valid(xter):
    """Ensure player choose valid character"""
    if  xter.upper() == "X" or xter.upper() == "O":
        return True

def set_player_xter():
    """choose your xter"""
    player_xter = input("Select your character ('O' or 'X'): ")
    while not player_is_valid(player_xter.upper()):
        print("You may be either 'O' or 'X'")
        player_xter = input("Select your character ('O' or 'X'): ")

    return player_xter.upper()

def set_pc_xter(player_xter):
    if player_xter == 'X':
        return 'O'
    else:
        return 'X'

def players_turn_is_valid(turn):
    """Ensure player choose valid turn"""
    if  turn == "1" or turn == "2":
        return True
    
def set_players_turn():
    """choose your turn"""
    players_turn = input("Select your turn ('1' or '2'): ")
    while not players_turn_is_valid(players_turn):
        print("You may be either '1' or '2'")
        players_turn = input("Select your turn ('1' or '2'): ")

    return int(players_turn)

def set_pc_turn(player_turn):
    if player_turn == 1:
        return 2
    else:
        return 1

def players_move_is_valid(position):
    """Ensure player choose valid position on the game board"""
    # if  position == "1" or position == "2" or position == "3" or position == "4":
    try:
        if int(position) in board_dict:
            return True
    except ValueError:
        print("You need to enter an interger")

def get_player_move():
    """choose a position on the board for player"""
    position = input("Select your turn ('1', '2', '3', '4', '5', '6', '7', '8', or '9'): ")
    while not players_move_is_valid(position):
        # print("You may choose either '1', '2', '3', '4', '5', '6', '7', '8', or '9'")
        position = input("Select your turn ('1', '2', '3', '4', '5', '6', '7', '8', or '9'): ")

    return int(position)

def get_pc_move():
    """choose a position on the board for PC"""
    available_positions = [key for key in board_dict if board_dict[key] == '']
    # print("available:", available_positions)
    print("waiting for PC's move")
    position = random.choice(available_positions)
    wait = random.randint(2,4)
    # print(wait, "seconds")
    time.sleep(wait)
    return position

def check_board_position(position):
    # check if position is already taken on the board
    if (board_dict[position] != ''):
        return False
    else:
        return True

def update_board(board, position, xter):
    # update the game board with player's character
    board_dict[position] = xter
    index = board_positions[position]
    string_list = list(board)
    string_list[index] = xter
    updated_board = "".join(string_list)

    return updated_board

def check_for_winner():
    """Check to see if we have a winner"""
    winner = ""
    # check positions 1, 2, 3
    if(board_dict[1] != "" and board_dict[1] == board_dict[2] and board_dict[2] == board_dict[3]):
        # print(f"{board_dict[1]} == {board_dict[2]} and {board_dict[2]} == {board_dict[3]}")
        winner = board_dict[1]
    # check positions 4, 5, 6
    elif(board_dict[4] != "" and board_dict[4] == board_dict[5] and board_dict[5] == board_dict[6]):
        # print(f"{board_dict[4]} == {board_dict[5]} and {board_dict[5]} == {board_dict[6]}")
        winner = board_dict[4]
    # check positions 7, 8, 9
    elif(board_dict[7] != "" and board_dict[7] == board_dict[8] and board_dict[8] == board_dict[9]):
        # print(f"{board_dict[7]} == {board_dict[8]} and {board_dict[8]} == {board_dict[9]}")
        winner = board_dict[7]
    # check positions 1, 3, 7
    elif(board_dict[1] != "" and board_dict[1] == board_dict[4] and board_dict[4] == board_dict[7]):
        # print(f"{board_dict[1]} == {board_dict[4]} and {board_dict[4]} == {board_dict[7]}")
        winner = board_dict[1]
    # check positions 2, 5, 8
    elif(board_dict[2] != "" and board_dict[2] == board_dict[5] and board_dict[5] == board_dict[8]):
        # print(f"{board_dict[2]} == {board_dict[5]} and {board_dict[5]} == {board_dict[8]}")
        winner = board_dict[2]
    # check positions 3, 6, 9
    elif(board_dict[3] != "" and board_dict[3] == board_dict[6] and board_dict[6] == board_dict[9]):
        # print(f"{board_dict[3]} == {board_dict[6]} and {board_dict[6]} == {board_dict[9]}")
        winner = board_dict[3]
    # check positions 1, 5, 9
    elif(board_dict[1] != "" and board_dict[1] == board_dict[5] and board_dict[5] == board_dict[9]):
        # print(f"{board_dict[1]} == {board_dict[5]} and {board_dict[5]} == {board_dict[9]}")
        winner = board_dict[1]
    # check positions 3, 5, 7
    elif(board_dict[3] != "" and board_dict[3] == board_dict[5] and board_dict[5] == board_dict[7]):
        # print(f"{board_dict[3]} == {board_dict[5]} and {board_dict[5]} == {board_dict[7]}")
        winner = board_dict[3]
    
    return winner

def main():
    # set player's xter
    player = set_player_xter()
    print("You are", player, "player")
    # set pc's xter
    pc = set_pc_xter(player)
    print("The PC is", pc, "player")

    pc_move = False

    # set players's turn
    players_turn = set_players_turn()
    print("You go on turn", players_turn)
    # set pc's turn
    pc_turn = set_pc_turn(players_turn)
    print("PC goes on turn", pc_turn)

    if (pc_turn == 1):
        pc_move = True

    # display instructions
    print("\nGame board:", GAME_BOARD)
    print("As you can see, there are 9 positions on the board.")

    end_of_game = False
    no_of_moves = 0
    current_board = board_str

    print("\nBoard:", current_board)

    while not end_of_game:
        game_winner = check_for_winner()
        if (game_winner != ""):
            # print("We have a winner")
            if (game_winner == player):
                print("\nCongratulations! You have won the game")
            else:
                print("\nGame Over! You lost!")
            
            end_of_game = True
            break

        print("Select a position (from 1 to 9) to place your character.")

        if (pc_move):
            pc_position = get_pc_move()
            no_of_moves += 1
            pc_move = False
            current_board = update_board(current_board, pc_position, pc)
            # print("PC places", pc, "on", pc_position)
        else:
            # wait for player's move
            players_position = get_player_move()
            if (check_board_position(players_position)):
                no_of_moves += 1
                # print("Player wants to place his/her xter at", players_position)
                # print("put", player, "in", players_position)

                current_board = update_board(current_board, players_position, player)

                pc_move = True
            else:
                print("Invalid move! Position already taken.")
        
        print("\nBoard:", current_board, "\nState:", board_dict, "\nTotal moves:", no_of_moves)

        if (no_of_moves == 9):
            game_winner = check_for_winner()
            if (game_winner == ""):
                print("\nGame ended in a tie!")
            else:
                if (game_winner == player):
                    print("\nCongratulations! You have won the game")
                else:
                    print("\nGame Over! You lost!")
                
            end_of_game = True

    # print("Board:", current_board, "\nState:", board_dict, "\nTotal moves:", no_of_moves)
    print("The game was completed in", no_of_moves, "moves.\n\n")

main()
input("Press enter key to exit.")