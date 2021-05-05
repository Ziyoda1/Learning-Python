#!/usr/bin/env python
# coding: utf-8

# In[2]:


usernames = {'Lily', 'John', 'Joe', 'Bob', 'admin' }

a = input('Please enter your name:')
for names in usernames:
    if a in usernames and a != 'admin':
        print(f'Hello {a} nice to see you here!')
        break
    elif a != 'admin':
        print(f'Hello {a}, would you like to see a status report?')
        break
    else:
        print('error')


# In[6]:


usernames = ['Lily', 'John', 'Joe', 'Bob', 'Admin' ]

a = input('Please enter your name:')
for names in usernames:
    if a in usernames and a != 'Admin':
        print(f'Hello {a} nice to see you here!')
        break
    elif a == 'Admin':
        print(f'Hello {a}, would you like to see a status report?')
        break
    else:
        print('error')


# In[1]:


usernames = ['Lily', 'John', 'Joe', 'Bob', 'Admin' ]

a = input('Please enter your name:')
for names in usernames:
    if a in usernames and a != 'Admin':
        print(f'Hello {a} nice to see you here!')
        break
    elif a == 'Admin':
        print(f'Hello {a}, would you like to see a status report?')
        break
    else:
        print('error')


# In[7]:


current_users = ['Lily', 'John', 'Joe', 'Bob', 'Admin' ]
new_users = ['Lily', 'John', 'Jessica', 'Travis', 'Kylie']

guest = [user.lower() for user in current_users]
for new in new_users:
    if new.lower() in guest:
        print("This username, " + new + ", is taken")
    else:
        print("Feel free to use " + new)


# In[1]:


# This is a guess the number game.
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break    # This condition is the correct guess!

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + 'guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))


# In[ ]:




