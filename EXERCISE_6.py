'''Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)'''

a = input('Write Your sentence: ')
b = a[len(a)::-1]
print(a,b)

if a == b :
    print('Your sentence: ',a,'is a palindrome')
else: 
    print('Your sentence: ',a,'is not a palindrome')
