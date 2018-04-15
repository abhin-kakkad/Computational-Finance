import numpy as np
import random

n =1000
count=0
nt=10000

for i in range (0,n):
	y=0
	x=0
	z=0
	for j in range(nt):
		rwalk1=random.randint(0,1)
		rwalk2 = random.randint(0,1)
		rwalk3 = random.randint(0,1)
		if rwalk2==0:
			y=y+1
		elif rwalk2==1:
			y=y-1
		if rwalk1==0:
			x=x+1
		elif rwalk1==1:
			x=x-1
		if rwalk3==0:
			z=z+1
		elif rwalk3==1:
			z=z-1
		if y==0 and x==0 and z==0:
			count=count+1
			break

ans=float(count)/n
print (ans)
