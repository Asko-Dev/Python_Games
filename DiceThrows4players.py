#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random
from IPython.display import clear_output

results = []
    
for num in range(1,5):
    rolls = []
    number = 0
    question =''
    
    print('-----------------------------')
    print (f'\nHello player{num}.')
    
    while question not in ['y','n']:
        question = input('Roll the dice? y/n: ').lower()
        clear_output()

        if question == 'n':
            break

        elif question == 'y':
            while number != 6:            
                number = random.randint(1,7)
                rolls.append(number)
                print (f'\nYou have rolled {number}')

    print (f'\nCongrats player{num}! You have rolled 6. It took you {len(rolls)} attempts')
    results.append(len(rolls))
    
clear_output()

print(f'\nThe amount of throws for each player is {results}')
print(f'\nPlayer{results.index(min(results))+1} is the WINNER with only {min(results)} throws. CONGRATULATIONS')


# In[ ]:




