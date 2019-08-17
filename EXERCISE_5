'''Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists
(without duplicates). Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python
(don’t worry if you can’t figure this out at this point - we’ll get to it soon)'''

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
import random
#a = range(1, random.randint(1,30), random.randint(1,5))

#b = range(1, random.randint(10,40), random.randint(2,7))

a = random.sample(range(1,100),random.randint(1,20))
b = random.sample(range(1,100),random.randint(1,15))

print(a)
print(b)
'''c =[]
d=[]
f=[]


for x in a :
    if x not in c :
        c.append(x)
print(c)

for y in b :
    if y not in d :
        d.append(y)
print(d)
e=c+d
print(e)

for z in e :
    if z not in f :
        f.append(z)
print(f)'''


print(list((set(a)) & (set(b))))
