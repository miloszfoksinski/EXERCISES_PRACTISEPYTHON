'''Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message
 to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
 If check divides evenly into num, tell that to the user. If not, print a different appropriate message.''' 

x = int(input('Write a number: '))

if (x==0) :
    print('Your number: 0 is neither even or odd number')
elif (x%4 == 0) :
    print('Your number: ',x, ' is even number and is divided by 4')
elif (x%2 == 0) :
    print('Your number: ',x, ' is even number')
else :
    print('Your number: ',x,' is odd number')

num = int(input('Write num: '))
check = int(input('Write check number to check num: '))

if (num%check == 0):
    print('Your check divides evenly into num')
else :
    print(' Your check doesn\'t divides evenly into num')
