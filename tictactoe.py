#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import clear_output

def display_board(board):
    
        clear_output()
        print (' ')
        print (color.PURPLE+'TIC TAC TOE!'+ color.END)
        print (' ')
        print (' ')
        print ('  '+board[1] +'  |  '+board[2]+'  |  '+board[3])
        print ('-----------------')
        print ('  '+board[4] +'  |  '+board[5]+'  |  '+board[6])
        print ('-----------------')
        print ('  '+board[7] +'  |  '+board[8]+'  |  '+board[9])
        print (' ')
        print (' ')


# In[2]:


def player_input():
    
    marker = ''
    
    while marker != 'O' and marker != 'X':
        marker = input("Player 1, do you want to be X or O?: ")
        marker = marker.upper()
      
    
    player1 = marker
    
    if player1 == 'X':
        player2 = 'O'
    else: 
        player2 ='X'
        
    return (player1, player2)    


# In[3]:


def place_marker(board, marker, position):
    
    if position not in range (1,10):
        return 'Your chosen number must be in the range of 1-9'
    else:
        board[int(position)] = marker


# In[4]:


def win_check(board, mark):
    
    if board[1]==board[2]==board[3]==mark:
        return True
    elif board[4]==board[5]==board[6]==mark:
        return True
    elif board[7]==board[8]==board[9]==mark:
        return True
    elif board[1]==board[4]==board[7]==mark:
        return True
    elif board[2]==board[5]==board[8]==mark:
        return True
    elif board[3]==board[6]==board[9]==mark:
        return True
    elif board[1]==board[5]==board[9]==mark:
        return True
    elif board[3]==board[5]==board[7]==mark:
        return True 
    else:
        return False 
        


# In[5]:


import random

def choose_first():
    if random.randint(0,1):
        return 'X goes first'
    else:
        return 'O goes first'


# In[6]:


def space_check(board, position):
    
     return board[position] == ' '


# In[7]:


def full_board_check(board):
    
    return board.count(' ')==1 


# In[8]:


def player_choice(board):
    
    position = ''
    
    while True:
        position = int(input('Pass a number in a range 1-9: '))
        if position not in range (1,10):
            continue
        elif space_check(board, position):
            return position
        else:
            print ('This number has been taken, choose another one')
            continue


# In[9]:


def replay():
    
    answer= ''
    
    while answer.lower() != 'yes' and answer.lower() != 'no':
        answer = input('Do you want to start the game? Yes or No: ')
    
    return answer.lower() == 'yes'


# In[10]:


class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


# In[11]:


print(f'{color.PURPLE}Welcome to Tic Tac Toe!{color.END}')

    
while replay(): 
    board = [' ']*10
    display_board(board)
    print(' ')
    print(player_input())
    print(f'{color.BLUE}Player1, Player2{color.END}')
    print(' ')
    print(f'{color.BOLD}The randomly selected player to go first: {color.END}')
    result = choose_first()
    print(result)
    if result == 'X goes first':
        player1='X'
        player2='O'
    else: 
        player1='O'
        player2='X'
        
    while not win_check(board,'X') or not win_check(board,'O'): 
            
                
        #Player1
        position = player_choice(board)
        place_marker(board, player1, position)
        display_board(board)
            
        #Win Check
        if win_check(board, player1): 
            print (' ')
            print ( f'{color.BLUE}Congratulations {player1} you have WON THE GAME!{color.END}')
            break 
            
        if full_board_check(board):
            print (f"{color.BLUE}Oh wow! It's a TIE! The board is full and you have both won : {color.END}" )
            break
                
        #Player2
        position = player_choice(board)
        place_marker(board, player2, position)
        display_board(board)
            
        #Win Check
        if win_check(board, player2): 
            print (' ')
            print (f'{color.BLUE} Congratulations {player2} you have WON THE GAME!{color.END}')
            break 
            
        if full_board_check(board):
            print (f"{color.BLUE}Oh wow! It's a TIE! The board is full and you have both won :{color.END} ")
            break   

print (color.BOLD+'Thank you playing the game, see you soon!' + color.END)


# In[ ]:




