'''Write a password generator in Python. Be creative with how you generate passwords 
- strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
The passwords should be random, generating a new password every time the user asks for a new password. 
Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.'''

import random

while True:
    print(
        '<<<<< PASSWORDS GENERATOR >>>>>\n\n1-weak password\n2-strong password\n\nHow strong password would You like to generate?')
    a = int(input('>>> '))
    print('How many characters should have the password ?')
    n = int(input('>>> '))
    set1 = '1234567890qwertyuiopasdfghjklzxcvbnm'
    set2 = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*'


    def generator_1(n):
        print(''.join(random.sample(set1, n)))


    def generator_2(n):
        print(''.join(random.sample(set2, n)))


    if a == 1:
        generator_1(n)
    elif a == 2:
        generator_2(n)
    else:
        continue
    print('\n\n____________')
