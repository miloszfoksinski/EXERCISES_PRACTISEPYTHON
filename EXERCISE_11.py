"""Ask the user for a number and determine whether the number is prime or not."""

x = int(input('Write Your number to check whether it is prime or not: '))


count = 0
for a in range (1,x+1):
	if x%a == 0:
		count +=1
if count > 2 :
	print('Your number ',x,' is not prime')
else:
	 print('Your number ',x,' is  prime')
