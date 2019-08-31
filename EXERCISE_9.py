'''Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
(Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.'''

import random

a = random.randint(1,9)   
b = input('Guess a number: ')
c=0


while True :
    if (b == 'exit') :
        break
    if ((a-int(b))>0) :
        print('You guess too low. Try again !')
        c+=1
    if ((a-int(b))<0) :
        print('You guess to high.Try again !')
        c+=1
    b = input('Guess a number: ')
    if (a==int(b)):
        print('You guess! \n Number of Your tries: ',c+1)
        c=0
        a = random.randint(1,9)
        b = input('Guess a number: ')
        continue
