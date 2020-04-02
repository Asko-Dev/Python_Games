#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random

def kamen_nuzky_papir():
    print('RULES\n')
    print('Enter Kamen, Nuzky or Papir.')
    print("Enter 'stop' for ending the game.")
    
    while True:
        options = ('Kamen', 'Nuzky', 'Papir')
        player =''
        
        while player.lower() not in ['kamen','nuzky','papir','stop']:
            player = input('What do you choose?:  ')
        
        player = player.capitalize()
        computer = random.choice(options)
        
        if player == 'Stop': 
            break
        elif player == computer:
            print(f'\nPlayer: {player}, Computer: {computer}.')
            print("It's a TIE!")
        elif player == 'Kamen' and computer == 'Nuzky' or player == 'Papir' and computer == 'Kamen' or player == 'Nuzky' and computer=='Papir':
            print(f'\nPlayer: {player}, Computer: {computer}.')
            print("The player has WON!")
        else: 
            print(f'\nPlayer: {player}, Computer: {computer}.')
            print("The computer has WON!")

    print('\nThank you for playing')

kamen_nuzky_papir()


# In[ ]:




