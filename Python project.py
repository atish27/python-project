#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import time
name = input("What is your name? ")
print ("Hello, " + name, "Time to play raja,rani,chor,police !")
time.sleep(1)

print('*          Rules...!!              *')
print('************************************')
print('It is a simple game where you have to guess whether...')
print('who is chor & police if you are mantri...')
print('If you are police you will get 100 points...')
print('If you are chor you will get 00 points...')
print('If you are mantri & your guess is correct you will get 150 points...')
print('If you are king you will get 300 points...')
print('If you are Queen you will get 200 points...')
print()
print('#####################################################')
print()

PScore=0
CScore=0
count = 0
while (count < 3):
    print('Starting Game Wait For A Sec...')
    time.sleep(3)
    royal = ['raja', 'rani','mantri']
    people = ['chor','police']

    chooseRoyal = random.choice(royal)

    if chooseRoyal.lower() == 'raja':
        time.sleep(2)
        print('Congrats you are Raja')
        print('Congrats you get 300 Points')
        PScore=PScore+300
        
    elif chooseRoyal.lower() == 'rani':
        time.sleep(2)
        print('Congrats you are Rani')
        print('Congrats you get 200 Points')
        PScore=PScore+200
    
    elif chooseRoyal.lower() == 'mantri':
        time.sleep(2)
        print('Congrats You Are a Mantri')
        time.sleep(2)
        print()
        print('On Raja Command Find Who Is CHOR & POLICE')
        guess = input('Who am I chor or police :')
        
        choosePeople = random.choice(people)

        if guess.lower() == choosePeople:
            time.sleep(2)
            print('You are correct')
            time.sleep(2)
            print('he is ',choosePeople)
            PScore=PScore+150
            print('Congrats you get 150 Points')
        if guess.lower() != choosePeople:
            time.sleep(2)
            print('You are wrong')
            time.sleep(2)
            print('he is ',choosePeople)
            CScore=CScore+150
            print('Congrats you get 0 Points')
    print()
    input('Press Enter to start again')

    count = count + 1
    
print(f'total {name} Score is =',PScore)
print('total Computer Score is =',CScore)
if (PScore > CScore):
    print(f'{name} Wins')
elif (CScore > PScore):
    print('Computer Wins')
elif (PScore == CScore):
    print('Both Score Are Equal So nobody Wins')
    


# In[ ]:





# In[ ]:




