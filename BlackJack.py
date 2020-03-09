#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[2]:


def cards_player(cards_P):
    
    clear_output()
    print (f'{color.PURPLE} ________   ________   ________{color.END} ')
    print (f'{color.PURPLE}|        | |        | |        |{color.END}')
    print (f'{color.PURPLE}|        | |        | |        |{color.END}')
    print (f'{color.PURPLE}|        | |        | |        |{color.END}')
    print (f'{color.PURPLE}|        | |        | |        |{color.END}')
    print (f'{color.PURPLE}|        | |        | |        |{color.END}')
    print (f'{color.PURPLE}|        | |        | |        |{color.END}')
    print (f'{color.PURPLE}|________| |________| |________|{color.END}')
    print (cards_P[0]+'   '+cards_P[1]+'   '+cards_P[2])
    print (' ')
    print (' ')


# In[3]:


def cards_computer(cards_P,cards_C):
    
    clear_output()
    print (f'{color.PURPLE} ________   ________   ________{color.END} ')
    print (f'{color.PURPLE}|        | |        | |        |{color.END}')
    print (f'{color.PURPLE}|        | |        | |        |{color.END}')
    print (f'{color.PURPLE}|        | |        | |        |{color.END}')
    print (f'{color.PURPLE}|        | |        | |        |{color.END}')
    print (f'{color.PURPLE}|        | |        | |        |{color.END}')
    print (f'{color.PURPLE}|        | |        | |        |{color.END}')
    print (f'{color.PURPLE}|________| |________| |________|{color.END}')
    print (cards_P[0]+'   '+cards_P[1]+'   '+cards_P[2])
    print (' ')
    print (' ')
    print (f'{color.GREEN} ________   ________   ________ {color.END}')
    print (f'{color.GREEN}|        | |        | |        |{color.END}')
    print (f'{color.GREEN}|        | |        | |        |{color.END}')
    print (f'{color.GREEN}|        | |        | |        |{color.END}')
    print (f'{color.GREEN}|        | |        | |        |{color.END}')
    print (f'{color.GREEN}|        | |        | |        |{color.END}')
    print (f'{color.GREEN}|        | |        | |        |{color.END}')
    print (f'{color.GREEN}|________| |________| |________|{color.END}')
    print (cards_C[0]+'   '+cards_C[1]+'   '+cards_C[2])


# In[4]:


def Players_Input():
        
    while True:
        if len(cards_P)!=3:
            answer = ''
            while answer.lower() != 'y' and answer.lower() != 'n':
                answer = input('Do you want to draw a card? Y or N: ')
            if answer.lower() == 'y' and len(cards_P) <= 2:
                if bust_check(values_player):
                    break
                card = random.choice(list(carddeck.items()))
                if card == ('Ace_Club', 0) or card == ('Ace_Spade', 0) or card == ('Ace_Heart', 0) or card == ('Ace_Diamond', 0):
                    newcard = list(card)
                    while newcard[1] != 1 and newcard[1] != 11:
                        try:
                            newcard[1] = int(input('You have drawn an Ace! Ace has two values. Do you want 1 or 11?:  '))
                            break
                        except:
                            print (f'{color.BOLD}\nInput one of the numbers 11 or 1{color.END}')
                            continue
                    cards_P.append(newcard[0])
                    values_player.append(int(newcard[1])) 
                    print (f'\nYour card is {newcard[0]}\nYour current point count is:  {sum(values_player)}')
                else:
                    cards_P.append(card[0])
                    values_player.append(int(card[1]))
                    print (f'\nYour card is {card[0]}\nYour current point count is:  {sum(values_player)}')
            else:
                if len(cards_P) == 0:
                    cards_P.append('NO CARD')
                    cards_P.append('NO CARD')
                    cards_P.append('NO CARD')
                elif len(cards_P) == 1:
                    cards_P.append('NO CARD')
                    cards_P.append('NO CARD')
                elif len(cards_P) == 2:
                    cards_P.append('NO CARD')
                else:
                    break
        else: 
            cards_player(cards_P)
            print ('Computers turn.')
            break
            
    while True:
        if bust_check(values_player):
            break
        while sum(values_computer) < 21 and len(cards_C)<2:
            if bust_check(values_computer):
                break
            card = random.choice(list(carddeck.items()))
            if card == ('Ace_Club', 0) or card == ('Ace_Spade', 0) or card == ('Ace_Heart', 0) or card == ('Ace_Diamond', 0):
                newcard = list(card)
                if (sum(values_computer)+11) <=21:
                    newcard[1]= 11
                    cards_C.append(newcard[0])
                    values_computer.append(int(newcard[1])) 
                    continue
                else: 
                    newcard[1]= 1
                    cards_C.append(newcard[0])
                    values_computer.append(int(newcard[1]))
                    continue
            else:
                cards_C.append(card[0])
                values_computer.append(int(card[1]))
                continue
        if sum(values_computer) == 21:
            break
        elif len(cards_C) == 2:
            if sum(values_player) >= sum(values_computer):
                card = random.choice(list(carddeck.items()))
                cards_C.append(card[0])
                values_computer.append(int(card[1]))
                if bust_check(values_computer):
                    break
                break
            else:
                cards_C.append('NO CARD')
                break
        else: 
            break

    if len(cards_C)!= 3:
        cards_C.append(' ')
        cards_C.append(' ')
        cards_C.append(' ')
    cards_computer(cards_P, cards_C)
    print (' ')
    print (' ')
    print (f'{color.BOLD}The final point count is:\nComputer:  {sum(values_computer)}\nPlayer:  {sum(values_player)}{color.END}')
    
    if bust_check(values_computer)== False and bust_check(values_player) == False:
        win_check(values_computer, values_player)
    
    elif bust_check(values_computer)== True:
        print ('\nComputer has exceeded 21! The Player wins!')
        
    elif bust_check(values_player)== True:
        print ('\nPlayer has exceeded 21! The Computer wins!')
        
        


# In[5]:


def replay():
    replay = ''
    while replay.lower() != 'y' and replay.lower() != 'n':
        replay = input('\nDo you want to start the game? Y or N:  ')
        continue
    if replay.lower() == 'y':
        return True
    else: 
        return False


# In[6]:


def win_check(value_computer, value_player):
    if sum(value_computer) == sum(value_player):
        print (f"{color.BLUE}\nIt's a TIE!{color.END}")
    elif sum(value_computer) > sum(value_player):
        print (f'{color.BLUE}\nCOMPUTER HAS WON THE GAME!{color.END}')
    elif sum(value_computer) < sum(value_player):
        print (f'{color.BLUE}\nPLAYER HAS WON THE GAME!{color.END}')
    


# In[7]:


def bust_check(value):
    return sum(value) > 21


# In[8]:


class Player25:
    
    def __init__(self, player, balance):
        self.player = player
        self.balance = balance
    
    def amount(self):
        bet_amount = 0
        while bet_amount not in range(1,self.balance+1):
            try:
                bet_amount = int(input(f'{color.BOLD}Enter a BET smaller than or equal to {self.balance}$:  {color.END}'))
            except:
                print(f'{color.BOLD}It has to be a NUMBER and SMALLER than your balance of {self.balance}$: {color.END}')
                continue
        
        self.bet_amount = bet_amount
        print (f'\n{color.BOLD}You have betted {bet_amount}$!{color.END}')
    
    def bet(self):
        if sum(values_computer) == sum(values_player):
            self.balance = self.balance
            print (f'{color.GREEN}\nYour bet amount of {self.bet_amount} has been cancelled! Currently your balance is {self.balance}${color.END}')          
        elif sum(values_computer) > sum(values_player) and sum(values_computer) <= 21:
            self.balance = self.balance - self.bet_amount
            print (f'{color.GREEN}\nYour bet amount of {self.bet_amount} has been deducted! Currently your balance is {self.balance}${color.END}')      
        elif sum(values_player) > sum(values_computer) and sum(values_player) <= 21:
            self.balance = self.balance + self.bet_amount 
            print (f'{color.GREEN}\nYour bet amount of {self.bet_amount} has been added! Currently your balance is {self.balance}${color.END}')
        elif sum(values_computer) > sum(values_player) and sum(values_computer) >= 22:
            self.balance = self.balance + self.bet_amount
            print (f'{color.GREEN}\nYour bet amount of {self.bet_amount} has been added! Currently your balance is {self.balance}${color.END}')
        else: 
            self.balance = self.balance - self.bet_amount
            print (f'\n{color.GREEN}Your bet amount of {self.bet_amount} has been deducted! Currently your balance is {self.balance}${color.END}') 
            
    def negative(self):
        if self.balance <= 0:
            self.balance = 100
            print (f"\n{color.BOLD}{color.RED}OOPSS, your balance is 0${color.END}")
            print (f'{color.RED}YOU HAVE LOST ALL YOUR MONEY AND THIS GAME! TRY AGAIN WITH DEFAULT 100$ {color.END}')   
        else:
            pass
            
            


# In[9]:


import random
from IPython.display import clear_output
print (f'{color.RED}Welcome to a BlackJack Game by Scotty!{color.END}')
print (f'\n{color.BOLD}The Rules:{color.END}\n- State your name when asked.\n- Your initial balance is 100$.\n- Your goal is to reach 21 or have more than the dealer without exceeding 21.\n- You can draw up to 3 cards.\n- Jack, Queen and King are the value of 10. Ace is 1 or 11, depends on your choice.')

print (f"\n{color.BOLD}Nice to meet you, what's your name?{color.END}")
playername = str(input(f'{color.BLUE}Your name: {color.END}'))
print (f'\n{color.BLUE}Hello {playername}! Your starting balance is 100$. Think about how much you want to bet and start the GAME! {color.END}')
balance = 100
gamestart = Player25(playername, balance)

while replay():
    carddeck = {'Ace_Club':0, '2_Clubs':2,'3_Clubs':3,'4_Clubs':4,'5_Clubs':5,'6_Clubs':6,'7_Clubs':7,'8_Clubs':8,'9_Clubs':9,'10_Clubs':10,
               'Jack_Clubs':10, 'Queen_Clubs':10,'King_Clubs':10,'Ace_Spade':0, '2_Spades':2,'3_Spades':3,'4_Spades':4,'5_Spades':5,'6_Spades':6,'7_Spades':7,'8_Spades':8,'9_Spades':9,'10_Spades':10,
               'Jack_Spades':10, 'Queen_Spades':10,'King_Spades':10,'Ace_Heart':0, '2_Hearts':2,'3_Hearts':3,'4_Hearts':4,'5_Hearts':5,'6_Hearts':6,'7_Hearts':7,'8_Hearts':8,'9_Hearts':9,'10_Hearts':10,
               'Jack_Hearts':10, 'Queen_Hearts':10,'King_Hearts':10,'Ace_Diamond':0, '2_Diamonds':2,'3_Diamonds':3,'4_Diamonds':4,'5_Diamonds':5,'6_Diamonds':6,'7_Diamonds':7,'8_Diamonds':8,'9_Diamonds':9,'10_Diamonds':10,
               'Jack_Diamonds':10, 'Queen_Diamonds':10,'King_Diamonds':10}
   
    values_player = [0]
    values_computer = [0]
    cards_P=[]
    cards_C=[]

    gamestart.amount()
    Players_Input()
    gamestart.bet()
    gamestart.negative()
    
print (f'\n{color.BOLD}Thank you for playing{color.END}')




# In[ ]:




