import numpy as np
import random

n =10000
count=0;

for i in range (0,n):
	y=0
	x=0
	for j in range(10000):
		rwalk1=random.randint(0,1)
		rwalk2 = random.randint(0,1)
		if rwalk2==0:
			y=y+1
		elif rwalk2==1:
			y=y-1
		if rwalk1==0:
			x=x+1
		elif rwalk1==1:
			x=x-1
		if y==0 and x==0:
			count=count+1
			break

ans=float(count)/n
print (ans)
