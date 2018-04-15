import numpy as np
import random

count=0;

for i in range (0,1000):
	y=0
	while True:
		rwalk=random.randint(0,1)
		if rwalk==0:
			y=y+1
		else:
			y=y-1
		if y==0:
			count=count+1;
			break

ans=float(count)/1000
print (ans);
