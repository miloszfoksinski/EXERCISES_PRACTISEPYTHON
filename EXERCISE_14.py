'''Write a program (function!) that takes a list and returns a new list that contains
all the elements of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a list, 
and another using sets.'''



x= [1,4,5,6,7,4,6,5,4,3,2,1,2,2,9,8,7,6,5,4,3,2,1]

#def shortcut(x) :
#	y=[]
#	for a in x :
#		if a not in y :
#			y.append(a)
#	print(y)

#shortcut(x)

def shortcut_2(x) :
	y=list(set(x))
	print(y)

shortcut_2(x)


