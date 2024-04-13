# import random and time functions
import random as random
import time as time


# declare all variables, lists and tuple to be used for quick refrence
CONDITION = (['1','2','3'],['4','5','6'],['7','8','9'],['1','4','7'],['2','5','8'],['3','6','9'],['1','5','9'],['3','5','7'])
iterator = False
entries = { str(num+1):"" for num in range(9) }          
spacer = ["_" if num < 6 else " " for num in range(9)]
available_entries = list(entries.keys())
player_picks = []
pc_picks = []
delay = [1,2,3]
end = []


# welcome player to the game 
print('welcome to Tic Tac Toe!\n')


# using while loop to prompt user for desired character 
while iterator == False: 
    char = input("please select your character ('O' or 'X'):").capitalize()
    if char == 'O': pc = 'X'; break 
    elif char =='X': pc = 'O'; break
    else: print("Invalid input:: you may be either ('O' or 'X')")
# display characters of player and pc
print(f'You are player {char}')
print(f'The pc is player {pc}')


# using while loop to prompt user for player that goes first
while iterator == False: 
    user = input("select your turn('1' or '2')")
    if user == '1': pc_turn = 2; user_turn = 1; break 
    elif user == '2': pc_turn = 1; user_turn = 2; break
    else: print("Invalid input:: you may be either ('1' or '2')")
# display turns of player and pc
print(f'You go on turn {user_turn}')
print(f'The pc goes on turn {pc_turn}')


# generate board format saved in variable board
board_format = '''
Game board:
    _1_|_2_|_3_
    _4_|_5_|_6_
     7 | 8 | 9
'''

# generate the board with replacable variables from the spacer list
def draw_board():
    new_board = f'''
Board:
    _{spacer[0]}_|_{spacer[1]}_|_{spacer[2]}_
    _{spacer[3]}_|_{spacer[4]}_|_{spacer[5]}_
     {spacer[6]} | {spacer[7]} | {spacer[8]} 
'''
    return new_board


# display board and board format to visually inform the player about the game
print(board_format)
print('As you can see there are 9 positions on the board.\n')
print(draw_board())
print('select a position (form 1 - 9) to place your character')


# takes users input and updates the board
def player_moves():
    print(f'player moves as {char}')  
    log = input(f'player select your next move: you have {available_entries} : ')
    if log in available_entries: 
        player_picks.append(log)
        available_entries.pop(available_entries.index(log))
        entries[log] = char
        spacer[int(log)-1] = char
        print(draw_board())
        print(f'board entries {entries}')
    else: print('invalid entry'); player_moves()
    for x in CONDITION:
        if all(e in player_picks for e in x): print('Congrats player, you won!'); end.append('yes'); break

# takes pc inputs and updates the board 
def pc_moves():
    print(f'pc moves as {pc}')
    print('waiting for pc')    
    time.sleep(random.choice(delay))
    movess = random.choice(available_entries)
    pc_picks.append(movess)
    available_entries.pop(available_entries.index(movess))
    entries[movess] = pc
    spacer[int(movess)-1] = pc
    print(draw_board())   
    print(f'board entries {entries}')
    for x in CONDITION:
        if all(e in pc_picks for e in x): print('Pc has won'); end.append('yes'); break


# code sequence in a loop based on turn 1 then turn 2
while iterator == False:
    if user == '1': 
        player_moves()
        if 'yes' in end: break
        if len(available_entries) == 0: print("game ends as a draw"); break
        pc_moves()
        if 'yes' in end: break
    else: 
        pc_moves()
        if 'yes' in end: break
        if len(available_entries) == 0: print("game ends as a draw"); break
        player_moves() 
        if 'yes' in end: break

print("game over")
