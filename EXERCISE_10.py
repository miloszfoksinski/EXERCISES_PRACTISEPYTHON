"""Take two lists, say for example these two:

	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common
between the lists (without duplicates). Make sure your program works on two lists of different sizes.
Write this using at least one list comprehension
Extra:

Randomly generate two lists to test this"""

import random

list_a = random.sample(range(10),random.randint(2,9))
list_b = random.sample(range(10),random.randint(2,9))
list_c = []
print('list A : ',list_a)
print('list B : ',list_b)

#for b in list_b :
#    if b  in list_a:
#        list_c.append(b)
list_c = list(set([b for b in list_b if b  in list_a]))
#print(list_c)

#list_c = list(set(list_c))
   
print('Common elements: ',list_c)

