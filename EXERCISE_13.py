'''Write a program that asks the user how many Fibonnaci numbers to generate
and then generates them. Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is 
the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)'''

n = int(input('How many Fibonnaci numbers  generate ? :\n >>> '))

def fibonnaci(n) :
	x = [1,1]
	for k in  range(1,n) :
		xk = x[k]+x[k-1]
		x.append(xk)
	print(x[0:n ])

fibonnaci(n)
