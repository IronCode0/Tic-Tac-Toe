#Start page
print('+------------------------------+')
print('|         Tic Tac Toe          |')
print('+------------------------------+')
print('\n   Initialing')
from os import system
from time import sleep
import random

def display(board,clear = 1):   # Create Display board
    if clear == 1:
        system('cls')
    print('\n             +-------------+')
    print('             |             |')
    print("             |    " + board[7] + "|" + board[8] + "|" + board[9] + "    |")
    print("             |    " + board[4] + "|" + board[5] + "|" + board[6] + "    |")
    print("             |    " + board[1] + "|" + board[2] + "|" + board[3] + "    |")
    print('             |             |')
    print('             +-------------+\n')

def player_input(): # Take input from user if they want to be '0' or 'X'
    marker = ""
    while not(marker == 'X' or marker == 'O'):
        marker = input("Player 1: Do you want to be X or O: ").upper()
    
    if marker == 'X':
        return('X','O')
    else:
        return('O','X')

def place_marker(board,marker,position):    # fill the user value on board
    board[position] = marker

def win_check(board,mark):  # winning goal
    return( (board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the left 
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right 
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # 2 diagnols
            (board[9] == mark and board[5] == mark and board[1] == mark) )

def space_check(board,position):    # If board is empty
    return board[position] == " "

def choose_first(): # Decide whose turn in first
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def full_board_check(board):    # If board is already full
    empty_space = int(0)
    for i in range(1,10):
        if space_check(board,i):
            empty_space += 1
    if empty_space == 0:
        return True
    else:
        return False

def player_choice(board):   # Take the input from user
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position) :
        try:
            position =  int(input("Please Enter position (1-9): "))
        except:
            position = 0
    return position

def replay():   # if user wants to play it again
    return input("You want to play again (yes , no): ").lower().startswith('y')

#Main Page
system('cls')
system('mode con:cols=40 lines=12')

print('+--------------------------------------+')
print('|             Tic Tac Toe              |')
print('+--------------------------------------+')
print(' Positions on board\n')
print("                  7|8|9")
print("                  4|5|6")
print("                  1|2|3\n")

while True:
    theBoard = [' ']*10
    player1_marker,player2_marker = player_input()
    turn = choose_first()
    game_on = True
    
    while game_on:
        if turn == 'Player 1':
            display(theBoard)
            print('Player 1 turn [ ' + player1_marker + ' ]')
            position = player_choice(theBoard)
            place_marker(theBoard,player1_marker,position)
            
            if win_check(theBoard,player1_marker):
                display(theBoard)
                print('Congratulation! \nPlayer 1 have won the game')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display(theBoard)
                    print('the game is a draw!!')
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            display(theBoard)
            print('Player 2 turn [ ' + player2_marker + ' ]')
            position = player_choice(theBoard)
            place_marker(theBoard,player2_marker,position)
            
            if win_check(theBoard,player2_marker):
                display(theBoard)
                print('Congratulation! \nPlayer 2 have won the game')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display(theBoard)
                    print('the game is a draw!!')
                    game_on = False
                else:
                    turn = 'Player 1'
    if not replay():
        break

system('cls')
print('\n\n')
print('+--------------------------------------+')
print('|         Thankyou for playing         |')
print('|             Tic Tac Toe              |')
print('+--------------------------------------+')
sleep(2)
exit()