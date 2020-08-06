# Tic Tac Toe game
import random
import subprocess


def display_board(board):
    subprocess.call("cls", shell=True)# works on windows os
    print(' {}|{}|{}'.format(board[1],board[2],board[3]))
    print('-------')
    print(' {}|{}|{}'.format(board[4],board[5],board[6]))
    print('-------')
    print(' {}|{}|{}'.format(board[7],board[8],board[9]))
    
def player_input(turn,player_mark):
    symbol=''
    while symbol not in ['X','O']:
        symbol=input('Player{} you want to (X or O): '.format(turn)).upper()
        
        if symbol not in ['X','O']:
            print('Sorry invalid choice, you can choose only X or O')
            
    if symbol=='X':
        player_mark[turn]=symbol
        player_mark[-turn]='O'
        
    else:
        player_mark[turn]=symbol
        player_mark[-turn]='X'

def place_marker(board, marker, position):
    board[position]=marker

def win_check(board, mark):
    if mark==board[1] and mark==board[2] and mark==board[3]:
        #print(1)
        return True
    elif mark==board[4] and mark==board[5] and mark==board[6]:
        #print(2)
        return True
    elif mark==board[7] and mark==board[8] and mark==board[9]:
        #print(3)
        return True
    elif mark==board[1] and mark==board[4] and mark==board[7]:
        #print(4)
        return True
    elif mark==board[2] and mark==board[5] and mark==board[8]:
        #print(5)
        return True
    elif mark==board[3] and mark==board[6] and mark==board[9]:
        #print(6)
        return True
    elif mark==board[1] and mark==board[5] and mark==board[9]:
        #print(7)
        return True
    elif mark==board[3] and mark==board[5] and mark==board[7]:
        #print(8)
        return True
    else:
        #print(0)
        return False

def choose_first():
    first_play=random.randint(1,2)
    print('Player{} gets first chance to play'.format(first_play))
    return first_play

def space_check(board, position):
    return board[position]==' '

def full_board_check(board):
    for i in board:
        if i==' ':
            return False
        else:
            pass
        
    return True


def player_choice(board):
    position=''
    while position not in range(1,10):
            p=input('Enter the position in the range(1-9): ')
            
            if p.isdigit():
                position=int(p)
                if position not in range(1,10):
                    print('Sorry invalid position, you can choose only in the range(1-9)')
                else:
                    is_free=space_check(board, position)
                    if is_free==True:
                        return position
                    else:
                        print('The position is not empty, try again')
                        position=''
                    
                
            else:
                 print('Sorry invalid input, you can enter no only ')
         

def replay():
    choice=''
    while choice not in ['Yes','No']:
        choice=input('Do you want to play again (Yes or No): ')
        
        if choice not in ['Yes','No']:
            print('Sorry invalid choice, you can choose only Yes or No')
            
            
    return choice=='Yes'






game_on=True
player_mark=['#',1,2]
board=['#',1,2,3,4,5,6,7,8,9]
print('Welcome to Tic Tac Toe!')    
while game_on==True:
    
    for loc in range(1,10):
        board[loc]=' '
        
    game_over=False   
    turn=choose_first()
    player_input(turn,player_mark)
    display_board(board)
    
    while game_over==False:
        
        #Player 1 Turn
        print('Player{}'.format(turn))
        position=player_choice(board)
        place_marker(board, player_mark[turn],position)
        display_board(board)
        if win_check(board,player_mark[turn])==True:
            print('Player{} has won'.format(turn))
            game_over==True
            break
        elif full_board_check(board)==True:
            print('The game is a draw')
            game_over==True
            break
            
        # Player2's turn.     
        print('Player{}'.format(3-turn))
        position=player_choice(board)
        place_marker(board, player_mark[-turn],position)
        display_board(board)
        if win_check(board,player_mark[-turn])==True:
            print('Player{} has won'.format(3-turn))
            game_over==True
            break
        elif full_board_check(board)==True:
            print('The game is a draw')
            game_over==True
            break
        
        
    game_on=replay()
