import numpy as ny
n=1000
m=100
count=0

for i in range(1,n):
	mx=-101
	x=0
	for j in range(1,m):
       		sum=ny.random.randint(2)
       		if sum==0:
           		x=x-1
       		else:
          		x=x+1
       		if x >= mx:
         	    	mx=x
	if mx >= 25:
		count=count+1

z=float(count)/float(n)
print(float(z))
	       
