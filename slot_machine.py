"""
Exercise 39. Slot Machine: 
(proposed by Codédex, The Legend of Python.)

    I decided to give it a little tweak so I could have a more robust and practical program.
    - implemented a credits system.
    - added a welcome loop 
    - added a `keep_playing` function to ask the user if he wants to keep testing his luck.

    This exercise includes practice with control flow, while loops, functions, and importing modules.
"""

import sys
import random

    # Function declaration:
def play(credits):
    symbols = ['🍒', '🍇','🍉','7️⃣']
    display = random.choices(symbols, k = 3)
    print(" | ".join(display))
    if display == ['7️⃣', '7️⃣',  '7️⃣']:
        print('-----> Jackpot 💰 <----- ')
        print('💵💴 Congratulation you won the big Prize 💵💴 ')
        sys.exit(0)
    elif display[0] == display[1] and display[0] == display[2]:
        print('Good but not enough')
        return credits + 3
    else:
        print(f'---> {random.choice(bad_luck_phrases)} <---')
        return credits - 1

def keep_playing():
    print()
    answer = int(input('Do you want to keep playing: \n   1) YES \n   2) NO \n '))
    if answer == 2:
        print('---> Goodbye <---')
        return False
    elif answer == 1:
      return True
    
#----------------------
# Main program 
#----------------------

credits = 5
invalid_option = 0
flag = True
welcome_phrases = ['Are you feeling lucky today?', 'Do you want to try your Luck?', 'Do you want to play?']
bad_luck_phrases = ['Try again','Bad Luck this time', 'Luck is not on your side', 'Better luck next time', 'You got nothing', 'You got crushed'] 

print('    +--$$ Welcome to the running Jackpot $$--+')

    # Welcome loop 
while True:
    print(f'          {random.choice(welcome_phrases)}' )
    want_play = (input('   1) Yes \n   2) No \n'))
    if want_play == '1':
        break

    elif want_play == '2':
        print('  ---> Come back later <---  ')
        sys.exit(0)     
    else:
        invalid_option += 1
        if invalid_option == 3: 
            print('--->Too many invalid attempts. Reset your program.<---')
            sys.exit(0)
        else:
            print('    ---> Invalid option <---  ')
            print('---> Select a correct option <---')
            print()

    # Game loop
while flag and credits > 0:
    credits = play(credits)
    print(f'\n---> You have {credits} credits left <---')
    if credits > 0:
        flag = keep_playing()
    else: 
        print('       ---> Game over ! <--- ')
