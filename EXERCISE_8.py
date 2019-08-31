'''Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner,
and ask if the players want to start a new game)'''
import random


while True :
    print('#'*40,'\nWelcome to Rock-Paper-Scisors game! \nChoose Your item:\n1 - Rock\n2 - Paper\n3 - Scissors')
    a = int(input('Your choise: '))
    b = random.randint(1,3)
    if not ((a == 1) or (a==2) or (a==3)) :
        print('Incorect value ! Try again !')
        continue
    print('#'*40)
    print('You choose : ',a)
    print('Your oponent choose : ',b)

    def result(a,b) :
        if (a==1 and b==1) :
            print('It\'s a tie !')
        elif (a==1 and b==2) :
            print('You loose !')
        elif (a==1 and b==3) :
            print('You won !')
        elif (a==2 and b==2) :
            print('It\'s a tie !')
        elif (a==2 and b==1) :
            print('You won !')
        elif (a==2 and b==3) :
            print('You loose !')
        elif (a==3 and b==3) :
            print('It\'s a tie !')
        elif (a==3 and b==2) :
            print('You won !')
        elif (a==3 and b==1) :
            print('You loose !')
        

    result(a,b)

    c = input('Do You want to play again ? (Y/N): ')
    if ((c =='Y') or (c=='y')) :
        continue
    else :
        break
